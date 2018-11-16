from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from TaskList import timedelta


class Task(models.Model):
    """
    A class describing the tasks to be carried out along with a description
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4000)
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    done = models.BooleanField(default=False)

    def __unicode__(self):
    #def __str__(self):
        return unicode(self).encode('utf-8')
        '''Tiny method for unicode names'''
        #return self.name.encode('utf-8')

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})

    def clean(self):
        '''
        method that validates the model
        :return:
        '''
        if self.start > self.end:
            #Start date is later than end date.
            raise ValidationError(_("The end date is earlier than the start date"))

    def finish(self):
        self.done = True
        self.end = datetime.now(timezone.utc)

    def calculate_task_time(self):
        return self.end - self.start

    def calculate_real_task_time(self):
        real_task_time = datetime.now(timezone.utc) - self.start

        if not self.done:
            return real_task_time

        return self.calculate_task_time()

    def get_localized_task_time(self):
        return timedelta.localize(self.calculate_task_time())

    def get_localized_real_task_time(self):
        return timedelta.localize(self.calculate_real_task_time())