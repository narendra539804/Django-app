# Generated by Django 4.0.1 on 2022-03-01 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagetable',
            old_name='thumbnail',
            new_name='ImageURL',
        ),
    ]
