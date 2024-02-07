from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('posts/', PostsList.as_view(), name='posts'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('posts/create/', PostCreate.as_view(), name='post_create'),
   path('posts/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   #path('pages/', include('django.contrib.flatpages.urls')),
 ]