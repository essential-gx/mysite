from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.models import Department, UserInfo


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


def user_list(request):
	return render(request, "user_list.html")


def orm(request):
	# 1. 添加数据
	# Department.objects.create(title="研发部")
	# UserInfo.objects.create(name="诸葛亮",password="zgl",age=18)
	# UserInfo.objects.create(name="张飞",password="zf")
	# 2. 删除数据
	# 条件删除：UserInfo.objects.filter(name="张飞").delete()
	# 删除所有：UserInfo.objects.all().delete()
	# 3. 获取数据
	# UserInfo.objects.all()
	# UserInfo.objects.filter(name="诸葛亮").first()
	# 4. 修改数据
	# UserInfo.objects.all().update(age=20)
	UserInfo.objects.filter(name="诸葛亮").update(age=59)
	
	return render(request, "user_add.html")


def tpl(request):
	name = "高希"
	roles = ["管理员", "CEO", "保安"]
	user_info = {
		"name": "gx",
		"age": 18,
		"roles": ["管理员", "CEO", "保安"],
	}
	return render(request, "tpl.html", {"name": name, "roles": roles, "user": user_info})


def something(request):
	# request是一个对象，封装了用户发送过来的请求数据
	
	# 1. 获取请求方式
	print(request.method)
	# 2. 获取GET请求数据
	# URL请求：http://127.0.0.1:8000/polls/something/?name=gx&ages=[12,23]
	print(request.GET)
	# 3. 获取POST请求数据
	#
	print(request.POST)
	# 4. 将响应数据以字符串形式返回
	# return HttpResponse("响应数据")
	# 5. 将响应数据以页面形式返回
	# return render(request,'something.html',{...})
	# 6. 重定向
	return redirect("https://www.bilibili.com/")


def login(request):
	if request.method == "GET":
		return render(request, "login.html")
	elif request.method == "POST":
		user_name = request.POST.get("user")
		password = request.POST.get("pwd")
		# print(request.POST)
		# 用户名称密码校验
		if user_name == "root" and password == "123":
			return redirect("https://www.bilibili.com/")
		else:
			return render(request, "login.html", {"msg": "用户名或密码不正确"})
		

def info_list(request):
	users = UserInfo.objects.all()
	return render(request,"info_list.html",{"users":users})


def user_add(request):
	if request.method == "GET":
		return render(request, "user_add.html")
	elif request.method == "POST":
		name = str(request.POST.get("username"))
		pwd = str(request.POST.get("password"))
		age = int(request.POST.get("age"))
		UserInfo.objects.create(name=name,password=pwd,age=age)
		return redirect("polls:info_list")
	
def user_delete(request,nid):
	nid = int(nid)
	UserInfo.objects.filter(id=nid).delete()
	return redirect("polls:info_list")