from django.shortcuts import render, HttpResponse
from django.db.utils import IntegrityError
from .models import NewPerson, CommunityPerson


# Create your views here.
def new_person_request(request):
    return render(request, 'new_person.html')


def new_person_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        class_num = request.POST.get('class_num')
        school = request.POST.get('school')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        qq_num = request.POST.get('qq_num')
        changeable = request.POST.get('changeable')

        try:
            NewPerson.objects.get_or_create(
                name=name,
                sex=sex,
                class_num=class_num,
                school=school,
                department=department,
                phone=phone,
                qq_num=qq_num,
                changeable=changeable
            )
        except IntegrityError as e:
            return HttpResponse('提交出错，此手机号已有记录，且你提交的内容与记录内容有不同处，重复提交无效。如需修改信息请联系我们')
        '''
        print(name)
        print(sex)
        print(class_num)
        print(school)
        print(department)
        print(phone)
        print(qq_num)
        print(changeable)
        '''
        return render(request, 'thanks.html')
    else:
        return render(request, 'new_person.html')


def community_person_request(request):
    return render(request, 'kexie_person.html')


def submit(request, name, sex, class_num, school, phone, qq_num, department, changeable):
    NewPerson.objects.get_or_create(
        name=name,
        sex=sex,
        class_num=class_num,
        school=school,
        department=department,
        phone=phone,
        qq_num=qq_num,
        changeable=changeable
    )
    '''
    print('姓名：', name)
    print('性别：', sex)
    print('班级：', class_num)
    print('校区：', school)
    print('学号：', stu_id)
    print('手机号：', phone)
    print('QQ号：', qq_num)
    print('想去的部门：', department)
    print('是否服从调剂：', changeable)
    '''
    return HttpResponse('提交成功！')


def community_person_submit(request):
    if request.method == 'POST':
        sex = request.POST.get('sex')
        name = request.POST.get('name')
        address = request.POST.get('address')
        activity = request.POST.get('activity')
        department = request.POST.get('department')
        department_job = request.POST.get('department_job')
        phone = request.POST.get('phone')
        # print(name)
        # print(sex)
        # print(address)
        # print(activity)
        # print(department)
        # print(department_job)
        # print(phone)
        try:
            CommunityPerson.objects.get_or_create(
                name=name,
                sex=sex,
                department=department,
                department_job=department_job,
                address=address,
                activity=activity,
                phone=phone,
            )
        except IntegrityError as e:
            return HttpResponse('提交出错，此学号已有记录，且你提交的内容与记录内容有不同处，重复提交无效。如需修改信息请联系我们')

        return render(request, 'thanks.html')
    else:
        return render(request, 'kexie_person.html')
