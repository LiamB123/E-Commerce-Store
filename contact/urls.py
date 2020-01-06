from django.conf.urls import url
from .views import contact_us, sales_form

urlpatterns=[
    url(r'^chat-us', contact_us, name="contact"),
    url(r'^chat-us-business', sales_form, name="sell_yours")

    ]