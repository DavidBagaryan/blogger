from django.db import models
from django.shortcuts import render, get_object_or_404


class ObjectDetailMixin:
    model: models.Model = None
    template: str = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
