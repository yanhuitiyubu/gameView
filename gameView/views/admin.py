# -*- coding:utf-8 -*-

from django.contrib import admin
import models

class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_A','team_B','result')
    ordering = ('team_A',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(MatchAdmin,self).queryset(request)
        return qs.only('team_A','team_B','result')
admin.site.register(models.Match, MatchAdmin)

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_person',)
    
    def queyset(self,request):
        qs = super(GoalAdmin,self).queryset(request)
        return qs.only('goal_person')
admin.site.register(models.Goal, GoalAdmin)

class RedAdmin(admin.ModelAdmin):
    list_display = ('red_person',)
    
    def queyset(self,request):
        qs = super(RedAdmin,self).queryset(request)
        return qs.only('red_person')
admin.site.register(models.RedCard, RedAdmin)

class YellowAdmin(admin.ModelAdmin):
    list_display = ('yellow_person',)
    
    def queyset(self,request):
        qs = super(YellowAdmin,self).queryset(request)
        return qs.only('yellow_person')
admin.site.register(models.YellowCard, YellowAdmin)

class FoulAdmin(admin.ModelAdmin):
    list_display = ('foul_person',)
    
    def queyset(self,request):
        qs = super(FoulAdmin,self).queryset(request)
        return qs.only('foul_person')
admin.site.register(models.Foul, FoulAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(TeamAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('student_id','name')
    list_filter = ('academy__name',)
    ordering = ('academy__name',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(PlayerAdmin,self).queryset(request)
        return qs.only('student_id','name','academy__name')
admin.site.register(models.Player, PlayerAdmin)


class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_filter = ('team__name',)
    ordering = ('team__name',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(FootballPlayerAdmin,self).queryset(request)
        return qs.only('team__name','number')
admin.site.register(models.FootballPlayer, FootballPlayerAdmin)

class BasketballPlayerAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_filter = ('team__name',)
    ordering = ('team__name',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(BasketballPlayerAdmin,self).queryset(request)
        return qs.only('player__student_id','player__name','team__name','number')
admin.site.register(models.BasketballPlayer, BasketballPlayerAdmin)

class LeaderAdmin(admin.ModelAdmin):
    list_display = ('student_id','name')
    list_filter = ('team__name',)
    ordering = ('team__name',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(LeaderAdmin,self).queryset(request)
        return qs.only('student_id','name','team__name')
admin.site.register(models.Leader, LeaderAdmin)

#class FootballPlayerAdmin(admin.ModelAdmin):
#    list_display = ('player__student_id','player__name','team__name','number')
#    list_filter = ('team__name',)
#    ordering = ('team__name',)
#    list_per_page = 50
#
#    def queryset(self,request):
#        qs = super(FootballPlayerAdmin,self).queryset(request)
#        return qs.only('player__student_id','player__name','team__name','number')
#admin.site.register(models.FootballPlayer, FootballAdmin)
#
#class BasketballPlayerAdmin(admin.ModelAdmin):
#    list_display = ('player__student_id','player__name','team__name','number')
#    list_filter = ('team__name',)
#    ordering = ('team__name',)
#    list_per_page = 50
#
#    def queryset(self,request):
#        qs = super(BasketballPlayerAdmin,self).queryset(request)
#        return qs.only('player__student_id','player__name','team__name','number')
#admin.site.register(models.BasketballPlayer, BasketballAdmin)

class AcademyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(AcademyAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Academy, AcademyAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def queyset(self,request):
        qs = super(NewsAdmin,self).queryset(request)
        return qs.only('title')
admin.site.register(models.News, NewsAdmin)

class TeamPrizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(TeamPrizeAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.TeamPrize, TeamPrizeAdmin)

class PlayerPrizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(PlayerPrizeAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.PlayerPrize, PlayerPrizeAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(PositionAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Position, PositionAdmin)

class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(NewsTypeAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.NewsType, NewsTypeAdmin)

class MatchTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(MatchTypeAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.MatchType, MatchTypeAdmin)

class BallTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(BallTypeAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.BallType, BallTypeAdmin)

