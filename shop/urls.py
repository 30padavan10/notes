from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^test$', views.test, name='test'),
	url(r'^$', views.LastGoodsListView.as_view(),  name='list_of_last_goods'),
	url(r'^smarts$', views.SmartListView.as_view(), name='smart_list'),
	url(r'^notes$', views.NoteListView.as_view(), name='note_list'),
	url(r'^smart/(?P<pk>\S+)$', views.GoodSmartDetail.as_view(), name='smart-detail'),
        url(r'^note/(?P<pk>\S+)$', views.GoodNoteDetail.as_view(), name='note-detail'),
        url(r'^product/(?P<pk>\S+)$', views.GoodDetail.as_view(), name='product-detail') 
]
