from django.contrib import admin
from .models import Quote
from .models import Sayfa
from .models import Kisi
from .models import Gezi

class SayfaAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

class KisiAdmin(admin.ModelAdmin):
    list_display = ("id","adi",'soyadi',"tel")
    ordering = ('adi',"soyadi")
    search_fields = ('adi',"soyadi")
    empty_value_display = "---"

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'submitted', 'quotedate', 'quoteprice')
    list_filter = ('submitted', 'quotedate')
    readonly_fields = ('submitted',)
    fieldsets = (
        ('Giriş Bilgileri', {
              'fields': ('name', 'email', 'description')
        }),
        ('İletişim Bilgileri', {
              'classes': ('collapse',),
              'fields': ('position', 'company', 'address', 'phone', 'web')
        }),
        ('İş Bilgileri', {
              'classes': ('collapse',),
              'fields': ('sitestatus', 'priority','jobfile', 'submitted')
        }),
        ('Admin Yönetimi', {
            'classes': ('collapse',),
            'fields': ('quotedate', 'quoteprice','username')
        }),
    )

class GeziAdmin(admin.ModelAdmin):
    list_display = ("id", "adi", 'bolge')
    ordering = ('adi', "bolge")
    search_fields = ('adi', "bolge")

admin.site.register(Sayfa,SayfaAdmin)
admin.site.register(Kisi,KisiAdmin)
admin.site.register(Gezi,GeziAdmin)
admin.site.register(Quote,QuoteAdmin)

