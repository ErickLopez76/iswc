import csv, io 
from re import template
from django.shortcuts import render
from django.contrib import messages
from .models import Iswc


def profile_upload(request):    # declaring template
    template = "profile_upload.html"
    data = Iswc.objects.all()# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, contributor and ISWC',
        'records': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)    
    csv_file = request.FILES['file']    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')    
    data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Iswc.objects.update_or_create(
            title=column[0],
            contributors=column[1],
            iswc=column[2]
        )
    context = {}
    return render(request, template, context)

def show_all(request):
    template = "datatable.html"
    query_results = Iswc.objects.all()
    prompt = {
        'records': query_results
    }
    context = {}
    return render(request, template, prompt)