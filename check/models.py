from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug


# class Student(models.Model):
#     name = models.CharField(
#         verbose_name="ФИО ученика",
#         max_length=100,
#         unique=True,
#         blank=False
#     )


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Никнейм",
        max_length=150,
        unique=True,
        validators=[validate_slug]
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        blank=False,
        null=False,
        max_length=150,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        blank=False,
        null=False,
        max_length=150,
    )
    middle_name = models.CharField(
        verbose_name="Отчество",
        blank=False,
        null=False,
        max_length=150,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        blank=True,
        unique=False,
        null=True
    )
    email_checked = models.DateTimeField(
        blank=True,
        null=True
    )
    isStudent = models.BooleanField(
        verbose_name='Является студентом',
        default=True
    )

    def __str__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)

    def __unicode__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)


class Lesson(models.Model):
    L1 = 'Программирование'
    L2 = 'Иностранный язык'
    L3 = 'Математический анализ'
    L4 = 'ЭВМ и периферийные устройства'
    L5 = 'Сетевые технологии'
    L6 = 'Вычислительная математика '
    L7 = 'Базы данных'
    L8 = 'Защита информации'
    LESSON_TYPE_CHOICES = [
        (L1, 'Программирование'),
        (L2, 'Иностранный язык'),
        (L3, 'Математический анализ'),
        (L4, 'ЭВМ и периферийные устройства'),
        (L5, 'Сетевые технологии'),
        (L6, 'Вычислительная математика '),
        (L7, 'Базы данных'),
        (L8, 'Защита информации'),
    ]

    LESSON1 = 'Первая пара'
    LESSON2 = 'Вторая пара'
    LESSON3 = 'Тетья пара'
    LESSON4 = 'Четвертая пара'
    LESSON5 = 'Пятая пара'
    LESSON6 = 'Шестая пара'
    LESSON7 = 'Седьмая пара'
    LESSON8 = 'Воосьмая пара'
    LESSON_ORDER_CHOICES = [
        (LESSON1, 'Первая пара'),
        (LESSON2, 'Вторая пара'),
        (LESSON3, 'Тетья пара'),
        (LESSON4, 'Четвертая пара'),
        (LESSON5, 'Пятая пара'),
        (LESSON6, 'Шестая пара'),
        (LESSON7, 'Седьмая пара'),
        (LESSON8, 'Воосьмая пара'),
    ]

    name = models.CharField(
            verbose_name="Предмет",
            max_length=30,
            choices=LESSON_TYPE_CHOICES,
            default=L1,
    )
    lesson_order = models.CharField(
        verbose_name="Номер пары",
        max_length=15,
        choices=LESSON_ORDER_CHOICES,
        default=LESSON1,
    )
    date = models.DateField()
    lesson = models.ManyToManyField(User, through="Mark", )

    def __str__(self):
        return "%s %s %s" % (self.name, self.lesson_order, self.date)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.lesson_order, self.date)


class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s %s %s" % (self.student, self.lesson.name, self.lesson.lesson_order, self.lesson.date, self.date)

    def __unicode__(self):
        return "%s %s %s %s %s" % (self.student, self.lesson.name, self.lesson.lesson_order, self.lesson.date, self.date)


