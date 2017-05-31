from django.contrib import admin

# Register your models here.
from django.contrib import admin
from label.models import maltinedb,lineid,ghostlydb,releases,update,labelset




admin.site.register(maltinedb)
admin.site.register(lineid)
admin.site.register(ghostlydb)
admin.site.register(releases)
admin.site.register(update)

admin.site.register(labelset)
