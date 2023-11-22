
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

from django.http import HttpResponseRedirect


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")  # Especifica la URL a la que deseas redirigir

    def form_valid(self, form):
        response = super().form_valid(form)
        # Después de un registro exitoso, redirige manualmente a la URL especificada
        return HttpResponseRedirect(self.success_url)
