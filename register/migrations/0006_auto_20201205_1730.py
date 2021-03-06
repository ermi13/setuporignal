# Generated by Django 3.1.2 on 2020-12-05 14:30

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20201205_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='first_name',
            field=models.CharField(max_length=100, validators=[register.models.validate_fname]),
        ),
        migrations.AlterField(
            model_name='developers',
            name='last_name',
            field=models.CharField(max_length=100, validators=[register.models.validate_lname]),
        ),
    ]
