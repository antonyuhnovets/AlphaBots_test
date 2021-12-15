import random

from django.db import models as md
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def generate_refer(self, referal_list):
        num = random.randint(10000000, 99999999)
        if str(num) in referal_list:
            self.generate_refer(referal_list)
        else:
            return num

    def _add_user(self, username, name, refer_id, **extra_fields):
        user = UserModel(
            username=username,
            name=name,
            refer_id=refer_id,
            **extra_fields,
        )
        self.user.save()

        return user


class UserModel(md.Model, UserManager):
    user_id = md.AutoField(
        primary_key=True,
    )
    name = md.CharField(
        max_length=80,
        verbose_name='Имя пользователя',
    )
    username = md.CharField(
        max_length=40,
        verbose_name='Логин пользователя',
    )
    refer_id = md.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999),
        ],
        verbose_name='Код реферальной ссылки',
    )

    objects = UserManager()

    def __str__(self):
        return f'Пользователь: {self.name} ID: {self.user_id}'

    @classmethod
    def referal_list(cls):
        return [str(x.__getattribute__('refer_id')) for x in cls.objects.all()]

    def add_user(self, username, name, *refer_id):
        if refer_id is None or False: refer_id = self.referal_list()
        self.generate_refer(refer_id)
        self._add_user(
            username=username,
            name=name,
            refer_id=refer_id,
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class MessageModel(md.Model):
    sender = md.ForeignKey(
        to=UserModel,
        verbose_name='Отправитель',
        on_delete=md.DO_NOTHING,
    )
    message_body = md.TextField(
        verbose_name='Текст сообщения'
    )
    created = md.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.message_body}\n\nОтправитель: {self.sender} \n{self.created}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
