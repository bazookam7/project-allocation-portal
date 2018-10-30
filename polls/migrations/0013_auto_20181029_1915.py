# Generated by Django 2.1.2 on 2018-10-29 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20181029_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allprojects',
            name='ProjectID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='InstructorID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='students',
            name='StudentID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='updatedproject',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 19, 15, 2, 761999, tzinfo=utc)),
        ),
    ]
