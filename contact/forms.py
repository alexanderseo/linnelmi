from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'id': 'name',
                                                            'name': 'name',
                                                            'input_type': 'text',
                                                            'placeholder': 'Ваше имя', }))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email',
                                                              'name': 'name',
                                                              'type': 'text',
                                                              'placeholder': 'Email', }))
    message = forms.CharField(widget=forms.Textarea(attrs={'id': 'comments',
                                                            'cols': '40',
                                                            'name': 'comments',
                                                            'rows': '3',
                                                            'placeholder': 'Сообщение', }))
