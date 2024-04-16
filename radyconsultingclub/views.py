from django.shortcuts import render, redirect
from django.contrib import messages
from radyconsultingclub.models import Contact
from .forms import ContactForm

# Create your views here.

def home_page_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            Contact.objects.create(**contact_form.cleaned_data)
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to the same page using a GET request
            return redirect('radyconsultingclub:home_page_view')  # Replace 'home_page_view' with the name of your URL pattern

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'radyconsultingclub/home.html', context)