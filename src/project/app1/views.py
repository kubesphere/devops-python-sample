# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.


def home(request):
    resp = HttpResponse()
    resp.write("<h1 style='text-align:center;'>Hello, Django!</h1>")
    return resp
