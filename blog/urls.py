from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

app_name="blog"

urlpatterns = [
    # puede colocarse inicio/ en la primera para seguir la ruta
    path('', BlogListView.as_view(), name="Home"),
    path('create/', BlogCreateView.as_view(), name="Create"),
    path('<int:pk>', BlogDetailView.as_view(), name="Detail"),
     
]