from django.urls import path
from . import views
app_name='blog'
urlpatterns=[

    path('',views.BlogPostListView.as_view(),name='home'),

    #/post/1/
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),

    #/post/new/
    path('post/new/',views.PostCreateView.as_view(),name='post_new'),

    #/post/1/edit/
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),

    #/post/1/delete/
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
]
