"""
Engine views
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Mark, Model, Evo
from .forms import EvoForm


class MarkListView(ListView):
    """
    Main page with marks
    """
    context_object_name = 'mark_list'
    queryset = Mark.objects.order_by('name')


class ModelListView(ListView):
    """
    Submain page with models
    """
    context_object_name = 'model_list'

    def get_queryset(self):
        self.mark = get_object_or_404(Mark, slug=self.kwargs['mark_slug'])
        return self.mark.model_set.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mark_name'] = self.mark.name
        context['mark_slug'] = self.mark.slug
        return context


class EvoListView(ListView):
    """
    Subsubmain page with evolutions
    """
    context_object_name = 'evo_list'

    def get_queryset(self):
        self.model = get_object_or_404(Model, slug=self.kwargs['model_slug'],
                                       mark__slug=self.kwargs['mark_slug'])
        return self.model.evo_set.all().order_by('year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.name
        context['mark_name'] = self.model.mark.name
        context['mark_slug'] = self.model.mark.slug
        return context


class EvoCreateView(CreateView):
    """
    Submain page with form
    """
    model = Evo
    form_class = EvoForm
    form_error = None

    def form_invalid(self, form):
        if form['name'].errors:
            self.form_error = 'Invalid evo name'
            if form['year'].errors:
                self.form_error += ' and year'
        elif form['year'].errors:
            self.form_error = 'Invalid year'
        elif form.errors.get('__all__'):
            self.form_error = form.errors['__all__'][0]
        return super().form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form_error'] = self.form_error
        return context
