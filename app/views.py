from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from . import models

# Create your views here.


def Home(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['email']
        phone = request.POST['Phone_No']
        subject = request.POST['Subject']
        message = request.POST['Message']
        proposal = request.POST['proposal']
        emailcheck = models.Contact.objects.filter(Email=email)
        if not emailcheck:
            models.Contact.objects.create(
                Name=name, Email=email, Phone_No=phone, Subject=subject, Message=message, Proposal=proposal)
            messages.success(
                request, '<strong class="me-2">Sucessfully Submitted</strong> We will Reach you Soon')
        else:
            messages.warning(
                request, '<strong class="me-2">Email Already Exist</strong> Please Check Your Mail Given Mail')

    return render(request, "index.html")


def Portfolio(request):
    return render(request, "portfolio.html")


def Aboutus(request):
    return render(request, "aboutus.html")


def Careers(request):
    return render(request, "careers.html")


def Blog(request):
    if 'blogs' in request.GET:
        blogsearch = request.GET.get('blogs')
        print(blogsearch)
        Lookups = Q(Title__icontains=blogsearch) | Q(Description__icontains=blogsearch)
        blogs = models.Blog.objects.filter(Lookups)
    else:
        blogs = models.Blog.objects.all()

    recent_blogs = models.Blog.objects.order_by('-id')[:4]

    page = request.GET.get('page',1)
    paginator = Paginator(blogs, 10)
    final_blogs = paginator.page(page)
    return render(request, "blog.html",{
        'blogs':final_blogs,
        'recent_blogs':recent_blogs
        })

def BlogDescription(request, slug):
    blog = models.Blog.objects.filter(Slug=slug)
    return render(request, "blogdesc.html",{'blog':blog})

def Products(request):
    return render(request, "products.html")


# App Devolopment
def MobileAppDevelopment(request):
    return render(request, "mobile_app/mobileapp.html")


def IOSAppDevelopment(request):
    return render(request, "mobile_app/iosapp.html")


def AndroidAppDevelopment(request):
    return render(request, "mobile_app/androidapp.html")


def NativeAppDevelopment(request):
    return render(request, "mobile_app/nativeapp.html")


def HybridAppDevelopment(request):
    return render(request, "mobile_app/hybridapp.html")


def XaminAppDevelopment(request):
    return render(request, "mobile_app/xaminapp.html")


def KoltinAppDevelopment(request):
    return render(request, "mobile_app/koltinapp.html")

# Services


def WebAppDevelopment(request):
    return render(request, "services/webapp.html")


def APIDevelopment(request):
    return render(request, "services/apidevop.html")


def IOTDevelopment(request):
    return render(request, "services/iotdevop.html")


def UIUXDesign(request):
    return render(request, "services/ui-ux.html")


def FullScaleDevelopment(request):
    return render(request, "services/fullscale.html")


def SmartXTeam(request):
    return render(request, "services/smartxteam.html")


def StartupAccelerator(request):
    return render(request, "services/startup.html")
