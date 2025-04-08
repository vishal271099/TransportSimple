from django.contrib import admin
from .models import Question, Answer, Like

# Register the Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at')  # Fields to display in list view
    search_fields = ('title', 'description')  # Fields to search in admin
    list_filter = ('created_at',)  # Filters for sidebar
    ordering = ('-created_at',)  # Default ordering by created_at, descending

# Register the Answer model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')  # Fields to display in list view
    search_fields = ('content',)  # Fields to search in admin
    list_filter = ('created_at',)  # Filters for sidebar
    ordering = ('-created_at',)  # Default ordering by created_at, descending

# Register the Like model
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Fields to display in list view
    list_filter = ('created_at',)  # Filters for sidebar
    ordering = ('-created_at',)  # Default ordering by created_at, descending

# Register the models with custom admin configurations
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Like, LikeAdmin)
