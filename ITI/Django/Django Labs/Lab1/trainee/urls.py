from django.urls import path
from .views import get_trainees_list, update_trainee, remove_trainee, add_new_trainee, display_trainee_details

urlpatterns = [
    path('', get_trainees_list, name='get_trainees_list'),
    path('update/<int:id>/', update_trainee, name='update_trainee'),
    path('delete/<int:id>/', remove_trainee, name='remove_trainee'),
    path('create/', add_new_trainee, name='add_new_trainee'),
    path('details/<int:id>/', display_trainee_details, name='display_trainee_details')
]
