from django.urls import path
from . import views

#set the NAMESPACE
app_name = 'meme_review'

urlpatterns = [
path('', views.PostListView.as_view(), name='home'),
]
