from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successfully')
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})

def success_view(request):

    return render(request, 'successfully.html')