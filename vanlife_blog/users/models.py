from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    email= models.EmailField(unique=True)

    def __str__(self):
        return self.username

#######################################################

# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default="")
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



post_save.connect(create_or_update_user_profile, sender=CustomUser)


# @receiver(post_save, sender=CustomUser)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         if not hasattr(instance, 'profile'):
#             Profile.objects.create(user=instance)
#         else:
#             instance.profile.save()
