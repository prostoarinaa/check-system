# Generated by Django 4.1.4 on 2022-12-26 12:57

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Никнейм')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('email_checked', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Программирование', 'Программирование'), ('Иностранный язык', 'Иностранный язык'), ('Математический анализ', 'Математический анализ'), ('ЭВМ и периферийные устройства', 'ЭВМ и периферийные устройства'), ('Сетевые технологии', 'Сетевые технологии'), ('Вычислительная математика ', 'Вычислительная математика '), ('Базы данных', 'Базы данных'), ('Защита информации', 'Защита информации')], default='Программирование', max_length=30, verbose_name='Предмет')),
                ('lesson_order', models.CharField(choices=[('Первая пара', 'Первая пара'), ('Вторая пара', 'Вторая пара'), ('Тетья пара', 'Тетья пара'), ('Четвертая пара', 'Четвертая пара'), ('Пятая пара', 'Пятая пара'), ('Шестая пара', 'Шестая пара'), ('Седьмая пара', 'Седьмая пара'), ('Воосьмая пара', 'Воосьмая пара')], default='Первая пара', max_length=15, verbose_name='Номер пары')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson',
            field=models.ManyToManyField(through='check.Mark', to=settings.AUTH_USER_MODEL),
        ),
    ]
