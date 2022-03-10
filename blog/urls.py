from django.urls import path
from.views import BlogListView, BlogCreateView, BlogDetailedView, UpdateShitpost, DeleteShitpost

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('new_shitpost/', BlogCreateView.as_view(), name='create'),
    path('shitpost_<int:pk>/', BlogDetailedView.as_view(), name='shitpost'),
    path('dumb_edit_<int:pk>/update/', UpdateShitpost.as_view(), name='update'),
    path('dump_shit_<int:pk>/deleting/', DeleteShitpost.as_view(), name='dump'),
]