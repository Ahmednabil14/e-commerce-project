from django.shortcuts import render, redirect
from .models import Track

def list_track(request):
    context = {}
    context['tracks'] = Track.objects.all()
    return render(request, 'track/list.html', context)

def update_track(request, id):    
    track = Track.objects.get(pk=id)
    if request.method == 'POST':
        track.track_name = request.POST.get('track_name')
        track.save()
        return redirect('list_track')
    return render(request, 'track/update.html', {'track': track})

def delete_track(request, id): 
    track = Track.objects.get(pk=id)
    track.delete()
    return redirect('list_track')

def create_track(request):
    if request.method == 'POST':
        track_name = request.POST.get('track_name')
        if track_name:
            Track.objects.create(track_name=track_name)
            return redirect('list_track')
    return render(request, 'track/create.html')

def show_details(request, id):
    context = {}
    context['track'] = Track.objects.get(id=id)
    return render(request, 'track/details.html', context)
