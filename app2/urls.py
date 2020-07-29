from django.urls import path
from app2 import views
app_name="app2"


urlpatterns =[
    path('child/',views.child,name="child"),
    path('home/',views.home,name='home'),
]