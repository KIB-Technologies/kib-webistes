from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),

    path('about-kib-technologies/', views.about, name='about'),

    path('kib-technologies-products/', views.products, name='products'),
    
    #it_services
    path('kib-technologies-it-services', views.it_services, name='it_services'),
    path('kib-technologies-web-development-services', views.web_development, name='web_development'),
    path('kib-technologies-mobile-app-development-services', views.mobile_app_development, name='mobile_app_development'),
    path('kib-technologies-software-development-services', views.software_development, name='software_development'),
    path('kib-technologies-game-development-services', views.game_development, name='game_development'),
    path('kib-technologies-cyber-security-services', views.cyber_security, name='cyber_security'),
    path('kib-technologies-graphic-designing-services', views.graphic_designing, name='graphic_designing'),

    #marketing_services
    path('kib-technologies-marketing-services', views.marketing_services, name='marketing_services'),
    path('kib-technologies-multimedia-marketing', views.multimedia_marketing, name='multimedia_marketing'),
    path('kib-technologies-cinema-branding', views.cinema_branding, name='cinema_branding'),
    path('kib-technologies-event-managment', views.event_managment, name='event_managment'),
    path('kib-technologies-digital-marketing', views.digital_marketing, name='digital_marketing'),
    path('kib-technologies-out-of-home-ads', views.out_of_home_ads, name='out_of_home_ads'),
    
    path('join-kib-technologies/', views.career, name='career'),
    path('blog-kib-technologies/', views.blog, name='blog'),
    path('blog-kib-technologies/<bid>', views.blogfull, name='blogfull'),

    path('contact-kib-technologies/', views.contact, name='contact'),
    path('return-policy-kib-technologies/', views.returnpolicy, name='returns'),
    path('login-into-kibtechnologies/', views.login, name='login'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)