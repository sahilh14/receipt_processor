from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from process.views import process_receipt, get_points

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path(
        "receipt_input_page/",
        TemplateView.as_view(template_name="receipt_input_page.html"),
        name="receipt_input_page",
    ),
    path(
        "id_input_page/",
        TemplateView.as_view(template_name="id_input_page.html"),
        name="id_input_page",
    ),
    path("receipts/process/", process_receipt, name="process_receipt"),
    re_path(r"^receipts/(?P<id>.+)/points/$", get_points, name="get_points"),
]
