from django.urls import path
from . import views
urlpatterns = [
    path('predictor', views.predictor,name='carpricepredictor'),
    path('back',views.back),
]