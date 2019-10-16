from django.conf.urls import include, url
from . import views
#from django.urls import path
#from . import views

#app_name= 'blog'
urlpatterns = [
    url(r'^$', views.post_list),
    #path('', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
