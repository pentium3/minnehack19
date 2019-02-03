# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from myproject.settings import MEDIA_ROOT
from myproject.myapp.classify import classify

# def list(request):
#     print('hahahahahahahaha')
#     filestr=''
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()
#             #print newdoc.docfile.url, newdoc.docfile.name
#             filestr=MEDIA_ROOT + '/' + newdoc.docfile.name
#             res=233333
#             res=classify(filestr)

#             # Redirect to the document list after POST
#             # Render list page with the documents and the form
#             return render(
#                 request,
#                 'list.html',
#                 {'form': form, 'newdoc': filestr, 'result': res, }
#             )
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = DocumentForm()  # A empty, unbound form

#     # Load documents for the list page
#     #documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render(
#         request,
#         'list.html',
#         {'form': form, 'newdoc': filestr, }
#     )


 
def list(request):
    zipcode = request.GET.get('zipcode','')
    plant = request.GET.get('choices-single-defaul','')
    results = []
    if zipcode:
        results.append(str(zipcode))
    if plant:
        results.append(str(plant))
    print(zipcode)
    print(plant)
    if(zipcode and plant):
        res = classify(zipcode, plant)
        results.append(res)
    print(results)
    return render(
        request,
        'list.html',
        {'results': results, }
    )
