from django.db import models

# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=200, help_text='title')
	body = models.TextField(max_length=20000, help_text='description')
	pub_date = models.DateField()
	
	class Meta:
		ordering = ['pub_date']

	def __str__(self):
		return '{}'.format(self.title) 
