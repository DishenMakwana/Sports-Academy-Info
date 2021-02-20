from django.shortcuts import get_object_or_404, redirect, render
from .models import Academy, Sports, Coach

from django.views import generic
from django.http import request


class AcademyListView(generic.ListView):
    model = Academy
    # context_object_name = 'academy_list'
    # template_name = 'templates/sports/academy_list.html'


class AcademyDetailView(generic.DetailView):
    model = Academy

    def academy_detail_view(self, primary_key):
        academy = get_object_or_404(Academy, pk=primary_key)
        return render(request, 'sports/academy_detail.html', context={'academy': academy})
