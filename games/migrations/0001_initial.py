# Generated by Django 5.2 on 2025-04-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hangman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None, max_length=25)),
                ('words', models.TextField(default=None)),
                ('nonletters', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
