from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group


@receiver(user_signed_up)
def assign_student_role(request, user, **kwargs):
    student_group = Group.objects.get(name="Student")
    user.groups.add(student_group)