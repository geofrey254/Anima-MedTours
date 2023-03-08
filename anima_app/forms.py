from django import forms
from django.forms import ModelForm, Textarea, FileInput, DateTimeField, TextInput
from django.conf import settings
from django.core.mail import send_mail


# contact/forms.py
class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone = forms.CharField(max_length=120)
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    name.widget.attrs.update({'class': 'app-form-control','placeholder':'NAME'})
    email.widget.attrs.update({'class': 'app-form-control','placeholder':'EMAIL'})
    phone.widget.attrs.update({'class': 'app-form-control','placeholder':'CONTACT NO'})
    subject.widget.attrs.update({'class': 'app-form-control','placeholder':'SUBJECT'})
    message.widget.attrs.update({'class': 'app-form-control','placeholder':'MESSAGE'})



    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} '
        msg += f'\n\nSubject:'
        msg += f'\n{subject}\n\n'
        msg += f'Message:\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )