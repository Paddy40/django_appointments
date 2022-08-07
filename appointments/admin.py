from django.contrib import admin
from .models import Doctable
from .models import Patienttable
from .models import Appointmenttable
from .models import Logintable
from .models import Querytable

# Register your models here.

admin.site.register(Doctable)
admin.site.register(Patienttable)
admin.site.register(Appointmenttable)
admin.site.register(Logintable)
admin.site.register(Querytable)