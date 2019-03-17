from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:title>', views.detail, name='detail'),
    #path('<slug:title>', views.detail, name='detail')
]