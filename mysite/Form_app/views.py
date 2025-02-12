from django.http import JsonResponse
from django.shortcuts import render
from . forms import FileUploadForm
from .models import FileUpload

# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form=FileUploadForm(request.POST,request.FILES)
    
        if form.is_valid():
          form.save() #model form
          
          #normal form
        #   file_data = FileUpload(name=form.cleaned_data['name'],file=form.cleaned_data['file'])
        #   file_data.save()
          
          return JsonResponse({
              "message": "File uploaded successfully"
          },status=200)
        else:
          return JsonResponse({
              "error": form.errors
          },status=400)
    else:  # GET request
        form=FileUploadForm() #generarating an empty form
        return render(request,'Form_app/file_upload.html',{'form':form})