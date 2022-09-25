from django.db import models


class TodoList(models.Model):
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title


class TodoItem(models.Model):
	item = models.CharField(max_length=200)
	todolist = models.ForeignKey('TodoList', on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item 


