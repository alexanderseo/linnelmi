from django.shortcuts import render, get_object_or_404
from uslugi.models import Uslugi, Detailusluga, Document


def uslugi(request):
    uslugi = Uslugi.objects.all()
    det_list_uslugi = Detailusluga.objects.all()
    return render(request, 'uslugi/uslugi.html', {'uslugi': uslugi, 'det_list_uslugi': det_list_uslugi,})


def usluga(request, slug_usluga=None):
    detailusluga = get_object_or_404(Detailusluga, slug=slug_usluga)
    materialdoc = detailusluga.documents.all()
    return render(request, 'uslugi/single-usluga.html', {'detailusluga': detailusluga, 'materialdoc': materialdoc,})
