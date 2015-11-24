# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from logging import getLogger

logger = getLogger("views_logger")

def index(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_home' : True,
    }
    return render_to_response(
        "views/index.html",
        args_data,
        context_instance=RequestContext(request)
    )
