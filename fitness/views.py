from django.shortcuts import get_object_or_404, render
from .models import Fitness, Trainer
from django.views import generic
from django.http import request


class FitnessListView(generic.ListView):
    model = Fitness


class FitnessDetailView(generic.DetailView):
    model = Fitness

    def fitness_detail_view(self, primary_key):
        fitness = get_object_or_404(Fitness, pk=primary_key)
        return render(request, 'fitness/fitness_detail.html', context={'fitness': fitness})
