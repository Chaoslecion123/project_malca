from django.contrib import admin
from django.urls import path
from core.views import (register,course,model_form_upload,CreateViewInterfaz,
    login_view,logout_view,course_detail)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
    path('cursos/',course,name='cursos'),
    path('interfaz/<int:pk>/',CreateViewInterfaz.as_view(),name='interface'),
    path('upload/',model_form_upload,name='documento'),
    path('curso/detalle/<int:pk>/',course_detail,name='curso-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
