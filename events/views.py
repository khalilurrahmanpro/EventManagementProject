from django.shortcuts import render,redirect
from .forms import EventForm
from .models import Event
from django.utils.timezone import now
from django.db.models import Count
from .models import Category
from .models import Participant

def event_list(request):
    events = Event.objects.select_related('category').prefetch_related('participant_set')
    for event in events:
        event.participant_count = event.participant_set.count()
    
    return render(request, 'events/event_list.html', {'events': events})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'events/participant_list.html', {'participants': participants})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    
    return render(request, 'events/create_event.html', {'form': form})

def dashboard(request):
    today = now().date()

    total_events = Event.objects.count()
    total_participants = Participant.objects.count()
    upcoming_events = Event.objects.filter(date__gt=today).count()
    past_events = Event.objects.filter(date__lt=today).count()
    todays_events = Event.objects.filter(date=today)

    context = {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events,
    }

    return render(request, 'events/dashboard.html', context)
