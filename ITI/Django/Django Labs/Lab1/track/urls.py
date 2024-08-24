from django.urls import path
from .views import display_tracks, update_track, remove_track, create_track, show_details

urlpatterns = [
    path('', display_tracks, name='display_tracks'),
    path('create/', create_track, name='create_track'),
    path('delete/<int:id>/', remove_track, name='remove_track'),
    path('update/<int:id>/', update_track, name='update_track'),
    path('details/', show_details, name='show_details')
]
