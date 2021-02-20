# Generated by Django 3.1.2 on 2020-10-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0010_remove_yoga_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='loc',
            field=models.TextField(default='', help_text='Go to Google Maps, Click on your location, Click share and choose Embed map tab, Copy the url and paste it here.', max_length=1000),
        ),
    ]