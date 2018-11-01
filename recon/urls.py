from django.conf.urls import url
from django.contrib.auth.views import login,logout_then_login
from django.contrib.auth.forms import AuthenticationForm
from . import views


urlpatterns = [
    #url(r'^$',views.login,name="login"),
    #url(r'^$',login,{'template_name':'login.html'},name="login",kwargs=dict(authentication_form=AuthenticationForm)),
    url(r'^$',login,name="login",kwargs=dict(authentication_form=AuthenticationForm,template_name="login.html")),
    url(r'^recon/$',views.index,name="index"),
    url(r'^logout/$',logout_then_login,name="logout"),
    url(r'^domain/$',views.domain,name='domain'),
    url(r'^dnslog/$',views.dnslog,name='dnslog'),



]

app_name = "recon"
