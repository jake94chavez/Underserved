from django.conf.urls import url
from . import views
from .views import about
from .views import results
from .views import profile
from .views import login
from .views import SignupView


urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', about),
    url(r'^results/$', results),
    url(r'^profile/$', profile),
    url(r'^login/$', login),
    url(r'^signup/$', SignupView.as_view(), name='signup'),

]
