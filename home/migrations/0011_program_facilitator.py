# Generated by Django 4.2.1 on 2023-05-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_index_testimony_program_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='facilitator',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
