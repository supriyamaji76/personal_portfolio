from django.contrib import admin
from base.models import Contact, Project, Skill

# Register the Contact model
admin.site.register(Contact)
admin.site.register(Project)
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)