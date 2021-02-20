from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

from django.db import models
from django.urls import reverse


class Fitness(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='fitness/pics', default="")
    desc = models.TextField(max_length=1000, help_text="Enter brief desc of Fitness club")
    address = models.TextField(max_length=1000, help_text="Enter address of Fitness club")
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    contact_no = models.CharField(max_length=20, default="")
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=200, default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fitness-detail', args=[str(self.id)])


class Trainer(models.Model):
    fitness = models.ForeignKey(Fitness, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='yoga/trainer', default="")
    name = models.CharField(max_length=200)
    exp = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TrainingLevel(models.Model):
    fitness = models.ForeignKey(Fitness, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='fitness/trainer', default="")
    training_name = models.CharField(max_length=200)
    training_type = models.CharField(max_length=200)

    class Meta:
        ordering = ['training_name', 'training_type']

    def __str__(self):
        return self.training_name
