# Generated by Django 5.2 on 2025-04-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=3)),
                ('qbody', models.TextField(default=None)),
                ('c1', models.CharField(default=None)),
                ('c2', models.CharField(default=None)),
                ('c3', models.CharField(default=None)),
                ('correctans', models.CharField(default=None, max_length=1)),
            ],
        ),
    ]
