from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .forms import MemeUploadForm, CommentForm
from .models import MemeUpload, Comment

class PostDetailView(DetailView):
    model = MemeUpload
    template_name = 'meme_review/post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = CommentForm()
        data['comments'] = Comment.objects.filter(post=self.object.id).order_by('-created')
        return data

    def post(self, request, *args, **kwargs): #method named post required if you want view to post data
        self.object = post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            #comment.user = request.user
            #comment.description = request.description
            comment.save()
            return redirect(request.path_info) 

        context = self.get_context_data(object=post)
        context['comment_form'] = form
        return self.render_to_response(context)

class BioView(TemplateView):
    template_name = "meme_review/bio.html"

def home(request):
    images = MemeUpload.objects.order_by('-pub_date')[0:5]
    return render(request, 'meme_review/home.html', {'images': images})

def upload(request):
    if request.method == "POST":
            upload_form = MemeUploadForm(request.POST, request.FILES)

            if upload_form.is_valid():
                upload_form.save()
                return HttpResponseRedirect(reverse('meme_review:home'))
            else:
                print(MemeUploadForm.errors)
    else:
        upload_form = MemeUploadForm()
    return render(request,'meme_review/upload_page.html', {'MemeUploadForm': upload_form})
   