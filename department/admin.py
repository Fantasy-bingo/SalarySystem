from django.contrib import admin
from department.models import DeptInfo


class DepartmentInfoAdmin(admin.ModelAdmin):
    """
    后台，部门信息展示
    """
    list_display = ('dept_id', 'dept_name', 'dept_desc', 'create_time')
    search_fields = ('dept_name', 'create_time')
    readonly_fields = ('dept_id', 'dept_name', 'dept_desc', 'create_time')

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields


class AddDepartmentInfo(admin.ModelAdmin):
    """
    增加部门信息类
    """
    pass


admin.site.register(DeptInfo, AddDepartmentInfo)
