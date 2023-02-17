from django.db import models

class Member(models.Model):
  membership_number = models.IntegerField(null=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  double_player = models.BooleanField()

  def __str__(self):
    return f"{self.firstname} {self.lastname}"