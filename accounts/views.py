from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # This tells base.html to use the auth layout
        context["is_auth_page"] = True 
        return context
    
    

    # Optional: add a friendly message if form is invalid
    def form_invalid(self, form):
        messages.error(
            self.request,
            "❌ Please fix the errors below and try again."
        )
        return super().form_invalid(form)
