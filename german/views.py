from django.shortcuts import render, get_object_or_404
from german.models import German, Detailgerman, Document


def germani(request):
    german = German.objects.all()
    det_list_german = Detailgerman.objects.all()
    return render(request, 'german/german.html', {'german': german, 'det_list_german': det_list_german,})


def german(request, slug_usluga=None):
    detailgerman = get_object_or_404(Detailgerman, slug=slug_usluga)
    materialdoc = detailgerman.documents.all()
    return render(request, 'german/german-single.html', {'detailgerman': detailgerman, 'materialdoc': materialdoc,})
