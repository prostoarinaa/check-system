# Generated by Django 4.1.4 on 2022-12-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_lesson_mark_lesson_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]