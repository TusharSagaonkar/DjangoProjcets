from django.contrib import admin
from BranchFinder.models import Branch,Passw,LinksMaster
from django.contrib.auth.models import Group


class BranchAdmin(admin.ModelAdmin):
    list_display = ('BranchName', 'BranchCode','Contact' ,'IFSCCode','PinCode','Email')
    search_fields = ['BranchName', 'BranchCode']
  
class PasswAdmin(admin.ModelAdmin):

  def get_queryset(self, request):
    qs = super(PasswAdmin, self).get_queryset(request)
    if request.user.is_superuser:
      return qs
    return qs.filter(user=request.user)
    
  list_display = ('ApplicationName','UserName', 'Password')
    # Let you to search with first name, last name and phone number of the customer
    #search_fields = ['ApplicationName']
    # There will be a filter on last name
  list_filter = ['ApplicationName']
  
class LinksAdmin(admin.ModelAdmin):

    list_display = ('LinkType', 'LinkName','Link')
    search_fields = ['LinkType', 'LinkName']
                    
# Register your models here.
admin.site.register(Branch, BranchAdmin)
admin.site.register(Passw, PasswAdmin)
admin.site.register(LinksMaster, LinksAdmin)
admin.site.unregister(Group)