from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header  =  "AJU's Shelf Administration"  
admin.site.site_title  =  "AJU Admin Site"
admin.site.index_title  =  "AJU's Shelf"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
