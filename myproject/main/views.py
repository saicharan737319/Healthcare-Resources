from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import *

# Create your views here.

def home(request):
    print("hello")
    return render(request,'sample3.html')

def drhome(request):
    print("doctor")
    return render(request,'doctor.html')

def loginUser(request):
    all_users = User.objects.all()
    print(all_users)
    if request.method =='POST':
        form = request.POST.get('form')
        if form == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request , username=username, password=password)

            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('/drhome')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('/home')
            else:
                msg = 'invalid credentials'
        elif form == 'signup':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            is_doctor = request.POST.get('is_doctor') == 'on'
            is_patient = request.POST.get('is_patient') == 'on'

            if User.objects.filter(username=username).exists():
                print("error")
                return JsonResponse({'message':'User already exists'})
            else:
                if not is_doctor and not is_patient:
                    return render(request, 'registration/register.html', {'error': 'You must select either Doctor or Patient.'})
                elif is_doctor and not is_patient:

                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.is_doctor = is_doctor
                    user.is_patient = is_patient
                    user.save()
                    print(user)
                    return redirect('/')
                
                elif not is_doctor and is_patient:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.is_doctor = is_doctor
                    user.is_patient = is_patient
                    user.save()
                    print(user)
                    return redirect('/')
    return render(request,'login.html')

def test(request):
    return render(request, 'test.html')

def pharmacy(request):
    return render(request, 'index.html')

def daily(request):
    if request.method == 'POST':
        test_type = request.POST.get('test')
        files = request.FILES.get('filename')

        Files.objects.create(test_type = test_type,file = files,uploaded_by = request.user)
    return render(request,'daily.html')

def lab(request):
    if request.method == 'POST':
        testtype = request.POST.get('test')
        file = request.FILES.get('filename')
        Labfiles.objects.create(testtype = testtype, lab_file = file,uploaded_user=request.user)
    return render(request,'labtest.html')

# uploaded_by=request.user
#         print(uploaded_by)
#         requested_data=Files.objects.filter(uploaded_by=uploaded_by)
#         if requested_data:
#             return render(request,'daily.html',{'contents':requested_data})
#         else:
#             return render(request,'daily.html')

def history(request):
    user=request.user
    requested_daily=Files.objects.filter(uploaded_by=user)
    requested_lab=Labfiles.objects.filter(uploaded_user=user)
    return render(request, 'history.html',{'dailys':requested_daily,'labs':requested_lab})


def appointment(request):

    return render(request,'patientdrappointment.html')

def booking(request):
    if request.method == 'POST':
        docterName = request.POST.get('doctorName')
        patientName = request.POST.get('patientName')
        reason = request.POST.get('reason')
        Appointment.objects.create(docterName = docterName, patientName = patientName,reason = reason)
    return render(request,'drbooking.html')

def bookinghistory(request):
    return render(request,'bookinghistory.html')

def profile(request):
    profiles = User.objects.filter(is_doctor = True)
    return render(request,'doctorsprofile.html',{'profiles':profiles})

def drpharmacy(request):
    return render(request,'drindex.html')

def products(request):
    return render(request,'products.html')

def cart(request):
    return render(request,'cart.html')

def drappointment(request):
    doctor=request.user
    requested_data=Appointment.objects.filter( docterName = doctor)
    return render(request,'doctorappointment.html',{'contents':requested_data})

def onlineprescription(request):
    return render(request,'onlineprescription.html')

def doctorappointment(request):
    return render(request,'doctorappointment.html')

def patienthistory(request):
    return render(request,'patienthistory.html')

def referral(request):
    return render(request,'referral.html')

def drindex(request):
    return render(request,'drindex.html')

