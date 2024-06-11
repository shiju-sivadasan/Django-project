from django.shortcuts import render,redirect
from .models import Biography
# Create your views here.
def create_biography(request):
    bio=Biography()
    if request.POST:
        bio.name=request.POST.get('username')
        bio.img=request.FILES.get('img')
        bio.date_of_birth=request.POST.get('dob')
        bio.gender=request.POST.get('gender')
        bio.marital_status=request.POST.get('marital_status')
        bio.nationality=request.POST.get('nationality')
        bio.skills=request.POST.get('skills')
        bio.address=request.POST.get('address')
        bio.email=request.POST.get('email')
        bio.phone=request.POST.get('phone')
        bio.linkedin=request.POST.get('linkedin')
        bio.save()
        return redirect('det/create_details')
    return render(request,'bio/create_bio.html')
