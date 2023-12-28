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
