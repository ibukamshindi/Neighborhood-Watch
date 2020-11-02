from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.register,name = 'register'),
    url(r'^home/$',views.home, name='home')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)