from django.http import HttpResponse
from TestModel.models import test


# 数据库插入操作
def testdb_insert(request):
    test1 = test(name='runoob',hobby="sing song")
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
# 数据库查询操作
def testdb_query(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = test.objects.filter(id=1)

    # 获取单个对象
    response3 = test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # 排序方式 asc 默认，reverse函数改变顺序
    for i in test.objects.order_by('name')[0:4]:
        print(i.name+" "+ i.hobby)

    # 数据排序
    for i in test.objects.order_by("id").reverse():
        print(i.id)

    # 上面的方法可以连锁使用
    test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " " + var.hobby
    response = response1
    return HttpResponse("<p>" + response + "</p>")
# 数据库更新操作
def testdb_update(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    test.objects.filter(id=1).update(name='Google1')

    # 修改所有的列
    # test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")
# 数据库删除操作
def testdb_delete(request):
    # 删除id=3的数据
    test1 = test.objects.get(id=3)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")