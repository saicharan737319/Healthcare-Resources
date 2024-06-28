from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = "main"

urlpatterns = [
    path('',loginUser,name='loginUser'),
    path('home/',home,name='home'),
    path('drhome/',drhome,name='drhome'),
    path('home/appointment/',appointment,name='appointment'),
    path('home/appointment/drprofile/',profile,name='profile'),
    path('home/appointment/drbooking/',booking,name='booking'),
    path('home/appointment/bookinghr/',bookinghistory,name='bookinghistory'),

    path('home/test/',test,name='test'),
    path('home/test/lab/',lab,name='labtest'),
    path('home/test/daily/',daily,name='daily'),
    path('home/test/history/',history,name='history'),
    path('home/pharmacy/',pharmacy,name='pharmacy'),

    path('drhome/drpharmacy/',drpharmacy,name='drpharmacy'),
    path('drhome/drpharmacy/drindex/',drindex,name='drindex'),
    path('drhome/drappointment/',drappointment,name='drappointment'),
    path('drhome/drpharmacy/products/',products,name='products'),
    path('drhome/drpharmacy/cart/',cart,name='cart'),
     path('drhome/drappointment/doctorappointment/',doctorappointment,name='doctorappointment'),
    path('drhome/drappointment/onlineprescription/',onlineprescription,name='onlineprescription'),
    path('drhome/drappointment/patienthistory/',patienthistory,name='patienthistory'),
    path('drhome/drappointment/referral/',referral,name='referral'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)