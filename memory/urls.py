from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^hello$', views.hello, name='hello'),
	url(r'^hello/list$', views.hello_model_list, name='hello_model_list'),
	url(r'^hello/detail/(?P<pk>\d+)/$', views.hello_model_detail, name='hello_model_detail')
]

