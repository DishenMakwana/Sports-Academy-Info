# Generated by Django 3.1.2 on 2020-10-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0003_auto_20201020_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='city',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
    ]