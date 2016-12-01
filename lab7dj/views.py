from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.





def registration (request):
    errors =[]
    errors.append(request.method)
    if request.method=='POST':
        errors.append(0)
        username=request.POST.get('username')
        if not username:
            errors.append(' Введите логин ')
        elif len(username)<5:
            errors.append(' Логин должен привышать 5 символов ')
            password = request.POST.get('password')
        if not password:
            errors.append(' Введите пароль ')
        elif len(password)<6:
            errors.append(' Длинна пароля должна превышать 6 символов')
            password_repeat = request.POST.get('password2')
        if password!=password_repeat:
            errors.append(' Пароли должны совпадать ')
        if not errors:
             return render(request, 'login_1.html')
    return render(request,'login_1.html',{'errors': errors})








class enter(View):
    def get (self,request):

        return render(request,"Enter.html")

