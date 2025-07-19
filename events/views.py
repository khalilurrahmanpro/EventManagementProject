from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from .forms import EventForm
from django.db.models import Q

def event_list(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
    else:
        events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})
