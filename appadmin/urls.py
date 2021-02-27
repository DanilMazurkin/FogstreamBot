from django.urls import path
from django.contrib.auth import views
from .views import (ViewMain, 
				    ViewMessage,
                    ViewUser,
                    show_edit_form_message)


app_name = "appadmin"

urlpatterns = [
    path('main', ViewMain.as_view(), name='main'),
    path('create/message', ViewMessage.as_view(), name='create_message'),
    
    path('edit/message/<int:id_message>', 
         ViewMessage.as_view(), 
         name='edit_message'),
    
    path('delete/message/<int:id_message>', 
         ViewMessage.as_view(), 
         name='delete_message'),
    
    path('form/edit/message/<int:id_message>',
         show_edit_form_message,
         name="edit_form_message"), 

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('show/users', ViewUser.as_view(), name='show_users')
]