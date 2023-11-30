from django.contrib import admin

# Register your models here.
from .models import Candidate, Career


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'career']
    search_fields = ['name', 'phone', 'email']
    list_per_page = 10


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Career)
