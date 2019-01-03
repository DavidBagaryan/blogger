from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

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
        if Tag.objects.filter(slug__iexact=cleaned_slug).count():
            raise ValidationError(f'slug must be unique: slug "{cleaned_slug}" already exist')

        return cleaned_slug

    # def save(self) -> Tag:
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
    #     return new_tag
