from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from time import sleep
from django.core.mail import send_mail
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny


def signup(request):
    if request.method=='POST':
        forms=CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'signup.html',{'forms':form}) 

def Register(request):
    return render(request,'registration.html')

class RegisterView(generics.ListCreateAPIView):
    queryset = Myuser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes =[AllowAny]

class RegisterRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Myuser.objects.all()
    serializer_class = RegisterSerializer

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def login_view(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        user=authenticate(request,username=phone_number,password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                # Redirect to a password change page
                return redirect('useradmin') 
            return redirect('userDashboard')
        else:
            return render(request,'login.html',{'name':{'info':"Invalid phone number or password"}})
    else:
        messages.error(request,"Enter phone number and password")
    return render(request,'login.html')

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             # Update the user's session to reflect the new password
#             update_session_auth_hash(request, form.user)
#             # Mark that the user no longer needs to change their password
#             request.user.need_password_change = False
#             #console.log('the data in the database is :...........' , )
#             request.user.save()
#             messages.success(request, 'Your password has been changed successfully.')
#             sleep(10)
#             return redirect('useradmin')  # Redirect to home or desired page
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {'form': form})


@login_required(login_url='/login/')
def userDashboard(request):
    user = request.user
    return render(request,'userDashboard.html',{'user':user,'totals':total})

def contactus(request):
    info={}
    if request.method == 'POST':
        fullname=request.POST.get('Fullname')
        email=request.POST.get('Email')
        subject=request.POST.get('Subject')
        message=request.POST.get('message')
        if not fullname or not email or not message or not subject:
            return HttpResponse("All fields are required!", status=400)
        contact=Feedback(FUll_Name=fullname,Email=email,Subject=subject,Message=message) # type: ignore
        contact.save()
        info={'name':"Thank you for sending us message!!"}
        return render(request,'contactus.html',{'info':info})
    return render(request,'contactus.html')


sum1,sum2,sum3,sum4,sum5=0,0,0,0,0
for g in Myuser.objects.all():
    sum1+=1

for g in ikinamba.objects.all():
    sum2+=1

for g in Car.objects.all():
    sum3+=1

for g in Service.objects.all():
    sum4+=1

total={
    'totaluser':sum1,
    'totalikinamba':sum2,
    'totalcars':sum3,
    'totalservices':sum4,
    # 'totalchw':sum5,
}



@login_required(login_url='/login/')
def useradmin(request):
    user=request.user
    return render(request,'admindashboard.html',{'user':user,'totals':total})


@login_required
def setting_view(request):
    return render(request,'settings.html')
@login_required
def userprofile_view(request):
    return render(request,'userprofile.html')
def notification_view(request):
    return render(request,'notifications.html')

@login_required
def pandb_view(request):
    return render(request,'parentsandbaby.html')  


@login_required  
def vandm_view(request):
    return render(request,'vaccineandmeasure.html')


def logout_view(request):
    if request.method == 'POST':
        Session.objects.filter(session_key=request.session.session_key).delete()
        logout(request)
        return redirect('login')
    logout(request)
    return redirect('login')

@login_required
def babies(request):
    return render(request,'babies.html') 

@login_required
def ikinambaList(request):
    return render(request,'ikinamba_list.html') 

@login_required
def carList(request):
    return render(request,'cars.html') 
@login_required
def carviewlist(request):
    return render(request,'car_list.html') 

@login_required
def serviceList(request):
    return render(request,'services.html') 
@login_required
def serviceViewList(request):
    return render(request,'service_list.html') 
# List all entries or create a new entry
class ikinambaListCreateView(generics.ListCreateAPIView):
    queryset = ikinamba.objects.all()
    serializer_class = ikinambaSerializer

# Retrieve, update, or delete a specific entry
class ikinambaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ikinamba.objects.all()
    serializer_class = ikinambaSerializer

# List and create cars
class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Retrieve, update, or delete a car
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class SubscriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# Create your views here.
