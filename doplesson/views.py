from django.shortcuts import render, get_object_or_404
from doplesson.models import Doplesson, Detailesson, Document


def doplesson_list(request):
    doplessons = Doplesson.objects.all()
    det_list_doplesson = Detailesson.objects.all()
    return render(request, 'doplesson/doplessons.html', {'doplessons': doplessons,
                                                         'det_list_doplesson': det_list_doplesson,})


def doplesson_single(request, slug_doplesson=None):
    single_lesson = get_object_or_404(Detailesson, slug=slug_doplesson)
    doc_for_lesson = single_lesson.documents.all()
    return render(request, 'doplesson/doplesson-single.html', {'single_lesson': single_lesson,
                                                               'doc_for_lesson': doc_for_lesson,})
