# Generated by Django 4.2.4 on 2023-09-12 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactUs',
        ),
        migrations.DeleteModel(
            name='ApprenticeShip',
        ),
    ]
