from django.shortcuts import render
from materials.models import Materials, Document


def materials_list(request):
    material = Materials.objects.all()
    materialdoc = Document.objects.all()
    return render(request, 'materials/materials.html', {'material': material, 'materialdoc': materialdoc, })
