from django.db import models


class Branch(models.Model):
  BranchName = models.CharField(max_length=255)
  BranchCode = models.IntegerField()
  Contact =models.CharField(max_length=255)
  IFSCCode = models.CharField(max_length=11)
  MICRCODE = models.IntegerField()
  District  = models.CharField(max_length=150)
  Address  = models.CharField(max_length=300)
  PinCode = models.IntegerField()
  Email = models.EmailField(max_length=254)