from django.apps import AppConfig


def startup():
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Lesson, Mark

    teachers, created = Group.objects.get_or_create(name='teachers_group')
    students, created = Group.objects.get_or_create(name='students_group')

    ct_l = ContentType.objects.get_for_model(Lesson)
    ct_m = ContentType.objects.get_for_model(Mark)

    can_add_lesson = Permission.objects.get(codename='add_lesson',
                                            name='Can add lesson',
                                            content_type=ct_l)
    # all_permissions = Permission.objects.filter(content_type__app_label='check', content_type__model='lesson')

    can_add_mark = Permission.objects.get(codename='add_mark',
                                          name='Can add mark',
                                          content_type=ct_m)
    can_view_mark = Permission.objects.get(codename='view_mark',
                                           name='Can view mark',
                                           content_type=ct_m)

    if can_add_lesson not in Permission.objects.filter(group=teachers):
        teachers.permissions.add(can_add_lesson)
    if can_add_mark not in Permission.objects.filter(group=students):
        students.permissions.add(can_add_mark)
    if can_view_mark not in Permission.objects.filter(group=teachers):
        students.permissions.add(can_view_mark)

    for p in Permission.objects.filter(group=teachers):
        print(p.codename)
    for p in Permission.objects.filter(group=students):
        print(p.codename)


class CheckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'check'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN'):
            startup()
