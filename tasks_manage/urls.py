from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'add/$', TaskCreate.as_view(), name='Task-add'),
    url(r'(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='Task-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', TaskDelete.as_view(), name='Task-delete'),
    url(r'taskList/$', TaskList.as_view(), name='Task-list'),
]