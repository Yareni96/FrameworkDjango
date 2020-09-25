from django.shortcuts import render,redirect
from .forms import FlorForm

# Create your views here.
def Home(request):
    return render(request,'index.html')

def crearFlor(request):
    if request.method == 'POST':
        flor_form = FlorForm(request.POST)
        if flor_form.is_valid():
            flor_form.save()
            return redirect('index')
    
    else:
        flor_form = FlorForm()
    return render(request,'flores/crear_flor.html',{'flor_form':flor_form})