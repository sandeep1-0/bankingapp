from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'ifsc',views.BankIfsc.as_view()),
    url(r'bank',views.BankName.as_view())
]