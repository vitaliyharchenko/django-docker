# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField(help_text='[!embed] для встраивания видео. [!readmore] для окончания shortcut-контента')
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={'post_id': self.pk})

    @property
    def full_content(self):
        list = self.body.split('[!readmore]')
        try:
            full = list[0] + list[1]
        except IndexError:
            full = self.body
        return full

    @property
    def short_content(self):
        return self.body.split('[!readmore]')[0]
