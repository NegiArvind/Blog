from django.urls import path
from . import views
app_name='blog'
urlpatterns=[

    path('',views.BlogPostListView.as_view(),name='home'),

    #/post/1/
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
]
