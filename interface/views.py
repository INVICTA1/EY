import socket
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from datetime import timedelta

from interface.models import File,Row
from .parse_file import parse_file

# Create your views here.
def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            newfile = File()
            row = Row()
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)  # сохранили файл в папку
            newfile.name = filename
            rows_excel = parse_file('excel_files/' + myfile.name)
            newfile.save()
            for row_excel in rows_excel:
                row.file_id = newfile
                row.bank_account,row.incoming_saldo_asset,row.incoming_saldo_liabilities,row.turnover_credit,\
                row.turnover_debit,row.outgoing_saldo_asset,row.outgoing_saldo_liabilities,row.class_type =row_excel[0]
                row.save()


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


def get_file_content(request,name):
    print('get_file_content')
    if request.method == 'GET':
        files = File.objects.all()
        for file in files:
            a= file.details.values_list('bank_account',flat=True)
            if file.name == name:
                pass

        return  render(request, 'mysite/index.html')



