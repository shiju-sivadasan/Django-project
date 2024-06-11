from django.shortcuts import render,redirect
from django.urls import reverse
from biography.models import Biography
from .models import Details
# Create your views here.
def create_details(request):
    bios=Biography.objects.all()
    details=Details()
    if request.POST:
        details.about=request.POST.get('about')
        details.projects=request.POST.get('projects')
        details.experience=request.POST.get('experience')
        details.education=request.POST.get('education')
        details.certifications=request.POST.get('certifications')
        details.save()
        return redirect("/proj/create_proj_details")
    return render(request,'details/create_details.html',{'bios':bios})