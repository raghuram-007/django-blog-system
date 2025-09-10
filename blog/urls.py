from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('intro', views.intro, name='intro'),
    path('password', views.value, name='value'),
    path("id/<int:id>", views.id, name='id'),
    path("user/<str:user>", views.user, name='user'),
    path("hello", views.home, name='home'),
    path("login", views.login, name="login"),
    path("sign", views.signup, name="sign"),
    path('post', views.post, name='post'),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('detail/<str:slug>', views.detail, name='detail'),
    path('logout', views.logout, name='logout'),
    path('new_post', views.new_post, name='new_post'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('publish_post/<int:post_id>/', views.publish_post, name='publish_post'),

    # Password Reset Flow URLs
    path('forget', views.forget_password, name='forget'),  # Your custom view for requesting reset
    path('reset/<uidb64>/<token>/', views.reset_password, name='reset_password'),  # Your custom view for requesting reset

   
]
