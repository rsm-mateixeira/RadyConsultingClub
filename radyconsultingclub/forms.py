from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'size': '40'})
    )
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': 'Please enter a valid email address.'},
        widget=forms.TextInput(attrs={'size': '40'})
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'size': '40'})
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': '10', 'cols': '40'})
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    use_required_attribute = False


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'linebreak', 'placeholder': 'Subject'}),
            'message': forms.Textarea(
                attrs={'class': 'linebreakTextArea1', 'placeholder': 'Message'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }

        use_required_attribute = False
