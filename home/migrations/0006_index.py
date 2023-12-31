# Generated by Django 4.2.1 on 2023-05-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_name_resource_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('statement', models.TextField()),
                ('role', models.CharField(choices=[('V', 'Volunteer'), ('T', 'Trainee'), ('P', 'Partner')], max_length=1)),
            ],
        ),
    ]
