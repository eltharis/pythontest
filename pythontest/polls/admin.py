from django.contrib import admin

# Register your models here.
from .models import Question, Choice


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    pass

@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    pass


