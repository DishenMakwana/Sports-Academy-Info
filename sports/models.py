from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

from django.db import models
from django.urls import reverse


class Academy(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='sports/pics', default="")
    desc = models.TextField(max_length=1000, help_text="Enter a brief desc of academy")
    address = models.TextField(max_length=1000, help_text="Enter address of academy")
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
        return reverse('academy-detail', args=[str(self.id)])


class Coach(models.Model):
    academy = models.ForeignKey(Academy, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='yoga/trainer', default="")
    name = models.CharField(max_length=200)
    exp = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Sports(models.Model):
    academy = models.ForeignKey(Academy, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='sports/trainer', default="")
    sports_name = models.CharField(max_length=200)
    sports_type = models.CharField(max_length=200)

    class Meta:
        ordering = ['sports_name', 'sports_type']

    def __str__(self):
        return self.sports_name
