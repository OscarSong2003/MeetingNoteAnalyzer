from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NotesSerializer
from .models import Notes, Audio_store 
from .forms import AudioForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .media.documents.audioProcessing import recognitionAndSegmentation, getTranscript
from .media.documents.nameEntityRec.entity import nameEntityRecognition
# Create your views here.
import os
class NotesView(viewsets.ModelViewSet): 
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save()
            fileName = request.FILES['record'].name
            # recognitionAndSegmentation(f'notes/media/documents/{fileName}', fileName)
            getTranscript(f'notes/media/documents/{fileName}', fileName)
            transcript_path = os.path.abspath(os.path.join('notes/media/documents/transcript'))
            print(transcript_path);
            nameEntityRecognition(transcript_path); 
            return HttpResponseRedirect('http://localhost:8880/viewer/')
            # return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'aud.html', {'form' : form}) 

