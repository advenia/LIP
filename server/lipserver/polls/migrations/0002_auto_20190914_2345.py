# Generated by Django 2.2.5 on 2019-09-15 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='description',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='y',
            new_name='longitude',
        ),
    ]
