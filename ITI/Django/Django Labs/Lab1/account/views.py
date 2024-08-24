from django.shortcuts import render

# Create your views here.


def add_new_account(request):
    return render(request, 'account/create.html')

def display_accounts(request):
    return render(request, 'account/list.html')

def remove_account(request, id):    
    return render(request, 'account/delete.html', {'id': id})

def update_accounts(request, id):    
    return render(request, 'account/update.html', {'id': id})

def display_account_details(request):
    return render(request, 'account/details.html')
