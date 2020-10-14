from django.contrib import admin
from .models import Blog
from .models import User
from .models import Admin
from .models import QR_code
# Register your models here.
admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(QR_code)
