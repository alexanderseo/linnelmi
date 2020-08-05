from django.shortcuts import render, render_to_response, reverse
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from contact.models import Contact
from contact.forms import ContactForm
from linnelmi import settings


def contact(request):
    contactinfo = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipients = ['']
            recipients.append(sender)
            try:
                send_mail(subject, message, 'alexanderzanin@yandex.ru', recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'contact/sent_mail.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'contactinfo': contactinfo, 'form': form})
