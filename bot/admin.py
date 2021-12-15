from django.contrib import admin
from .models import UserModel, MessageModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'refer_id', 'user_id')
    fields = ('username', 'name', 'refer_id')


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message_body', 'pk', 'created')
    fields = ('sender', 'message_body', 'pk', 'created')


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(MessageModel, MessageModelAdmin)
