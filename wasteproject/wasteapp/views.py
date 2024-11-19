from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
import os
from . models import User,Waste
from django.conf import settings
from tensorflow.keras.models import load_model
model_path=os.path.join(settings.BASE_DIR,'models','efficientnetb0_waste_classificationcpunew.keras')
model = load_model(model_path)
import cv2
import numpy as np
# Create your views here.
def index(request):
    return render(request, 'index.html')

def process_image(image_path):
    IMG_SIZE = 224
    custom_image = cv2.imread(image_path)
    if custom_image is None:
        raise ValueError(f"Image not found at path: {image_path}")
    custom_image = cv2.resize(custom_image, (IMG_SIZE, IMG_SIZE))
    custom_image = custom_image.astype('float32') / 255.0
    custom_image = np.expand_dims(custom_image, axis=0)
    print("Custom image shape:", custom_image.shape)
    return custom_image

def delete_ac(request):
    email = request.session.get('email')
    if email:
        user = get_object_or_404(User, email=email)
        user.delete()
        return render(request, 'index.html')
    return render(request, 'user_login.html')

def logout(request):
    request.session.flush()
    return render(request, 'index.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        place = request.POST.get('place')
        phonenumber = request.POST.get('phonenumber')
        profile_picture = request.FILES.get('profile_picture')
        if User.objects.filter(email=email).exists():
            alert_message = "<script>alert('EMAIL ALREADY EXIST');window.location.href='/user_registration/';</script>"
            return HttpResponse(alert_message)
    
        User(username=username, password=password, email=email,place=place, phonenumber=phonenumber, profile_picture=profile_picture).save()
        return redirect('user_login')
    return render(request, 'user_registration.html')

def user_login(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email1, password=password)
        if user:
            u=User.objects.get(email=email1,password=password)
            id =u.id
            email1 =u.email
            password=u.password
            request.session['id']=id
            request.session['email']=email1
            request.session['password']=password
            return redirect('user_home')
        return render(request, 'user_login.html')
    return render(request,'user_login.html')

def user_home(request):
    return render(request, 'user_home.html')


def user_profile(request):
    email = request.session.get('email')
    if not email:
        return render(request, 'user_login.html', {'error': 'User not logged in'})
    user = get_object_or_404(User, email=email)
    user_info = {
        'username': user.username,       
        'phonenumber': user.phonenumber,
        'email': user.email,
        'password': user.password,
        'place': user.place,
        'profile_picture': user.profile_picture
    }
    return render(request, 'user_profile.html', user_info)
#userprofileupdate
def user_update(request):
    email=request.session['email']
    cr =User.objects.get(email=email)
    if cr:
        user_info = {
            'username':cr.username,
            'phonenumber':cr.phonenumber,
            'email':cr.email,
            'password':cr.password,
            'place':cr.place,
            'profile_picture':cr.profile_picture
        }
        return render(request,'user_update.html',user_info)
    else:
        return render(request,'user_update.html')

def proupdate(request):
    email = request.session.get('email')
    if not email:
        return redirect('adminlogin') 
    if request.method == "POST":
        user = User.objects.get(email=email)
        username = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        place = request.POST.get('place')
        profile_picture = request.FILES.get('profile_picture')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user.username = username
        user.phonenumber = phonenumber
        user.place = place
        user.email = email
        user.password = password
        
        if profile_picture :
            user.profile_picture = profile_picture
        
        user.save()
        
        user_info = {
            'username':user.username,
            'phonenumber':user.phonenumber,
            'email':user.email,
            'password':user.password,
            'place':user.place,
            'profile_picture':user.profile_picture
        }
        
        return render(request, 'user_profile.html', user_info)
    else:
        return render(request, 'user_update.html')
    

def upload_waste(request):
    if request.method == 'POST':
        waste_image = request.FILES.get('waste_image')
        wst = Waste(waste_image=waste_image)
        wst.save()
        impath = wst.waste_image.path
        pre_img = process_image(impath)
        predictions = model.predict(pre_img)
        predicted_class = np.argmax(predictions, axis=1)
        class_labels = ['biological', 'metal', 'paper', 'plastic']
        predicted_label = class_labels[predicted_class[0]] 
        print('Prediction Result:', predicted_label)
        return render(request, 'upload_waste.html', {'predictions': predicted_label})
    return render(request, 'upload_waste.html')

def admin_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    e='admin'
    p='1234'
    if email==e and password==p:
        return redirect('admin_home')
    return render(request, 'admin_login.html')


def admin_home(request):
    return render(request, 'admin_home.html')

def user_list(request):
    user = User.objects.all()
    return render(request, 'user_list.html', {'users': user})

def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user_list')


