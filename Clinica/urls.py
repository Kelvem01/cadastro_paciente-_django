from django.contrib import admin
from django.urls import path

from base.views import inicio , inscrever
from eventos.views import evento

urlpatterns = [
    path('',inicio,name='inicio'),
    path('inscrever-se/',inscrever,name='inscrever'),
    path('eventos/<int:id>/',evento,name='evento'),
    path('admin/', admin.site.urls),
]
