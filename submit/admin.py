from django.contrib import admin
from .models import NewPerson, CommunityPerson
from .csvMaker import export_as_csv_action


# Register your models here.

class NewPersonProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'department', 'phone', 'changeable', 'address', 'activity')
    list_filter = ('name', 'sex', 'department', 'phone', 'changeable', 'address', 'activity')
    search_fields = ('name', 'sex', 'department', 'phone', 'changeable', 'address', 'activity')
    actions = [export_as_csv_action('导出表格', fields=['name', 'sex', 'class_num', 'school' 'department', 'phone', 'qq_num', 'changeable'])]


class CommunityPersonProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'department', 'department_job', 'phone', 'activity', 'address')
    list_filter = ('id', 'name', 'sex', 'department', 'department_job', 'phone', 'activity', 'address')
    search_fields = ('id', 'name', 'sex', 'department', 'department_job', 'phone', 'activity', 'address')
    actions = [export_as_csv_action('导出表格', fields=['name', 'sex', 'class_num', 'school' 'department', 'phone', 'qq_num', 'changeable'])]


admin.site.register(NewPerson, NewPersonProfileAdmin)
admin.site.register(CommunityPerson, CommunityPersonProfileAdmin)
