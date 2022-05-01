from django.db import models
from django.contrib.auth.models import User
import uuid


def upload_avatar_path(instance, filename):
    return '/'.join(['avatars', str(instance.user_profile.id) + str(".") + str("jpeg")])


class Profile(models.Model):
    user_profile = models.OneToOneField(
        User, related_name='user_profile',
        on_delete=models.CASCADE
    )
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

    def __str__(self):
        return self.user_profile.username


class Category(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item


class Task(models.Model):
    STATUS = (
        ('1', 'Before started'),
        ('2', 'On going'),
        ('3', 'Finished'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=40, choices=STATUS, default='1')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deadline = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
