from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import TodoList, TodoItem
from .forms import TodoItemForm, TodoListForm


@csrf_exempt
def base(request):
	# POST method to create the title of the ToDoro List:
	if request.method == "POST":
		form_list = TodoListForm(request.POST)
		if form_list.is_valid():
			form_list.save()
			messages.success(request, ('List title successfully created!'))
			return HttpResponseRedirect('/')

	else:
		form_list = TodoListForm()

	# POST method to add items to a ToDoro List:
	if request.method == "POST":
		form_item = TodoItemForm(request.POST)
		if form_item.is_valid():
			form_item.save()
			messages.success(request, ('New list item added!'))
			return HttpResponseRedirect('/')
			
	else:
		form_item = TodoItemForm()

	# grap all TodoLists (titles) from database:
	titles = TodoList.objects.all()

	return render(request, 'home.html', 
		{
		'form_list': form_list, 
		'form_item': form_item,
		'titles': titles
		})


# delete the list:
def delete_list(request, title_id):
	# get the titel of todo list:
	todolist = TodoList.objects.get(id=title_id)
	todolist.delete()
	messages.success(request, ('List has been deleted!'))
	return HttpResponseRedirect('/')


# delete an item of a list:
def delete_item(request, item_id):
	item = TodoItem.objects.get(id=item_id)
	item.delete()
	messages.success(request, ('List item has been deleted!'))
	return HttpResponseRedirect('/')


# edit the title:
@csrf_exempt
def edit_title(request, title_id):
	title = TodoList.objects.get(id=title_id)

	if request.method == "POST":
		form = TodoListForm(request.POST, instance=title)
		if form.is_valid():
			form.save()
			messages.success(request, ('List title successfully edited!'))
			return redirect('/')

	else:
		form = TodoListForm(instance=title)

	return render(request, 'edit_title.html', {'form': form})


# edit the item:
@csrf_exempt
def edit_item(request, item_id):
	item = TodoItem.objects.get(id=item_id)
	
	if request.method == "POST":
		form = TodoItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			messages.success(request, ('List item successfully edited!'))
			return redirect('/')

	else:
		form = TodoItemForm(instance=item)

	return render(request, 'edit_item.html', {'form': form})


def done(request, item_id):
	# search for items which are completed (done):
	done = TodoItem.objects.get(id=item_id)
	done.completed = False
	done.save()
	return HttpResponseRedirect('/')


def incomplete(request, item_id):
	# search for items which are incomplete:
	incomplete = TodoItem.objects.get(id=item_id)
	print(incomplete)
	print('1st bool: ', incomplete.completed)
	incomplete.completed = True
	print('bool: ', incomplete.completed)
	incomplete.save()
	return HttpResponseRedirect('/')




		
