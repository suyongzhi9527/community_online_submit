import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Student, SystemControl, Activity, AcademyClass


# Register your models here.


@admin.register(SystemControl)
class SystemControlInformation(admin.ModelAdmin):
    list_display = ('id', 'can_submit', 'team_size', 'was_published_recently')


@admin.register(Activity)
class ActivityInformation(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super(ActivityInformation, self).save_model(request, obj, form, change)


@admin.register(Student)
class StudentInformation(admin.ModelAdmin):
    list_display = ('name', 'stu_id', 'class_num', 'academy', 'qq_num', 'phone', 'team_id', 'is_leader', 'submit_time',)
    list_filter = ('class_num', 'academy', 'is_leader',)
    search_fields = ('name', 'stu_id', 'class_num', 'academy', 'qq_num', 'phone', 'team_id', 'is_leader', 'submit_time',)
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        meta = self.model._meta  # 用于确定导出的文件名, 格式为: app名.模型类名
        field_names = [field.name for field in meta.fields]  # 所有属性名

        response = HttpResponse(content_type='text/csv')  # 指定响应内容类型
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        response.charset = 'utf-8-sig'  # 可选, 修改编码为带BOM的utf-8格式(Excel打开不会有乱码)
        writer = csv.writer(response)
        writer.writerow(field_names)  # 将属性名写入csv
        for obj in queryset:  # 遍历要导出的对象列表
            row = writer.writerow([getattr(obj, field) for field in field_names])  # 将当前对象的各属性值写入csv
        return response

    export_as_csv.short_description = '表格形式导出所选内容'


@admin.register(AcademyClass)
class AcademyClassInformation(admin.ModelAdmin):
    list_display = ('class_name', 'academy',)
    list_filter = ('academy', 'class_name',)
    search_fields = ('academy', 'class_name',)

"""
目前情况是这样，我现在公司是做亚马逊跨境电商的嘛，上个月公司把办公室分租去了
同时主管也跑路我觉得老大都跑了说明情况不太好吧，不过今年大环境下电商公司都不好过。
现在部门7个人，只有我和另一个同事在负责公司ERP系统业务，其他人在搞区块链。
因为现在没啥新的业务开发了，现在工作只算是维护一下系统，没什么事做的了就很闲
然后我就在想要不要跳槽，上周8号就刚好入职满一年。
"""