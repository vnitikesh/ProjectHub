from django.shortcuts import render, redirect
from .models import Directory
import json

# Create your views here.
def wohoo(request):
    if(request.method == 'POST'):
        abc = {}

        docfile = request.FILES['file_field']
        abc['file_field'] = docfile
        #print(len(request.POST['directories']))
        directory = json.loads(request.POST['directories'])
        #json.stringify()
        #print("hey")
        #print(type(directory))
        #print(docfile)
        #print(directory)
        new_doc = Directory(docfile = docfile, directory_name = directory)
        new_doc.save()
        return redirect('doc')
    documents = Directory.objects.all()
    print(documents)
    #for i in documents:

        #print("hi")
        #print(i.docfile)
        #print(type(json.loads(i.directory_name)))
    return render(request, 'wohoo.html', {'documents': documents})
