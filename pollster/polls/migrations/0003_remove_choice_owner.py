# Generated by Django 3.0.8 on 2020-11-07 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201107_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='owner',
        ),
    ]
