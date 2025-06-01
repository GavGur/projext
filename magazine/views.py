from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Client, Product
def index(request):
    return render(request, 'index2.html')

def test(request):
    return render(request, 'stest.html')

def test_second(request):
    products = Product.objects.all()

    return render(request, 'test.html', {'products': products})

@csrf_exempt
def vhod(request):
    return render(request, 'index3.html')

@csrf_exempt
def cykagdeuron(request):
    return render(request, 'index.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = Client(login=username, password=password)
        user.save()
        return render(request, 'index3.html')
    else:
        return render(request, 'index.html')

@csrf_exempt
def vhod(request):
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        try:
            user = Client.objects.get(login=username, password=password)
            # Если пользователь найден - вход успешен
            return render(request, 'index2.html', {'username': username})
        except Client.DoesNotExist:
            # Если пользователь не найден или пароль неверный
            return render(request, 'index3.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'index3.html')
