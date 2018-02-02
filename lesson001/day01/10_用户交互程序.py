#Author:命命

#一.注释
#单行注释
msg1 = "注释内容"
#多行注释
msg2 = """
name1 = '注释内容’
name2 = '注释内容’
name3 = '注释内容’
"""
print(msg2)

#二、格式化输入  %s接受字符串  %d接受整数  %f接受浮点数
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")
info = '''
------------info of %s-------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)
print(info)