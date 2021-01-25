from django.urls import path
from django.conf.urls import include, url
from meme_review import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'meme_review'

urlpatterns = [
    path('', views.BioView.as_view(), name='biopage'),
    path('pics/', views.home, name='home'),
    path('pics/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('upload_page/', views.upload, name='upload_page'),
]
