from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='my-home'),
    path('about', views.about, name='my-about'),
    path('blog', views.blog, name='my-blog'),
    path('products', views.post_job, name='my-post'),
    path('cart', views.want_job, name='my-cart'),
    path('contact', views.contact, name='my-contact'),
    path('category', views.user_signup, name='my-category'),
    path('login', views.user_login, name='my-login'),
    path('logout', views.user_logout, name='my-logout'),
    path('checkout', views.checkout, name='my-checkout'),
]

