from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),       # pk가 int로 넘어옴
    #re_path(r'(?P<pk>\d+)$', views.post_detail),   < 위와 동일함 (pk가 문자열로 넘어옴)
    #path('archives/<int:year>/', views.archives_year),
    re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
]