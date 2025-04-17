from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ This will now call your `home` view
]
