from django.shortcuts import render
from .forms import ProjectUploadForm
# Create your views here.

def dashboard(request):
    form = ProjectUploadForm()
    context = {
    'form': form,
    }
    return render(request, 'dashboard.html', context)
