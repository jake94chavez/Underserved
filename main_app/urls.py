from django.conf.urls import url
from . import views
from .views import about

# from views import about
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', about),

]
