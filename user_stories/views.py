from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from user_stories.models import *

# Create your views here.


class NewRoom(View):
    def get(self, request):
        return render(request, "new_room.html")

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        new_room = Room.objects.create(name=f'{name}', capacity = capacity)
        if projector:
            new_room.projector = True
            new_room.save()
        msg = "Dodano nową salę"
        return render(request, "base.html", locals())



class Rooms(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, "rooms.html", locals())

                      # {"rooms": rooms})