from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Branch(models.Model):
  BranchName = models.CharField(max_length=255,unique=True)
  BranchCode = models.IntegerField(unique=True)
  Contact =models.CharField(max_length=255)
  IFSCCode = models.CharField(max_length=11,unique=True)
  MICRCODE = models.IntegerField(unique=True)
  District  = models.CharField(max_length=150)
  Address  = models.CharField(max_length=300)
  PinCode = models.IntegerField()
  Email = models.EmailField(max_length=254, unique=True)

  class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branch's Data"

Application_CHOICES = (
    ("1", "NPCI-UPI"),
    ("2", "NPCI-IMPS"), 
    ("3", "NPCI-NFS"),
    ("4", "NPCI-AEPS"),
    ("5", "NPCI-RUPAY"),
    ("6", "CONCERTO"),
    ("7", "EXCHANGE"),
    ("8", "OTHER"),
)

class Passw(models.Model):
  ApplicationName = models.CharField(max_length=50,
                                     choices = Application_CHOICES,
                                      default = '1')
  UserName = models.CharField(max_length=50)
  Password = models.CharField(max_length=50)

  
  class Meta:
        unique_together = ('ApplicationName', 'UserName')
        verbose_name = "Password"
        verbose_name_plural = "Password Manager"
  def __str__(self):
        return self.title


Link_CHOICES = (
    ("1", "Abhyudaya"),
    ("2", "NPCI"), 
    ("3", "Internet"),
)
class LinksMaster(models.Model):
  LinkType=models.CharField(max_length=50,
                            choices = Link_CHOICES,
                            default = '1')
  LinkName=models.CharField(max_length=50)
  Link=models.CharField(max_length=500)
  class Meta:
        unique_together = ('LinkType', 'LinkName')
        verbose_name = "Links"
        verbose_name_plural = "Links Manager"

  

