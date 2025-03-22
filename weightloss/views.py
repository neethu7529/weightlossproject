from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddWeightForm
from .models import WeightRegister
from django.core.paginator import Paginator
from datetime import date
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
@login_required
def weightloss(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about-us.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            auth_login(request, user) 
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    return render(request, 'logout.html', {'user': request.user})

@login_required
def addWeight(request):
    today = date.today()
    existing_entry = WeightRegister.objects.filter(user=request.user, date=today).first()
    if request.method == 'POST':
        form = AddWeightForm(request.POST)
        if form.is_valid():
            if existing_entry:
                return render(request, 'addweight.html', {
                    'form': form,
                    'error': 'You have already added your weight for today.'
                })
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.date = today
            weight_entry.save()
            return render(request, 'success.html', {'success': 'Your weight was added successfully'})
    else:
        form = AddWeightForm()
    return render(request, 'addweight.html', {'form': form, 'error': existing_entry and 'You have already added your weight for today.'})

@login_required
def addedWeight(request):
    weight_list = WeightRegister.objects.filter(user=request.user)
    return render(request, 'retrieve.html', {'weight_list': weight_list})

@login_required
def weight_update(request, pk):
    weight = get_object_or_404(WeightRegister, pk=pk)
    
    if request.method == 'POST':
        form = AddWeightForm(request.POST, instance=weight)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddWeightForm(instance=weight)
    
    return render(request, 'update.html', {'form': form})

@login_required
def weight_delete(request, pk):
    weight = get_object_or_404(WeightRegister, pk=pk)
    if request.method == 'POST':
        weight.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {'weight': weight})

@login_required
def weight_list(request):
    weight_entries = WeightRegister.objects.filter(user=request.user)
    paginator = Paginator(weight_entries, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weight_list.html', {'page_obj': page_obj})

@login_required
def weight_loss_calculator(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        print(f"Start Date: {start_date}")  
        print(f"End Date: {end_date}")     

        try:
            start_weight = WeightRegister.objects.get(user=request.user, date=start_date)
            end_weight = WeightRegister.objects.get(user=request.user, date=end_date)

            weight_loss = start_weight.weight - end_weight.weight
            return JsonResponse({'weight_loss': weight_loss})
        except WeightRegister.DoesNotExist:
            return JsonResponse({'error': 'Weight data not available for the selected dates'}, status=400)

    return render(request, 'weight_loss_calculator.html')
