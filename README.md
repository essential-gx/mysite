# Django学习项目
## 安装

~~~ shell
pip install django
~~~

## 创建项目

~~~ sh
$ django-admin startproject mysite
~~~

mysite：Django项目名称

## 项目结构

~~~ 
mysite/ # 项目根路径
    manage.py # Django项目的命令行工具
    mysite/ # 
        __init__.py
        settings.py # Django项目的配置文件
        urls.py # Django 项目的 URL 声明
        asgi.py # ASGI 兼容的 Web 服务器上的入口
        wsgi.py # WSGI 兼容的Web服务器上的入口
    templates/ # Django项目模板目录
~~~

## 项目启动

默认IP地址和端口的启动方式：

~~~ shell
$ python manage.py runserver
~~~

指定端口的启动方式：

~~~ shell
$ python manage.py runserver 8080
~~~

指定IP地址和端口的启动方式：

~~~ shell
$ python manage.py runserver 0.0.0.0:8000
~~~

0.0.0.0表示服务器本机所有的IPV4地址。

## 个性化配置

* 汉化
* 指定模板
* 指定数据库
* 指定静态路径

## 创建应用

1. 命令行方式创建应用：

~~~ shell
$ python manage.py startapp polls
~~~

polls：创建的应用名称

2. 将应用注册的项目中：

~~~ python
# mysite/settings.py
...
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls.apps.PollsConfig" # 
]
...
~~~



polls应用的目录结构：

~~~ 
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
~~~

## 编写视图

编写视图层函数：

```python
# polls/views.py¶
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

编辑URL路径：

```python
# polls应用下的URL
# polls/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]

# django项目下的总URL
# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

重新启动项目后，浏览器访问 http://localhost:8000/polls/，能够看见 "*Hello, world. You're at the polls index.*" 

## Path函数

> path()参数： `route`，匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 `urlpatterns` 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

> path()参数： `view`，当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。

> path()参数： `kwargs`，任意个关键字参数可以作为一个字典传递给目标视图函数。

> path()参数： `name`，为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。









































