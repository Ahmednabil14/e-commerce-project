from django.urls import path
from .views import display_accounts, update_accounts, remove_account, add_new_account, display_account_details

urlpatterns = [
    path('', display_accounts, name='display_accounts'),
    path('create/', add_new_account, name='add_new_account'),
    path('delete/<int:id>/', remove_account, name='remove_account'),
    path('update/<int:id>/', update_accounts, name='update_accounts'),
    path('details/', display_account_details, name='display_account_details')
]
