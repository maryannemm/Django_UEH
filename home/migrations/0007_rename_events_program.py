# Generated by Django 4.2.1 on 2023-05-12 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_index'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='events',
            new_name='program',
        ),
    ]