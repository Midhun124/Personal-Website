from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm
from django.views.decorators.csrf import csrf_exempt


def home(request):
  return render(request , 'personal.html')

@csrf_exempt
def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    # Save form data to database
    form = ContactForm(name=name, email=email, subject=subject, message=message)
    form.save()
    return HttpResponse('Your message has been received. Thank you!')
  else:
    return HttpResponse('Invalid request.')