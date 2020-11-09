from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from foodtaskerapp.forms import RestaurantForm, UserForm
from foodtaskerapp.models import Restaurant

# Create your views here.
def Home(request):
    bgclr="#d5dbdb"
    return render(request,'foodtaskerapp/home.html', {"bgclr": bgclr})

#@login_required(login_url='/example url you want redirect/')


class UserLogin(LoginView):
    template_name = 'restaurant/loginview_form.html'

def UserLogout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

def RestaurantSignup(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect('restaurant_home')

    return render(request, "restaurant/sign_up.html", {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })


@login_required (login_url='login_form')
def RestaurantHp(request):
    bgclr="#fff808"
    list_restaurants=Restaurant.objects.all()
    return render(request, 'restaurant/homepage.html', {"list_restaurants":list_restaurants, "bgclr":bgclr})
