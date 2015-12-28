from django.contrib import admin

# Register your models here.
from .models import Question, Choice


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ('questionText', 'pubDate')


@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    list_display = ('question', 'choiceText', 'votes')



