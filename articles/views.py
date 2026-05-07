from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"
    ordering = ["-date"]

    def get_queryset(self):
        return Article.objects.prefetch_related("comments").select_related("author")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user
            comment.save()

        return redirect(self.object.get_absolute_url())


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article_edit.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author