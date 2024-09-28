from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from .views import projects,project,projectCRUD,projectUpdate,projectDelete

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', projects , name= 'projects' ),
    path('project/<int:pk>/', project,name = 'project'),
    path('create/', projectCRUD, name='createproject'),
    path('update/<int:pk>/', projectUpdate,name='updateproject'),
    path('delete/<int:pk>/',projectDelete,name='deleteproject')
   

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
