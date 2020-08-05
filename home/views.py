from django.shortcuts import render
from home.models import *


def index(request):
    slides = Slider.objects.all()
    adslide = Additionslider.objects.all()
    about = Prepodovatel.objects.all()
    someaboutme = Someaboutme.objects.all()
    counteres = Counterelementy.objects.all()
    resume = Resume.objects.all()
    resumeelement = Resumeelement.objects.all()
    urok = Urok.objects.all()
    itemurok = Itemurok.objects.all()
    myvideo = Myvideo.objects.all()
    textblock = Textblock.objects.all()
    seo = Seohome.objects.first()
    return render(request, 'home/index.html', {'slides': slides,
                                               'adslide': adslide,
                                               'about': about,
                                               'someaboutme': someaboutme,
                                               'counteres': counteres,
                                               'resume': resume,
                                               'resumeelement': resumeelement,
                                               'urok': urok,
                                               'itemurok': itemurok,
                                               'myvideo': myvideo,
                                               'textblock': textblock,
                                               'seo': seo,})
