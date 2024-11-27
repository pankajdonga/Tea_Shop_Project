from django.contrib import admin
from django.urls import path
from manager import views
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
    path('',views.shoplogin),
    path('m_index/',views.index,name='index'),
    path('m_menu/',views.menu,name='menu'),
    path('m_order/',views.order,name='order'),
    path('m_signup/',views.signup),
    path('m_addproduct/',views.addproduct),
    path('m_deleteproduct/<int:id>',views.deleteproduct),
    path('m_updatedata/<int:id>',views.updatedata),
    path('m_shoplogout/',views.shoplogout),
    path('m_cinfirmOrder/<int:id>',views.confirmOrder), 
    path('m_staffattendance/',views.staffattendance),
    path('m_viewattendance/',views.viewattendance),
    path('m_addstaff/',views.addstaff,name='addstaff'),
    path('m_deliveryStatus/<int:id>',views.deliveryStatus),

     # Password reset url
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='manager/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='manager/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='manager/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='manager/password_reset_complete.html'),name='password_reset_complete'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)