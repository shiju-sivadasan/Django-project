# Generated by Django 5.0.6 on 2024-06-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('projects', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('certifications', models.TextField()),
            ],
        ),
    ]
