from django.conf.urls import url

from webInterface import settings
from . import views
from django.conf.urls.static import static
from django.urls import path

app_name = 'webInterface'
urlpatterns = [
    url(r'^$', views.simple_upload, name='upload_file'),
    url(r'show_upload_files', views.show_upload_files, name='show_upload_files'),
    path(r'get_file_content/(?P<id>\d+)/$', views.get_file_content, name='get_file_content'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)