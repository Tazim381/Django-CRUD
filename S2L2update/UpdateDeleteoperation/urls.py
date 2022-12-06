from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name="home"),

    path('home',views.home, name="home"),
    path('addnew',views.addnew, name="addnew"),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/<str:id>',views.update, name='update'),
    path('update/updaterecord/<str:id>', views.updaterecord, name='updaterecord'),
    
    
]