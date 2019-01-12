from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class ObjectDetailMixin:
    model: models.Model = None
    template: str = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj, 'obj': obj, 'detail': True})


class BaseCUDMixin(LoginRequiredMixin):
    raise_exception = True

    action = None
    model: models.Model = None
    form_model = None
    template: str = 'blog/crud_template.html'

    @property
    def get_model_name_lower(self) -> str:
        return self.model.__name__.lower()


class ObjectCreateMixin(BaseCUDMixin):
    action = 'create'

    @property
    def get_form_action(self) -> str:
        return f'{self.action}_{self.model.__name__.lower()}'

    def get(self, request, prev_instance=None):
        return render(request, self.template, context={
            'form': self.form_model() if not prev_instance else prev_instance,
            'action': self.action,
            'form_action': reverse(self.get_form_action),
            'obj_name': self.get_model_name_lower
        })

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            valid_form = bound_form.save()
            return redirect(valid_form)

        return self.get(request, bound_form)


class ObjectUpdateMixin(BaseCUDMixin):
    action = 'update'

    def get_renderer(self, request, bound_form, obj):
        return render(request, self.template, context={
            'form': bound_form,
            'action': self.action,
            'form_action': obj.get_update_url(),
            'obj_name': self.get_model_name_lower,
        })

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return self.get_renderer(request, bound_form, obj)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            valid_form = bound_form.save()
            return redirect(valid_form)

        return self.get_renderer(request, bound_form, obj)


class ObjectDeleteMixin(BaseCUDMixin):
    action = 'delete'

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={
            'obj': obj,
            'action': self.action,
            'form_action': obj.get_delete_url(),
            'obj_name': self.get_model_name_lower,
        })

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.get_list_page))

    @property
    def get_list_page(self) -> str:
        return f'{self.model.__name__.lower()}s_list'
