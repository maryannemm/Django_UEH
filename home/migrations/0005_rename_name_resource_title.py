# Generated by Django 4.2.1 on 2023-05-12 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_resource_about_alter_resource_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='title',
        ),
    ]
