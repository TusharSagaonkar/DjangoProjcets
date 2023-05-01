from django.contrib import admin
from BranchFinder.models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ('BranchName', 'BranchCode', 'IFSCCode')

# Register your models here.
admin.site.register(Branch, BranchAdmin)
