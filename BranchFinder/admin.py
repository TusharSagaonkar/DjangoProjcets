from django.contrib import admin
from BranchFinder.models import Branch,Passw
from django.contrib.auth.models import Group


class BranchAdmin(admin.ModelAdmin):
    list_display = ('BranchName', 'BranchCode','Contact' ,'IFSCCode','PinCode','Email')
    search_fields = ['BranchName', 'BranchCode']
  
class PasswAdmin(admin.ModelAdmin):
    list_display = ('ApplicationName','UserName', 'Password')
    # Let you to search with first name, last name and phone number of the customer
    #search_fields = ['ApplicationName']
    # There will be a filter on last name
    list_filter = ['ApplicationName']

                    
# Register your models here.
admin.site.register(Branch, BranchAdmin)
admin.site.register(Passw, PasswAdmin)
admin.site.unregister(Group)
