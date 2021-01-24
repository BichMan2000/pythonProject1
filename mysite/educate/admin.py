from django.contrib import admin
from.models import users,user_learning_history,roles,permission,role_permission,course_document_file,course_document,course,course_user
# Register your models here.
class studentsadmin(admin.ModelAdmin):
    list_display = ['name','create_at']
    list_filter = ['create_at']
    search_fields = ['id']


admin.site.register(users)
admin.site.register(user_learning_history)
admin.site.register(roles)
admin.site.register(permission)
admin.site.register(role_permission)
admin.site.register(course_user)
admin.site.register(course_document)
admin.site.register(course_document_file)
admin.site.register(course)