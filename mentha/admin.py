from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
	    if not obj.id:
	        obj.owner = request.user
	    obj.save()

class PayeeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
	    if not obj.id:
	        obj.owner = request.user
	    obj.save()

admin.site.register(models.Account)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Payee, PayeeAdmin)
admin.site.register(models.Transaction)
