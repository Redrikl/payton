from django.shortcuts import render, redirect, get_object_or_404
from .models import Software
from .forms import SoftwareForm

def software_list(request):
    softwares = Software.objects.all()
    return render(request, 'software_list.html', {'softwares': softwares})
def home(request):
    softwares = Software.objects.all()  # Извлекаем все записи из модели Software
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую запись в базе данных
            return redirect('home')  # Перенаправляем обратно на главную страницу
    else:
        form = SoftwareForm()  # Пустая форма для GET-запроса

    return render(request, 'home.html', {'softwares': softwares, 'form': form})
def software_detail(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    return render(request, 'software_detail.html', {'software': software})
def software_edit(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('software_detail', software_id=software.id)  # Перенаправляем на страницу с детальной информацией
    else:
        form = SoftwareForm(instance=software)  # Заполняем форму текущими данными записи

    return render(request, 'software_edit.html', {'form': form, 'software': software})