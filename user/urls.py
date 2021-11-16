from django.urls import path
from user.views import (
	create_user_view,
    detail_user_view,
    all_user_view,
    editform_user_view
)

app_name = 'user'

urlpatterns = [
    path('create', create_user_view, name="create"),
    path('all', all_user_view, name="all"),
    path('detail/', detail_user_view, name="detail"),
    path('editform/', editform_user_view, name="editform"),

    
 ]
