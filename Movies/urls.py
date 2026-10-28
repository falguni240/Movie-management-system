from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_mov,name='create_mov'),
    path('read_mov',views.read_mov,name='read_mov'),
    path('update_mov/<int:mid>',views.update_mov,name='update_mov'),
    path('delete_mov/<int:mid>',views.delete_mov,name='delete_mov'),
    
    # usermadel
    path('create_user',views.create_user, name='create_u'),
    path('read_user',views.read_user, name='read_u'),
    path('update_user/<int:uid>',views.update_user, name='update_u'),
    path('delete_user/<int:uid>',views.delete_user, name='delete_u'),
    
    # booking
    path('add_booking',views.add_booking, name='add_book'),
    path('read_booking',views.read_booking, name='read_book'),
    path('update_booking/<int:bid>',views.update_booking, name='update_book'),
    path('delete_booking/<int:bid>',views.delete_booking, name='delete_book')
    
]