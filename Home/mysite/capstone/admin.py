from django.contrib import admin

from .models import Question
from .models import Post

admin.site.register(Post)
admin.site.register(Question)
# Register your models here.
