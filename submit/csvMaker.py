# -*- coding:utf-8 -*-
# @Author: syz
# @Time: 2022/11/11 18:00
# @File: csvMaker.py
import csv
import codecs
import importlib
import sys
from django.http import HttpResponse

importlib.reload(sys)


def export_as_csv_action(description='Export selected objects as CSV file', fields=None, exclude=None, header=True):
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        if not fields:
            field_names = [field for field in opts]
        else:
            field_names = fields

        response = HttpResponse(content_type='text/csv')
        response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name.encode('utf-8'))
        writer = csv.writer(response)
        if header:
            cn_field_names = ['姓名', '性别' '学号', '班级', '校区' '意向部门', '手机号', 'qq号', '是否服从调剂']

            writer.writerow(cn_field_names)
        for obj in queryset:
            # row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]
            # 新增处理功能，比如处理时间的显示格式
            row = []
            for field in field_names:
                value = getattr(obj, field).encode("utf8")
                #                if (field == 'publishing_time'):
                #                    value = str(value)
                #                if isinstance(value, datetime.datetime):
                #                    value = value.strftime('%y-%m-%d')
                row.append(value)
            writer.writerow(row)
        return response

    export_as_csv.short_description = description
    return export_as_csv
