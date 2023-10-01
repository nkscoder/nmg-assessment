from .views import *
from django.urls import path


urlpatterns = [

    path('', home, name='home'),
    path('video/<int:video_id>/', watch_video, name='watch_video'),
    path('video/add_like/<int:video_id>/', add_like, name='add_like'),
    path('<str:session_username>/profile/', profile, name='profile'),
    path('<str:session_username>/dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_video, name='upload'),
    path('edit_video/<int:video_id>', edit_video, name='edit_video'),
    path('delete_video/', delete_video, name='delete_video'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', search, name='search'),
]