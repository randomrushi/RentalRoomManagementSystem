from django.contrib import admin

# Register your models here.
from .models import Tenent
admin.site.register(Tenent)

from .models import Owner
admin.site.register(Owner)

from .models import Property
admin.site.register(Property)
