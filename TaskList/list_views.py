from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from TaskList.models import Task


@method_decorator(login_required, name='dispatch') #
class TaskList(ListView):
    '''
    Task list
    '''
    allow_empty = True

    def get_queryset(self):
        '''
        returns a list of tasks for the user
        :return: task list for the current user
        '''
        return Task.objects.filter(user=self.request.user.pk)

    def get_context_data(self, **kwargs):
        '''
        returns the view data context
        :param kwargs: context variables
        :return: context view
        '''
        context = super(TaskList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['active'] = 'tasks'
        return context


@method_decorator(login_required, 'dispatch') #
class TaskListFilteredByFlagDone(ListView):
    '''Tasks filtered by flags'''
    done = True
    allow_empty = True
    template_name = "TaskList/task_list_filt.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.pk, done=self.done)

    def get_context_data(self, **kwargs):
        '''
        returns the view data context
        :param kwargs: context variables
        :return: context view
        '''
        context = super(TaskListFilteredByFlagDone, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, 'dispatch')
class TaskDetailsView(DetailView):
    template_name = "TaskList/task_details.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskDetailsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
