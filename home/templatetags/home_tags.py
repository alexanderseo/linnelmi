from django import template
from home.models import Sociallink, Footerblock

register = template.Library()


@register.inclusion_tag('layouts/social_links.html')
def social_links():
    soc_link = Sociallink.objects.all()
    return {'soc_link': soc_link, }


@register.inclusion_tag('layouts/footer_contact_info.html')
def footer_contact_info():
    f_c_info = Footerblock.objects.all()
    return {'f_c_info': f_c_info, }
