# Generated by Django 4.1.7 on 2023-04-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_year',
            name='session_end',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
