# Generated by Django 3.2.7 on 2021-10-08 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myticket', '0007_person_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
    ]
