# Generated by Django 4.0.6 on 2022-07-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='videos',
        ),
        migrations.AddField(
            model_name='movie',
            name='videos',
            field=models.ManyToManyField(to='core.video'),
        ),
    ]
