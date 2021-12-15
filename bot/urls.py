from django.urls import path
from bot import views

urlpatterns = [
    path('', views.LinkHandler.as_view(), name='bot'),
    path(r'^\d{8}/$', views.LinkHandler.as_view(), name='refer_link'),
    path(r'^\d{8}[=not_found]/$', views.LinkHandler.as_view(), name='referal_error'),
]
