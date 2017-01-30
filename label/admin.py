from django.contrib import admin

# Register your models here.
from django.contrib import admin
from label.models import sensedb,warpdb,altemadb,bunkaidb,maltinedb,flaudb,progressivedb,trekkiedb,planetdb,lineid,diggerdb

admin.site.register(sensedb)
admin.site.register(warpdb)
admin.site.register(altemadb)
admin.site.register(bunkaidb)
admin.site.register(maltinedb)
admin.site.register(flaudb)
admin.site.register(progressivedb)
admin.site.register(trekkiedb)
admin.site.register(planetdb)
admin.site.register(lineid)
admin.site.register(diggerdb)