from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        cleaned_slug = self.cleaned_data['slug'].lower()

        if cleaned_slug == 'create':
            raise ValidationError('slug can not be "Create"')
        if not self.instance.id and bool(Tag.objects.filter(slug__iexact=cleaned_slug).count()):
            raise ValidationError(f'slug must be unique: slug "{cleaned_slug}" already exist')

        return cleaned_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        cleaned_slug = self.cleaned_data['slug'].lower()

        if cleaned_slug == 'create':
            raise ValidationError('slug can not be "Create"')

        return cleaned_slug
