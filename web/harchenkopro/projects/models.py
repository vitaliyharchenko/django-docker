from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    description = models.CharField(max_length=600, verbose_name='Описание', blank=True)
    link = models.CharField(max_length=600, blank=True, verbose_name='Ссылка')
    logo = models.ImageField(upload_to='projects/logo', verbose_name='Логотип', blank=True, null=True)
    views = models.IntegerField(default=0)

    class Meta():
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        app_label = 'projects'
        ordering = ['-views']

    def get_absolute_url(self):
        return "/project/%i" % self.id

    def __str__(self):
        return self.title