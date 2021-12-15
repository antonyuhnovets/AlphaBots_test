from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView

from . import models as md

REFERAL_LIST = md.UserModel.referal_list()


class LinkHandler(FormView):
    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='index.html',
        )

    def post(self, request, *args, **kwargs):
        input_refer = str(request.POST['text'])
        if input_refer in REFERAL_LIST:
            url = f'https://t.me/alphabots_testbot?start={input_refer}'
            return redirect(
                to=url,
            )
        else:
            return render(
                request=request,
                template_name='referal_error.html',
                context={'refers': REFERAL_LIST},
            )

# class MessageHandler(CreateView):
#     def post(self, request, *args, **kwargs):
