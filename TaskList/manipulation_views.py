from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView, View

from TaskList.forms import TaskEditForm
from TaskList.models import Task


@method_decorator(login_required, name='dispatch')
class TaskCreate(CreateView):
    """Creating a new task"""
    model = Task
    success_url = reverse_lazy('task_list')
    form_class = TaskEditForm

    def get_context_data(self, **kwargs):
        '''
        returns the view data context
        :param kwargs: context variables
        :return: view context
        '''
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch') 
class TaskUpdate(UpdateView):
    """update Task"""
    model = Task
    success_url = reverse_lazy('task_list')
    form_class = TaskEditForm

    def get_context_data(self, **kwargs):
        '''
        returns the view data context
        :param kwargs: context variables
        :return: view context
        '''
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['edit'] = False
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    """delete task"""
    model = Task
    login_required = True
    template_name = "TaskList/task_delete.html"
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        '''
        returns the view data context
        :param kwargs: context variables
        :return: context view
        '''
        context = super(TaskDelete, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['delete_mode'] = True
        return context


@method_decorator(login_required, name='dispatch')
class TaskFinish(View):
    """finishing the task"""
    template_name = "TaskList/task_delete.html"

    def get(self, request, **kwargs):
        task = Task.objects.get(user=self.request.user.pk, pk=kwargs['pk'])
        context = {
            'delete_mode': False,
            'user': self.request.user,
            'object': task
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        task = Task.objects.get(user=self.request.user.pk, pk=kwargs['pk'])
        task.finish()
        task.save()

        return redirect('task_list')
