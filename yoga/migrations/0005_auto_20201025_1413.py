# Generated by Django 3.1.2 on 2020-10-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0004_yoga_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='yoga',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
    ]