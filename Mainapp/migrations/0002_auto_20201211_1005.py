# Generated by Django 3.1.4 on 2020-12-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenent',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='tenent',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='tenent',
            name='empolybility',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='tenent',
            name='highest_education',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='tenent',
            name='home_address',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tenent',
            name='maried',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenent',
            name='work_address',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
