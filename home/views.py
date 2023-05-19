from django.shortcuts import render,get_object_or_404, redirect
from .models import Volunteer, donor, contact, team, program, Resource, testimony, OngoingEvent, PastEvent, FutureEvent
from django.contrib import messages


# Create your views here.


from .models import OngoingEvent

def search(request):
    query = request.GET.get('q')
    results = OngoingEvent.objects.filter(name__icontains=query)
    return render(request, 'index.html', {'results': results})

def index(request):
    testimon=testimony.objects.all()
    testimonies={'testimonies': testimon}

    current=OngoingEvent.objects.all().order_by('-id')[:3][::-1]
    currentev={'currentev':current}
    
    future=FutureEvent.objects.all().order_by('-id')[:3][::-1]
    futurev={'futurev':future}

    past= PastEvent.objects.all().order_by('-id')[:3][::-1]
    Pastev= {'pastev':past}

    context= {
        'currentev': currentev,
        'pastev':Pastev,
        'testimonies': testimonies,
        'futurev':futurev
    }
    return render (request, 'index.html', context)
def volunteer(request):
    if request.method == 'POST':
        form_name = request.POST['form_name']
        form_gender = request.POST['form_subject']
        form_email = request.POST['form_email']
        form_hear_about_us = request.POST['form_subject']
        form_message = request.POST['form_message']
        form_cv = request.FILES.get('cv', None)

        volunteer = Volunteer(
            name=form_name,
            gender=form_gender,
            email=form_email,
            hear_about_us=form_hear_about_us,
            message=form_message,
            cv=form_cv
        )
        volunteer.save()
        return messages.info(request, 'You have successfully applied!')
    else:
        messages.info(request, 'you have enterred invalid credentials' )

    return render(request, 'volunteer.html')
def donate(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('femail')
        contact = request.POST.get('fcontact')
        payment_method = request.POST.get('form_subject')
        donors = donor(name=name, email=email, contact=contact, payment_method=payment_method)
        donors.save()
        # Process the donation using the payment method and amount
        # ...
        return render(request, 'donate.html')

    return render(request, 'donate.html')
def contact(request):
    if request.method == 'POST':
        name= request.POST['form_name']
        email=request.POST['form_email']
        phone=request.POST['form_phone']
        message= request.POST['form_message']

        contact_info=contact(name=name, email=email, phone=phone, message=message)
        contact_info.save()

    return render(request, 'contact.html')
def team_list(request):
    details=team.objects.all()
    members={'members':details}
    return render(request, 'team.html', members)

def events_list(request):
    details=program.objects.all()
    occations={'occasions':details}
    return render(request, 'events.html', occations)
def program_details(request, pk):
    prog = get_object_or_404(program, pk=pk)
    return render(request, 'program-details.html', {'occasion': prog})

def about(request):
    return render( request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def resources(request):
    resourcess = Resource.objects.all()
    resources= {'resources': resourcess}
    return render(request, 'resources.html', resources)

def faq(request):
    return render(request, 'faq.html')