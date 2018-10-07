from django.urls import path
from src import views

urlpatterns = [
    path('src/',views.index.as_view(),name='src'), 



]

app_name = "src"
