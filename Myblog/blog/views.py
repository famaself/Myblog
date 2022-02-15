from django.shortcuts import render, redirect, reverse
from .models import BlogModel
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def blog_add(request):
    # 渲染页面
    if request.method == 'GET':
        return render(request, 'blog/add.html')
    elif request.method == 'POST':
        title = request.POST.get('title')  # name中的
        content = request.POST.get('content')
        blog = BlogModel(title=title, content=content)
        blog.save()  # 将数据保存在数据库中
        b_list = BlogModel.objects.all()  # 查询所有文章
        # 文章添加成功后转到列表页
        return render(request, 'blog/list.html', {'b_list': b_list})


def list(request):
    b_list = BlogModel.objects.all()
    return render(request, 'blog/list.html', context={'b_list': b_list})


def detail(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', context={'blog': blog})


def delete(request, blog_id):
    blog = BlogModel.objects.filter(id=blog_id)  # 如果用get不含该条数据会报错无法运行
    # 如果有就删除
    if blog:
        blog.delete()
        return redirect(reverse('blog_list'))
    # 如果没有报错
    else:
        return HttpResponse('文章不存在')


def update(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)  # 如果用get不含该条数据会报错无法运行
    # 如果有就输入
    if request.method == 'GET':
        if blog:
            return render(request, 'blog/update.html',context={'blog': blog})
    # 如果没有报错
        else:
            return HttpResponse('文章不存在')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog.title = title
        blog.content = content
        blog.save()
        # BlogModel.objects.filter(id=blog_id).update(title=title,content=content)
        return redirect(reverse('blog_list'))

# def update(request, blog_id):
#     blog = BlogModel.objects.get(id=blog_id)
#     return render(request, 'blog/update.html', context={'blog': blog})

