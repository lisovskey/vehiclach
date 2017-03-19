from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Mark, Model, Evo

def index(request):
    '''
    Main page with marks
    '''
    marklist = Mark.objects.order_by('name')
    error_message = 'seems to be 404'

    context = {
        'marklist': marklist,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/marks.html', context)

def sub_index(request, mark_name):
    '''
    Submain page with models
    '''
    mark = get_object_or_404(Mark, name=mark_name)
    modellist = Model.objects.filter(mark__name=mark_name).order_by('name')
    error_message = 'seems to be empty'

    context = {
        'modellist': modellist,
        'mark_name': mark_name,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/models.html', context)

def sub_sub_index(request, mark_name, model_name):
    '''
    Subsubmain page with evolutions
    '''
    model = get_object_or_404(Model, name=model_name)
    evolist = Evo.objects.filter(model__name=model_name).order_by('year')
    error_message = 'seems to be empty'

    context = {
        'evolist': evolist,
        'mark_name': mark_name,
        'model_name': model_name,
        'error_message': error_message,
    }

    return render(request, 'engine/sections/evos.html', context)
