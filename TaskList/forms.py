from django import forms
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget

from TaskList.models import Task


class TaskEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)

    class Meta:
        DateTimeOptions = {
            'language': 'en',
            'showMeridian': 'true'
        }

        model = Task
        fields = ['name', 'description', 'start', 'end']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'start': _('Start'),
            'end': _('End'),
            'done': _('Done')
        }
        help_texts = {
            'name': _('Name of the task'),
            'description': _('Description of the task'),
            'start': _('Date in which the task should start'),
            'end': _('Date in which the task should end'),
            'done': _('Done')
        }
        error_messages = {
            'name': {
                'max_length': _("The task name is too long."),
            },
            'description': {
                'max_length': _("The task description is too long."),
            },
        }
        widgets = {
            'start': DateTimeWidget(options=DateTimeOptions, usel10n=True, bootstrap_version=3),
            'end': DateTimeWidget(options=DateTimeOptions, usel10n=True, bootstrap_version=3)
        }
