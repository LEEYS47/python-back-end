from django.shortcuts import get_object_or_404,render
from mysite.models import MainContent

# Create your views here.

def mainpage(request):
    content_list=MainContent.objects.order_by('-pub_date')
    context={'content_list':content_list}
    return render(request,'pages/mainpage.html',context)

def detail(request,content_id):
    content_list=get_object_or_404(MainContent,pk=content_id)
    context={'content_list':content_list}
    return render(request,'mysite/content_detail.html',context)

# def mainpage(request):
#    return render(request,'pages/mainpage.html')

def company(request):
    return render(request,'pages/company_info.html')