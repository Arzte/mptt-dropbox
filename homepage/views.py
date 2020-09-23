from django.shortcuts import render

from homepage.models import File


def index_view(request):
   files = File.objects.all()
   return render(request, 'index.html', {'files': files})
