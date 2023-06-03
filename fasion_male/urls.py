from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('shop/', include('product.urls')),
    path('blog/', include('blog.urls')),
    path('contact-us/', include('contact.urls')),
    path('about-us/', include('about.urls')),
    path('captcha/', include('captcha.urls')),
    path('basket/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
