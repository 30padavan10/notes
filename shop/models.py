from django.db import models
import uuid
from datetime import datetime
from django.urls import reverse
# Create your models here.


class Good(models.Model):
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  Это хорошая альтернатива AutoField для primary key, т.к. база данных не генерирует UUID, хотя наличие uuid рекомендуется. AutoField создается автоматически для каждой модели, если ни одно из полей модели не указывает явно primary key.
	producer = models.ForeignKey('Producer', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	dev = (('Смартфон','Смартфон'), ('Ноутбук','Ноутбук'))
	category = models.CharField(max_length=15, choices=dev, default='Смартфон', blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField(max_length=1000)
	image = models.ImageField(null=True, blank=True, upload_to='images', help_text='150x150px', verbose_name='Ссылка картинки')  
	comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
	sale = models.BooleanField()
	pub_date = models.DateTimeField(null=True, blank=True)


	class Meta:
		ordering = ['-pub_date']
	
	def __str__(self):
		return self.name


class Producer(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Smartphone(Good):
	year = models.IntegerField()
	version_os = models.CharField(max_length=50)
	num_core = models.IntegerField()
	frequency_cpu = models.CharField(max_length=50)
	memory =  models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('smart-detail', args=[str(self.id)])


class Notebook(Good):
	version_os = models.CharField(max_length=50)
	display = models.CharField(max_length=50)
	CPU = models.CharField(max_length=50)
	memory = models.CharField(max_length=50)
	GPU = models.CharField(max_length=50)
	HDD = models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('note-detail', args=[str(self.id)])

class Comment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.title







