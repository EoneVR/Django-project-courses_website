from django.contrib import admin
from .models import Courses


# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_of_start', 'price', 'language']
    list_display_links = ['id', 'title']
    list_editable = ['price']


admin.site.register(Courses, CoursesAdmin)
