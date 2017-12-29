"""
Engine views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Mark, Model, Evo
from .forms import PropositionForm


def marks(request):
    """
    Main page with marks
    """
    marklist = Mark.objects.order_by('name')
    error_message = 'seems to be 404'

    context = {
        'marklist': marklist,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/marks.html', context)


def models(request, mark_name_slug):
    """
    Submain page with models
    """
    mark_name = mark_name_slug.replace('_', ' ')
    mark = get_object_or_404(Mark, name=mark_name)
    modellist = mark.model_set.all().order_by('name')
    error_message = 'seems to be empty'

    context = {
        'modellist': modellist,
        'mark_name': mark_name,
        'mark_name_slug': mark_name_slug,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/models.html', context)


def evos(request, mark_name_slug, model_name_slug):
    """
    Subsubmain page with evolutions
    """
    mark_name = mark_name_slug.replace('_', ' ')
    model_name = model_name_slug.replace('_', ' ')
    model = get_object_or_404(Model, name=model_name, mark__name=mark_name)
    evolist = model.evo_set.all().order_by('year')
    error_message = 'seems to be empty'

    context = {
        'evolist': evolist,
        'mark_name': mark_name,
        'mark_name_slug': mark_name_slug,
        'model_name': model_name,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/evos.html', context)


def add(request):
    """
    Supmain page with form
    """
    if request.method == 'POST':
        form = PropositionForm(request.POST)
        if form.is_valid():
            evo = form.save()
            url = '/{}/{}'.format(evo.model.mark.url_name(),
                                  evo.model.url_name())
            return HttpResponseRedirect(url)
    else:
        form = PropositionForm()

    if form['name'].errors:
        form_error = 'Invalid evo name'
        if form['year'].errors:
            form_error += ' and year'
    elif form['year'].errors:
        form_error = 'Invalid year'
    elif form.errors.get('__all__'):
        form_error = form.errors['__all__'][0]
    else:
        form_error = ''

    context = {
        'form': form,
        'form_error': form_error,
    }

    return render(request, 'engine/sections/prop.html', context)
