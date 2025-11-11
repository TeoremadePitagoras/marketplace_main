from django.urls import path
from .views import home, contact, detail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', detail, name='detail'),
]
