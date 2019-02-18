from django.contrib import admin

# Register your models here.
from main.models import UserExtended, TypeOf, Organization, Donation

admin.site.register(UserExtended)
admin.site.register(TypeOf)
admin.site.register(Organization)
admin.site.register(Donation)

