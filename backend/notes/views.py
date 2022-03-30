from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NotesSerializer
from .models import Notes, Audio_store 
from .forms import AudioForm
from django.http import HttpResponse
from django.conf import settings
from .media.documents.audioProcessing import recognitionAndSegmentation

# Create your views here.

class NotesView(viewsets.ModelViewSet): 
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

def Audio_store(request):
    if request.method == 'POST': 

        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save()
            fileName = request.FILES['record'].name
            recognitionAndSegmentation(f'notes/media/documents/{fileName}', fileName)
            print(fileName)
     
            return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'aud.html', {'form' : form}) 

