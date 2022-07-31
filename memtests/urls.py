from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='memtests-index'),
	path('matching/', views.matchingTest, name='memtests-matching'), #fixme
]
