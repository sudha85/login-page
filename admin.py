from django.contrib import admin

from loginapp.models import login
from loginapp.models import Register
from loginapp.models import ResetPassword




# Register your models here.
admin.site.register(login)
admin.site.register(Register)
admin.site.register(ResetPassword)


