from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='memtests-index'),
	path('test/', views.test, name='memtests-test'), #fixme
]
