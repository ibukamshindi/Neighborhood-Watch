from django.conf.urls import url,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.register,name ='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$',views.home, name='home'),
    url(r'^hood/(?P<hood_id>[0-9])$', views.hood, name='hood'),
    url(r'profile/',views.profile, name='profile'),
    url(r'^add-business/', views.add_biz, name='add-biz'),
    url(r'^add-post/', views.add_alert, name='add-alert'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)