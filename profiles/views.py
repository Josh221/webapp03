from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class LoginRequired(object):
    """
    Este mixin requerira que el usuario acceda como usuario
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired, self).dispatch(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3

@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])