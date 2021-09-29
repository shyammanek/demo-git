from django.shortcuts import render,redirect
from .models import task
from .forms import taskForm

# Create your views here.
def home(request):
	if request.method == 'POST':
		form = taskForm(request.POST or None)
		if form.is_valid():
			form.save()
		return redirect('home')
	else:
		form = taskForm
		tasks = task.objects.all
		context={"tasks":tasks,"form":form}
	
	return render(request,'./home.html',context)

def description(request,pid):
	 task_des=task.objects.get(pk=pid)
	 context={"task_des":task_des}
	 return render(request,'./task_des.html',context)


def taskedit(request,pid):
	if request.method == 'POST':
		task_edit = task.objects.get(pk=pid)
		form = taskForm(request.POST or None, instance = task_edit)
		if form.is_valid():
			form.save()
		return redirect('home')
	else:
		task_ed = task.objects.get(pk=pid)
		return render(request, './edit.html', {'task_ed': task_ed})

def taskdelete(request,pid):
	task_del = task.objects.get(pk=pid)
	task_del.delete()
	return redirect('home')