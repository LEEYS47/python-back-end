from django.shortcuts import render
# from django.http import HttpResponse 삭제
from .models import MainContent
def index(request):
    # return HttpResponse("Hello world") 삭제
    content_list=MainContent.objects.order_by('-pub_date')
    context={'content_list':content_list}
    return render(request,'mysite/content_list.html',context)