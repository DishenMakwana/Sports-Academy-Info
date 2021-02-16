from django.shortcuts import get_object_or_404, render
from .models import Yoga, Guru
from django.views import generic
from django.http import request


class YogaListView(generic.ListView):
    model = Yoga


class YogaDetailView(generic.DetailView):
    model = Yoga

    def yoga_detail_view(self, primary_key):
        yoga = get_object_or_404(Yoga, pk=primary_key)
        return render(request, 'yoga/yoga_detail.html', context={'yoga': yoga})
