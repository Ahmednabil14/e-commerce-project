from django.contrib import admin
from django.urls import path, include
from trainee.views import add_new_trainee  # Import the create view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accounts/', include('account.urls')),
    path('Track/', include('track.urls')),
    path('Trainee/', include('trainee.urls')),
    path('', include('trainee.urls')),  # Add this line to include trainee.urls in the root
    path('create/', add_new_trainee, name='add_new_trainee'),  # Add this line to directly access /create/
]
