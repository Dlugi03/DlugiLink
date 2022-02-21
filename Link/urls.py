from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('generated/', views.submit_link),
    path('<str:short_code>', views.redirect_by_short),
]
