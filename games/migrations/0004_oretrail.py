# Generated by Django 5.2 on 2025-04-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_hangmansesh_disp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oretrail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None)),
                ('body', models.CharField(default=None)),
            ],
        ),
    ]
