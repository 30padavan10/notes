from django.shortcuts import render
from django.views import generic 
# Create your views here.
from .models import Good, Producer, Comment, Smartphone, Notebook

def test(request):
	test = 'test'
	return render(request, 'shop/test.html', {'name':test})


class LastGoodsListView(generic.ListView):
	model = Good
	context_object_name = 'last_goods_list'
	queryset = Good.objects.all()[:5]
	template_name = 'shop/list_of_last_goods.html'

class SmartListView(generic.ListView):
        model = Smartphone
        context_object_name = 'CategorySmartListView'
        queryset = Smartphone.objects.all().order_by('price')  #  Для фильтра по полю из связанных моделей, используйте имена связывающих полей разделенных двойным нижним подчеркиванием, пока вы не достигните нужного поля.
        template_name = 'shop/CategorySmartListView.html'


class NoteListView(generic.ListView):
        model = Notebook
        context_object_name = 'CategoryNoteListView'
        queryset = Notebook.objects.all().order_by('price')
        template_name = 'shop/CategoryNoteListView.html'


class GoodSmartDetail(generic.DetailView):
	model = Smartphone
	# не забывать что если не указан template, то надо создавать по умолчанию с названием model_detail.html


class GoodNoteDetail(generic.DetailView):
        model = Notebook
