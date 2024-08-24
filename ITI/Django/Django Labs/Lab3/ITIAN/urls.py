from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Home view using a template
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Acounts/', include('account.urls')),  # Adjust with the correct app name if needed
    path('Track/', include('track.urls')),
    path('Trainee/', include('trainee.urls')),
    path('', home, name='home'),  # Set home as the root URL
]
