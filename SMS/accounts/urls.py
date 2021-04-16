from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name="logout"),
    url(r'^signup/$',views.SignUpView,name="signup"), 
    url(r'^signup/admin/$',views.AdminCreateView.as_view(),name='create_admin'),
    url(r'^signup/manager/$',views.ManagerCreateView.as_view(),name='create_manager'),
]