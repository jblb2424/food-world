
from django.contrib import admin
from .models import User, Snack, Wishlist, Cart, Authenticator, Reccomendation
# Register your models here.

admin.site.register(User)
admin.site.register(Snack)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Authenticator)
admin.site.register(Reccomendation)