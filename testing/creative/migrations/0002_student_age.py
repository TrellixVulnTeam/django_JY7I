# Generated by Django 2.2.3 on 2019-08-08 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
