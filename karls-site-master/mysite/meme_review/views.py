from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView
from .forms import MemeUploadForm
from .models import MemeUpload
from django.views.generic import TemplateView

def home(request):
    images = MemeUpload.objects.order_by('-pub_date')[0:]
    return render(request, 'meme_review/home.html', {'images': images})

def upload(request):
    if request.method == "POST":
            upload_form = MemeUploadForm(request.POST, request.FILES)
            #upload_form.image = request.FILES['image']

            if upload_form.is_valid():
                upload_form.save()
                return HttpResponseRedirect(reverse('meme_review:home'))
            else:
                print(MemeUploadForm.errors)

    else:
        upload_form = MemeUploadForm()
    return render(request,'meme_review/upload_page.html', {'MemeUploadForm': upload_form})

class BioView(TemplateView):
    template_name = "meme_review/bio.html"
