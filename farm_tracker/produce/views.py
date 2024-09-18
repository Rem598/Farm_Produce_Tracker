# Create your views here.
# produce/views.py
from django.shortcuts import render, redirect
from .forms import CropForm, YieldForm, SaleForm
from .models import Crop, Yield, Sale
from django.contrib.auth import authenticate, login,logout
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    crop_form = CropForm()
    yield_form = YieldForm()
    sale_form = SaleForm()

    # Handling form submission
    if request.method == 'POST':
        if 'add_crop' in request.POST:
            crop_form = CropForm(request.POST)
            if crop_form.is_valid():
                crop_form.save()
                return redirect('dashboard')
        elif 'add_yield' in request.POST:
            yield_form = YieldForm(request.POST)
            if yield_form.is_valid():
                yield_form.save()
                return redirect('dashboard')
        elif 'add_sale' in request.POST:
            sale_form = SaleForm(request.POST)
            if sale_form.is_valid():
                
                sale_form.save()
                return redirect('dashboard')
            
            
    # Fetch all crops, yields, and sales data
    crops = Crop.objects.all()
    yields = Yield.objects.all()
    sales = Sale.objects.all()

    # Debugging statements
    print("Crops:", crops)
    print("Yields:", yields)
    print("Sales:", sales)
  
     

    # Create summary data
    crop_summary = []
    for crop in crops:
        total_yield = yields.filter(crop=crop).aggregate(Sum('amount'))['amount__sum'] or 0
        total_sales = sales.filter(crop=crop).aggregate(Sum('revenue'))['revenue__sum'] or 0
        crop_summary.append({
            'name': crop.name,
            'total_yield': total_yield,
            'total_sales': total_sales
        })

    context = {
        'crop_summary': crop_summary,
        'crop_form': crop_form,
        'yield_form': yield_form,
        'sale_form': sale_form,
    }
    return render(request, 'produce/dashboard.html', context)

    

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'produce/login.html', {'form': form})




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'produce/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'produce/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'produce/index.html')