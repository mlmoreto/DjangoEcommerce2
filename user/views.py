from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def show_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            pass
        else:
            dic = {'form': form}
            return render(request, 'testeForm.html', dic)
    else:
        form = UserForm()
        dic = {'form': form}
        return render(request, 'testeForm.html', dic)