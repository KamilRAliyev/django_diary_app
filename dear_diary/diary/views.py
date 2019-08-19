from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm


def index(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {
        'entries': entries
    }
    return render(request, 'diary/index.html', context)


def add(request):
    if (request.method == 'POST'):
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    
    context = {'form':form}
    return render(request, 'diary/add.html',context)
