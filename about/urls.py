from django.urls import path,include
from about import views

urlpatterns=[
    path('',views.add,name='addbook'),
    path('readbook',views.read_book,name='readbook'),
    path('updatebook/<int:id>',views.update_book,name='updatebook'),

]