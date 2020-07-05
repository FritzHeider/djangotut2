from django.urls import path

from . import views
# stuff
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    
]
