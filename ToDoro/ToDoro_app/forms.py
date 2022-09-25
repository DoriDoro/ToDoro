from django import forms  
from .models import TodoItem, TodoList


class TodoItemForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = '__all__'


class TodoListForm(forms.ModelForm):
	class Meta:
		model = TodoList
		fields = ('title',)

		