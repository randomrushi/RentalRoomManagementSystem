# Generated by Django 3.1.4 on 2020-12-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0004_auto_20201211_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='propdef.jpg', upload_to='property'),
        ),
    ]
