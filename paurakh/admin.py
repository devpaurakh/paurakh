from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Home)



#About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]

#skill
class skillsInLine(admin.TabularInline):
    model = Skills
    extra = 2
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        skillsInLine,
    ]
    
#portfolio
admin.site.register(Portfolio)