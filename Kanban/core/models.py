from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Role(models.Model):
    PROJECT_MANAGER = 1
    SCRUM_MASTER = 2
    DEVELOPER = 3
    ROLE_CHOICES = (
        (PROJECT_MANAGER, 'project_manager'),
        (SCRUM_MASTER, 'scrum_master'),
        (DEVELOPER, 'developer'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_no = models.CharField(max_length=13)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.username}"


class Technology(models.Model):
    technology_id = models.AutoField(primary_key=True)
    technology_name = models.CharField(max_length=255)

    def __str__(self):
        return self.technology_name


class DeveloperProfile(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.base_user.username}"


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_updated_by')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_created_by')
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_updated_by')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_created_by')


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_updated_by')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_created_by')
    user = models.ManyToManyField(User)
 

class Comment(models.Model):
    comment = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
