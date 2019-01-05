from django.db import models
from django.shortcuts import render, get_object_or_404, redirect


class ObjectDetailMixin:
    model: models.Model = None
    template: str = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template: str = None

    def get(self, request):
        return render(request, self.template, context={'form': self.form_model()})

    def post(self, request):
        bound_form = self.form_model(data=request.POST)

        if bound_form.is_valid():
            valid_form = bound_form.save()
            return redirect(valid_form)

        return render(request, self.template, context={'form': bound_form})
