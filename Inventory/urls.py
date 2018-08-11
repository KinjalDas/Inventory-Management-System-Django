from django.urls import path

from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('<int:item_id>/',views.details,name='details'),
	path('<int:item_id>/transfer',views.transferitm,name='transferitm'),
	path('<int:item_id>/return',views.returnitm,name='returnitm'),
]
