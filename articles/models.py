from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField(null= True, blank = True)
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title