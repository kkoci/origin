from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, View

from TaskList.auth_forms import RegisterUserForm, LoginForm


class LoginView(FormView):
    """
    This class is responsible for operating the user login view
    """
    template_name = "TaskList/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("task_list")

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['user'] = None
        context['active'] = "home"
        return context

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
        else:
            form.add_error(None, _("Invalid username or password provided."))
            return self.form_invalid(form)


class RegisterView(FormView):
    template_name = "TaskList/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context_data = super(RegisterView, self).get_context_data(**kwargs)
        context_data['user'] = None
        return context_data
    
    def form_valid(self, form):
        form_data = form.clean()
        
        # Check if there is such a user. If it does not exist, create it.
        user, created = User.objects.get_or_create(username=form_data['username'])
        if created:
            user.set_password(form_data['password'])
            user.save()
            return super(RegisterView, self).form_valid(form)
        else:
            form.add_error('username', _('A user with this name already exists'))
            return super(RegisterView, self).form_invalid(form)
            

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
