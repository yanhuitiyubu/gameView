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

def news(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_news' : True,
    }
    return render_to_response(
        "views/news.html",
        args_data,
        context_instance=RequestContext(request)
    )

def schedule(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_schedule' : True,
    }
    return render_to_response(
        "views/schedule.html",
        args_data,
        context_instance=RequestContext(request)
    )

def basketball_info(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_basketball_info' : True,
    }
    return render_to_response(
        "views/teamlist_bas.html",
        args_data,
        context_instance=RequestContext(request)
    )

def football_info(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_football_info' : True,
    }
    return render_to_response(
        "views/teamlist_soc.html",
        args_data,
        context_instance=RequestContext(request)
    )

def basketball_rank(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_basketball_rank' : True,
    }
    return render_to_response(
        "views/rank_bas.html",
        args_data,
        context_instance=RequestContext(request)
    )

def football_rank(request):
    """
    Home page of gameview
    """
    args_data = {
    'cv_football_rank' : True,
    }
    return render_to_response(
        "views/rank_soc.html",
        args_data,
        context_instance=RequestContext(request)
    )
