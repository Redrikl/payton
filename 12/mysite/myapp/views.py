from django.shortcuts import render, redirect
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