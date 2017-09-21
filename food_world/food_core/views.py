from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User, Snack, Wishlist, Cart
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def getUsers(request, pk):
	print(pk)
	user = User.objects.get(pk = pk)
	first_name = user.first_name
	last_name = user.last_name
	email  = user.email
	phone_number = user.phone_number

	return JsonResponse({'First Name': first_name, "Last Name": last_name, "email": email, "Phone Number": phone_number})

def getSnacks(request, pk):
	snack = models.Snack.objects.get(pk = pk)
	name = snack.name
	description = snack.description
	price = snack.price
	nutrition_info = snack.nutrition_info
	return JsonResponse({"Name": name, "Description": description, "Price": price, "Nutrition Info": nutrition_info})

def getCarts(request):
	cart = models.Cart.objects.get(pk = pk)
	user = cart.user
	total_price = cart.total_price
	num_items = cart.num_items
	return JsonResponse({"User": user, "Total Price": total_price, "Number of Items": num_items})

def getWishlist(request, pk):
	wishlist = models.Wishlist.objects.get(pk = pk)
	user = wishlist.user
	total_price = wishlist.total_price
	num_items = wishlist.num_items
	return JsonResponse({"User": user, "Total Price": total_price, "Number of Items": num_items})


@csrf_exempt
def createUser(request):
	first_name = request.POST.get("First Name", "No First Name Provided")
	last_name = equest.POST.get("Last Name", "No Last Name Provided")
	email  = request.POST.get("Email", "No Email Provided")
	phone_number = request.POST.get("Phone Number", "No Phone Number Provided")
	new_user = User(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number)
	new_user.save()

@csrf_exempt
def createSnack(request):
	name = request.POST.get("Name", "No Name Provided")
	description  = request.POST.get("Description", "No Description Provided")
	price = request.POST.get("Price", 0.00)
	nutrition_info = request.POST.get("Nutrition Info","No Nutrition Info Provided")
	new_snack = Snack(name = name, description = description, price = price, nutrition_info = nutrition_info)
	try:
		new_snack.save()
		return JsonResponse({"Status Code": "200", "NameTest": request.POST})
	except:
		return JsonResponse({"Status Code": "500"})


@csrf_exempt
def createCart(request):
	user = request.POST.get("User", "No user Provided")
	total_price = request.POST.get("Total Price", 0.00)
	num_items  = request.POST.get("Num Items", "No Description Provided")
	
	new_cart = Cart(user = user, total_price = total_price, num_items = num_items)
	try:
		new_cart.save()
		return JsonResponse({"Status Code": "200", "NameTest": request.POST})
	except:
		return JsonResponse({"Status Code": "500"})


@csrf_exempt
def createWishlist(request):
	user = request.POST.get("User", "No user Provided")
	total_price = request.POST.get("Total Price", 0.00)
	num_items  = request.POST.get("Num Items", "No Description Provided")
	
	new_wishlist = Wishlist(user = user, total_price = total_price, num_items = num_items)
	try:
		new_wishlist.save()
		return JsonResponse({"Status Code": "200", "NameTest": request.POST})
	except:
		return JsonResponse({"Status Code": "500"})
