# Generated by Django 3.1.2 on 2020-10-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0008_auto_20201029_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='loc',
            field=models.TextField(default='', help_text='Enter Your Location here. Steps -> Go to google map, tap on your location, Click share and choose Embed-map tab, Copy only url and paste it here.', max_length=1000),
        ),
    ]
