# Generated by Django 4.1.4 on 2022-12-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
    ]
