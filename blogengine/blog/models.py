from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(string) -> str:
    new_slug = slugify(string, allow_unicode=True)
    suffix = datetime.now().strftime('_%y-%m-%d_%H:%M')
    return f'{new_slug}{suffix}'


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)

        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_posts', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'
