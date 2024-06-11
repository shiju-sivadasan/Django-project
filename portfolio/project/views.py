from django.shortcuts import render,redirect
from biography.models import Biography
from details.models import Details
from .models import Project
# Create your views here.
def create_project_details(request):
    bios=Biography.objects.all()
    details=Details.objects.all()
    project=Project()
    if request.POST:
        project.title=request.POST.get('title')
        project.project_img=request.FILES.get('img')
        project.description=request.POST.get('project_details')
        project.date=request.POST.get('date')
        project.links=request.POST.get('links')
        project.save()
        return redirect('/proj/portfolio')
    return render(request,'project/create_project_details.html',{'bios':bios,'details':details})
def portfolio(request):
    bios=Biography.objects.all()
    details=Details.objects.all()
    projects=Project.objects.all()
    return render(request,'portfolios/index.html',{'bios':bios,'details':details,'projects':projects})