from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuetionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'],  # 필드 순서 변경
    fieldsets = [
        ('Date Infomation', {'fields':['pub_date'], 'classes':['collapse']}),
        ('Question Statement', {'fields':['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuetionAdmin)
admin.site.register(Choice)