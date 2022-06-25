# created by me
import os
from django.http import HttpResponse
from django.shortcuts import render
from . import process
import tempfile, zipfile
from django.http import HttpResponse
from wsgiref.util import FileWrapper


def solve(request):
    # is request se data utha sakte hai form ka
    # print(request.GET.get('givenMatrix', 'default')) : jis element ka naam text hai request mai uska data utha lega
    print("Control came here.")
    process.simulateGraph(request)
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    images = os.listdir('static/output')
    for image in images:
        fullpath = f'/Users/vaibhavgoyal/Documents/Programming/Python/PycharmProjects/GraphVisualiser/static/output/{image}'
        archive.write(fullpath, image)

    archive.close()

    temp.seek(0)
    wrapper = FileWrapper(temp)

    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=test.zip'

    return response