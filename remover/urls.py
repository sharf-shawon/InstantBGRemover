from django.shortcuts import render
from django.urls import path
from remover.views import remove_background, index, tos, about, faq

urlpatterns = [
    path("", index, name="index"),  # This will serve your frontend
    path("terms-of-service/", tos, name="tos"),
    path("about-us/", about, name="about"),
    path("frequently-asked-questions/", faq, name="faq"),
    path("remove-bg/", remove_background, name="remove_bg"),
]
