import socket
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from datetime import timedelta

from interface.models import File
from .parse_file import insert_data_in_database, get_data_from_database


# Create your views here.
def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            newfile = File()
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)  # сохранили файл в папку
            newfile.name = filename
            newfile.save()
            insert_data_in_database('excel_files/' + myfile.name, newfile.id)
    except BaseException as e:
        print(e)
    return render(request, 'mysite/home.html')


def show_upload_files(request):
    list_file = []
    try:
        if request.method == 'GET':
            file = File.objects.all()
            for doc in file:
                list_file.append(doc)
    except BaseException as e:
        print(e)
    finally:
        return render(request, 'mysite/upload_file.html', {'list_file': list_file})


def get_file_content(request, name):
    print('get_file_content')
    if request.method == 'GET':
        files = File.objects.all()
        for file in files:
            if file.name == name:
                file_id = file.id
                rows = get_data_from_database(file_id)
                return render(request, 'mysite/index.html',{'rows':rows})
