from django.test import TestCase, Client

from activity_submit.models import Student


# Create your tests here.

class StudentTestCase(TestCase):
    # 初始化环境，包括创建初始数据
    def setUp(self) -> None:
        print('setUp方法执行，初始化数据...')
        Student.objects.create(
            name='stu1',
            stu_id=123,
            class_num='计应1班',
            qq_num='333',
            phone='111',
            academy='信息工程学院',
            team_id='95271',
            is_leader=1
        )

    def test_create_and_stu_id_show(self):
        print('test_create_and_stu_id_show')
        student = Student.objects.create(
            name='stu2',
            stu_id=1234,
            class_num='计应2班',
            qq_num='3334',
            phone='1112',
            academy='信息工程学院',
            team_id='95272',
            is_leader=0
        )
        self.assertEqual(student.stu_id, 1234, '学号字段内容与展示不一样')

    # 测试查询是否可用
    def test_filter(self):
        print('测试查询')
        students = Student.objects.get(name='stu1')
        self.assertEqual(students.academy, '信息工程学院', '该学生学院与预期结果不一样')

    def test_get_index(self):
        print('测试主页是否正常')
        client = Client()
        response = client.get('http://127.0.0.1:8000/admin/')
        self.assertEqual(response.status_code, 200, '状态码必须为200!!')
