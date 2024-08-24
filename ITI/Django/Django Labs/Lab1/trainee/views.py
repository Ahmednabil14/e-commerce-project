from django.shortcuts import render

def get_trainees_list(request):
    context = {}
    trainee_list = [{"id": 1, "name": "Ahmed", "track": "python"}, {"id": 2, "name": "Awadallah", "track": "JavaScript"}]
    context['trainee_list'] = trainee_list
    print(context)
    return render(request, 'trainee/list.html', context)

def add_new_trainee(request):
    return render(request, 'trainee/create.html')

def update_trainee(request, id):    
    return render(request, 'trainee/update.html', {'id': id})

def remove_trainee(request, id):    
    return render(request, 'trainee/delete.html', {'id': id})

def display_trainee_details(request, id):
    context = {}
    context['id'] = id
    return render(request, 'trainee/details.html', context)
