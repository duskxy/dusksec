from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login,name="login"),
    url(r'^recon/$',views.index,name="index"),
    url(r'^domain/$',views.domain,name='domain'),
    url(r'^dork/$',views.dork,name='dork'),



]

app_name = "recon"
