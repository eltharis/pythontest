from django.contrib import admin

# Register your models here.
from registrations.models import *


@admin.register(TeacherGrade)
class AdminTeacherGrade(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    pass


@admin.register(TermType)
class AdminTermType(admin.ModelAdmin):
    pass


@admin.register(Term)
class AdminTerm(admin.ModelAdmin):
    pass


@admin.register(TermTime)
class AdminTermTime(admin.ModelAdmin):
    pass


@admin.register(SignedStudents)
class AdminSignedStudents(admin.ModelAdmin):
    pass


