# Generated by Django 3.1.4 on 2020-12-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0003_owner_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('vishnupuri', 'vishnupuri')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='district',
            field=models.CharField(choices=[('nanded', 'nanded'), ('nagpur', 'nagpur')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='landmark',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(choices=[('Maharashtra', 'Maharashtra')], max_length=50, null=True),
        ),
    ]