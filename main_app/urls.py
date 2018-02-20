from django.conf.urls import url
from .signuptestview import SignupView

urlpatterns = [
	url(r'^signup/$', SignupView.as_view(), name='signup'),
]