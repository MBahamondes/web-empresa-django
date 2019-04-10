from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    contactForm = ContactForm()

    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['mbahamondes.osorio@gmail.com'],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")



    return render(request, 'contact/contact.html', { 'form': contactForm })
