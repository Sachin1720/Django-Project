from django.db import models

# Create your models here.
post_choices = (
    ("HR", "HR"), ("MANAGER", "MANAGER"), ("SENIOR ENGINEER", "SENIOR ENGINEER"),
)


class Employee(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    post = models.CharField(max_length=20, choices=post_choices)

    def __str__(self):
        return self.firstname + " " + self.lastname
