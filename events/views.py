from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category, Participant
from .forms import EventForm, CategoryForm, ParticipantForm
from django.utils.timezone import now
from django.db.models import Count, Q
from django.contrib import messages


def event_list(request):
    query = request.GET.get('q')
    events = Event.objects.select_related('category')
    if query:
        events = events.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'events/event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect('event_list')
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Create Event'})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Update Event'})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('event_list')


def category_list(request):
    categories = Category.objects.annotate(event_count=Count('event'))
    return render(request, 'events/category_list.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'events/category_form.html', {'form': form, 'title': 'Create Category'})

def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'events/category_form.html', {'form': form, 'title': 'Update Category'})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect('category_list')


def participant_list(request):
    participants = Participant.objects.prefetch_related('events').all()
    return render(request, 'events/participant_list.html', {'participants': participants})


def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Participant added successfully!")
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'events/participant_form.html', {'form': form, 'title': 'Add Participant'})

def update_participant(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, "Participant updated successfully!")
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'events/participant_form.html', {'form': form, 'title': 'Update Participant'})

def delete_participant(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.delete()
    messages.success(request, "Participant deleted successfully!")
    return redirect('participant_list')


def dashboard(request):
    total_events = Event.objects.count()
    total_participants = sum(event.participant_set.count() for event in Event.objects.all())
    upcoming_events = Event.objects.filter(date__gte=now().date()).count()
    past_events = Event.objects.filter(date__lt=now().date()).count()
    today_events = Event.objects.filter(date=now().date())

    context = {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'today_events': today_events
    }
    return render(request, 'events/dashboard.html', context)
