from django.shortcuts import render
from .models import ProjectModel

# Create your views here.
def myproject(request):
    projectobj = ProjectModel.objects.all()
    context = {
    "data" : projectobj,
    }
    return render(request, 'myproject.html', context)


def myprojectdetail(request, slug):
    get_single_object = ProjectModel.objects.get(title = slug)
    context = {
    'data': get_single_object,
    }
    return render(request, 'myprojectdetail.html', context)
