from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^sms/', views.sms),
    url(r'^province/', views.province),
    url(r'^city/', views.city),
    url(r'^area/', views.area),
    url(r'^test/', views.test),
]
