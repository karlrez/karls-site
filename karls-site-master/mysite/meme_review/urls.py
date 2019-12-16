from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'meme_review'

urlpatterns = [
    path('memes/', views.home, name='home'),
    path('', views.BioView.as_view(), name='biopage'),
    path('upload_page/', views.upload, name='upload_page'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
