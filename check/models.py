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
    fullname = models.CharField(
        verbose_name="ФИО",
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

    def __str__(self):
        return "%s" % self.fullname

    def __unicode__(self):
        return "%s" % self.fullname


class Lesson(models.Model):
    MATH = 'MATH'
    PHYS = 'PHYS'
    ALG = 'ALG'
    DRG = 'DRG'
    CHM = 'CHM'
    HSTR = 'HSTR'
    MSC = 'MSC'
    BIO = 'BIO'
    LESSON_TYPE_CHOICES = [
        (MATH, 'Математика'),
        (PHYS, 'Физика'),
        (ALG, 'Алгебра'),
        (DRG, 'Рисование'),
        (CHM, 'Химия'),
        (HSTR, 'История'),
        (MSC, 'Музыка'),
        (BIO, 'Биология'),
    ]

    LESSON1 = 'LESSON1'
    LESSON2 = 'LESSON2'
    LESSON3 = 'LESSON3'
    LESSON4 = 'LESSON4'
    LESSON5 = 'LESSON5'
    LESSON6 = 'LESSON6'
    LESSON_ORDER_CHOICES = [
        (LESSON1, 'Первый урок'),
        (LESSON2, 'Второй урок'),
        (LESSON3, 'Третий урок'),
        (LESSON4, 'Червертый урок'),
        (LESSON5, 'Пятый урок'),
        (LESSON6, 'Шестой урок'),
    ]

    name = models.CharField(
            verbose_name="Предмет",
            max_length=4,
            choices=LESSON_TYPE_CHOICES,
            default=MATH,
    )
    lesson_order = models.CharField(
        verbose_name="Порядковый номер урока",
        max_length=7,
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


