import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from .models import Urls
from django.contrib.auth.decorators import permission_required
from . models import Urls
from django.contrib import messages
import  re

@permission_required('admin.can_add_log_entry')
def data_upload(request):
    template = "applet/upload.html";

    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Urls.objects.update_or_create(
            sr_no = column[0],
            prn=column[1],
            links=column[2],
            count=column[3],
            
        )
    context = {}
    return render(request, template, context)


def index(request):
        template = 'applet/start.html'
        temp = []
        uname = request.user.username
        all_urls = Urls.objects.all()

        cnt=0
        for url in all_urls:
            if url.prn == uname:
                temp.append(url)
                cnt+=1
                if cnt == 5:
                    break


        context = {'all_urls' :all_urls ,'uname' : uname,'n' : range(5),'temp' : temp}
        return render(request,template,context)
	

def youtube(request):
    template = 'applet/youtube.html'
    temp = []
    uname = request.user.username
    all_urls = Urls.objects.all()


    for url in all_urls:

        if url.prn == uname:
            if re.match("https://www.youtube.com", str(url.links))!=None:
                temp.append(url)



    for i in temp:
        print(i)
    context = {'all_urls': all_urls, 'temp': temp}
    return render(request, template, context)




