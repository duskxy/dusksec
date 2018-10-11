from django.urls import path
from src import views

urlpatterns = [
    path('src/<gs>/',views.index.as_view(),name='src'), 



]

app_name = "src"
