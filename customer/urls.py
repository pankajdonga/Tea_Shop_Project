from django.contrib import admin
from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# ********
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
# ********

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('',views.index,name='customerIndex'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu, name='customermenu'),
    path('cart/',views.cart,name='cart'),
    path('userlogout/',views.userlogout),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('updateprofile/',views.updateProfile),
    path('revieworder/',views.revieworder,name='revieworder'),
    path('ordertracking/<int:order_id>',views.ordertracking,name='ordertracking'),
    path('vieworder/',views.vieworder),
    path('otpverify/',views.otpverify,name='otpverify'),

    # Password reset url
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='customer/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='customer/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='customer/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='customer/password_reset_complete.html'),name='password_reset_complete'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)