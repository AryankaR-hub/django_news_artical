from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib import messages

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # Optional: add a success message when user signs up
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "🎉 Account created successfully! You can now log in."
        )
        return response

    # Optional: add a friendly message if form is invalid
    def form_invalid(self, form):
        messages.error(
            self.request,
            "❌ Please fix the errors below and try again."
        )
        return super().form_invalid(form)
