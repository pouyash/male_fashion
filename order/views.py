from datetime import datetime

import sweetify
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from order.models import Order, OrderDetail
from product.models import Product
import requests
import json

@method_decorator(login_required, name='dispatch')
class OrderView(View):
    def get(self, request: HttpRequest):
        user = request.user
        order = Order.objects.filter(is_paid=False, user=user).first()
        order_details = OrderDetail.objects.filter(order=order)
        context = {
            'order_details': order_details,
            'order': order,
        }
        return render(request, 'order/basket.html', context)


@method_decorator(login_required, name='dispatch')
class AddToCardView(View):
    def get(self, request, slug):
        user = request.user
        product = get_object_or_404(Product, slug=slug)
        order, res = Order.objects.get_or_create(user=user, is_paid=False)

        order_detail = OrderDetail.objects.filter(order=order, product=product).exists()
        if order_detail:
            Order_detail: OrderDetail = OrderDetail.objects.filter(order=order, product=product).first()
            Order_detail.count += 1
            final_price = Order_detail.final_price
            Order_detail.final_price = final_price + product.price
            Order_detail.save()
        else:
            OrderDetail.objects.create(count=1, order=order, product=product, final_price=product.price * 1)
        sweetify.success(request, 'Add To Card Successfully')
        # return redirect(reverse('product', kwargs={'slug':slug}))
        return redirect(request.META.get('HTTP_REFERER'))


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"
CallbackURL = 'http://localhost:8000/basket/verify/'

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required

@login_required
def send_request(request):
    user = request.user
    order = Order.objects.filter(user=user, is_paid=False).first()
    amount = int(order.total_price())

    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        "CallbackURL": CallbackURL,
        "Description": description,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                try:
                    return redirect(ZP_API_STARTPAY + str(response['Authority']),
                                    {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                                     'authority': response['Authority']})
                except:
                    return redirect(reverse('order'))
            else:
                return redirect(reverse('order'))
        return redirect(reverse('order'))

    except requests.exceptions.Timeout:
        return redirect(reverse('order'))
    except requests.exceptions.ConnectionError:
        return redirect(reverse('order'))

@login_required
def verify(request):
    user = request.user
    order = Order.objects.filter(user=user,is_paid=False).first()
    amount = int(order.total_price())
    status = request.GET.get('Status')
    authority = request.GET['Authority']
    if status == 'OK':
        data = {
            "MerchantID": MERCHANT,
            "Amount": amount,
            "Authority": authority,
            "Description": description,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                order.is_paid = True
                order.payment_date = datetime.now()
                order.save()
                sweetify.success(request,'Payment Successfully!')
                return redirect(reverse('order'))
            else:
                sweetify.error(request,'Payment Unsuccessfully!')
                return redirect(reverse('order'))
        sweetify.error(request,'Payment Error!')
        return redirect(reverse('order'))
    sweetify.error(request,'Payment Not Done!')
    return redirect(reverse('order'))

@login_required
def remove(request, id):
    user = request.user
    order = get_object_or_404(Order,is_paid=False, user=user)
    order_details: OrderDetail = get_object_or_404(OrderDetail,order=order, id=id)

    if order_details.delete():
        sweetify.success(request, 'Your OrderDetail Deleted.')
    else:
        sweetify.error(request, 'Your OrderDetail in Delete Error Occur!')
    if order.order_detail.count() == 0:
        if order.delete():
            sweetify.success(request, 'Your Order Deleted')
        else:
            sweetify.error(request, 'Your Order and OrderDetail in Delete Error Occur!')
    return redirect(request.META.get("HTTP_REFERER"))
