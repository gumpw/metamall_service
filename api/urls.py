from django.conf.urls import include, url

from api import views

urlpatterns = [
    url(r'^api/', views),
    url(r'^sms/', views.sms),
    url(r'^province/', views.province),
    url(r'^city/', views.city),
    url(r'^area/', views.area),
]
