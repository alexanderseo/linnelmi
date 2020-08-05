# from django import template
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.mail import send_mail, BadHeaderError
#
# register = template.Library()
#
# @register.inclusion_tag('contact/contact.html')
# def contactView(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             sender = form.cleaned_data['sender']
#             message = form.cleaned_data['message']
#             copy = form.cleaned_data['copy']
#             recipients = ['alexanderzanin@yandex.ru']
#             if copy:
#                 recipients.append(sender)
#             try:
#                 send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found')
#             return render(request, 'contact/contact.html')
#     else:
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})