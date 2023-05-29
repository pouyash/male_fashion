from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from about.models import Partner, OurTeam, Question, AboutImage, Message, About


class AboutUS(View):

    def get(self, request: HttpRequest):
        partners = Partner.objects.filter(is_active=True)
        our_teams = OurTeam.objects.filter(is_active=True)
        questions = Question.objects.filter(is_active=True)
        about_img = AboutImage.objects.filter(is_active=True).first()
        message = Message.objects.filter(is_active=True).first()
        about_ourteam = About.objects.filter(is_active=True, title=About.TitleChoices.OUR_TEAM).first()
        about_partner = About.objects.filter(is_active=True, title=About.TitleChoices.PARTNER).first()
        context = {
            'partners': partners,
            'our_teams': our_teams,
            'questions': questions,
            'about_img': about_img,
            'message': message,
            'about_ourteam': about_ourteam,
            'about_partner': about_partner,
        }
        return render(request, 'about/about.html', context)
