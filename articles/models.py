from django.conf import settings
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):  # ✅ Kept `comment` Field
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments"  # ✅ Added related_name for easier queries
    )
    comment = models.CharField(max_length=140)  # ✅ Kept `comment`
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment  # ✅ Still returns `comment`

    def get_absolute_url(self):
        return reverse("article_list")
