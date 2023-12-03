from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'Post':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
