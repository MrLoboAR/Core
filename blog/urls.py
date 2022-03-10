from django.urls import path
from.views import BlogListView, BlogCreateView

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('new_shitpost/', BlogCreateView.as_view(), name='create'),
]