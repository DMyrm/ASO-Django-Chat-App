from django.contrib import admin

# Register your models here.
from chatrooms.models import Room, Message, User

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(User)
