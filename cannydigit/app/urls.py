from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('portfolio', views.Portfolio, name="portfolio"),
    path('about-us', views.Aboutus, name="aboutus"),
    path('careers', views.Careers, name="careers"),
    path('blog', views.Blog, name="blog"),
    path('blog/<slug:slug>', views.BlogDescription, name="blogdesc"),
    path('products', views.Products, name="products"),
    # App Development
    path('mobile-application-development', views.MobileAppDevelopment, name="mobileapp"),
    path('ios-application-development', views.IOSAppDevelopment, name="iosapp"),
    path('android-application-development', views.AndroidAppDevelopment, name="androidapp"),
    path('native-application-development', views.NativeAppDevelopment, name="nativeapp"),
    path('hybrid-application-development', views.HybridAppDevelopment, name="hybridapp"),
    path('xamin-application-development', views.XaminAppDevelopment, name="xaminapp"),
    path('koltin-application-development', views.KoltinAppDevelopment, name="koltinapp"),
    # Services
    path('web-application-development', views.WebAppDevelopment, name="webapp"),
    path('api-development', views.APIDevelopment, name="apidevop"),
    path('iot-development', views.IOTDevelopment, name="iotdevop"),
    path('ui-ux-design', views.UIUXDesign, name="ui-ux"),
    path('full-scale-development', views.FullScaleDevelopment, name="fullscale"),
    path('smart-x-team', views.SmartXTeam, name="smartxteam"),
    path('startup-accelerator', views.StartupAccelerator, name="startup"),
] 