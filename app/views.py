from django.shortcuts import render, redirect
from app.models import PasswordModel
from django.shortcuts import get_object_or_404


def password_list(request):
    object_list = PasswordModel.objects.all()

    context = {
        'list': object_list,
    }
    return render(request, 'app/list.html', context)


def password_detail(request, pk):
    context = {
        'obj': get_object_or_404(PasswordModel, id=pk),
    }
    return render(request, 'app/detail.html', context)


def password_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        username = request.POST['username']
        password = request.POST['password']

        PasswordModel.objects.create(title=title, username=username, password=password)
        return redirect('list')

    return render(request, 'app/create.html')


def password_edit(request, pk):
    obj = get_object_or_404(PasswordModel, id=pk)
    if request.method == 'POST':
        obj.title = request.POST['title']
        obj.username = request.POST['username']
        obj.password = request.POST['password']

        obj.save()
        return redirect('detail', pk=obj.id)

    context = {
        'obj': obj,
    }
    return render(request, 'app/create.html', context)


def password_delete(request, pk):
    obj = get_object_or_404(PasswordModel, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('list')

    context = {
        'obj': obj,
    }
    return render(request, 'app/confirm_delete.html', context)
