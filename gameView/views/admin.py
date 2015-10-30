# -*- coding:utf-8 -*-

from django.contrib import admin
import models

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('student_id','name')
    list_filter = ('team__name',)
    ordering = ('team__name',)
    list_per_page = 50

    def queryset(self,request):
        qs = super(PlayerAdmin,self).queryset(request)
        return qs.only('student_id','team__name')
admin.site.register(models.FootballPlayer, PlayerAdmin)

class AcademyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(AcademyAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Academy, AcademyAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(TeamAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Team, TeamAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def queyset(self,request):
        qs = super(PositionAdmin,self).queryset(request)
        return qs.only('name')
admin.site.register(models.Position, PositionAdmin)

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_person',)
    
    def queyset(self,request):
        qs = super(GoalAdmin,self).queryset(request)
        return qs.only('goal_person')
admin.site.register(models.Goal, GoalAdmin)

class YellowAdmin(admin.ModelAdmin):
    list_display = ('yellow_person',)
    
    def queyset(self,request):
        qs = super(YellowAdmin,self).queryset(request)
        return qs.only('yellow_person')
admin.site.register(models.YellowCard, YellowAdmin)

class RedAdmin(admin.ModelAdmin):
    list_display = ('red_person',)
    
    def queyset(self,request):
        qs = super(RedAdmin,self).queryset(request)
        return qs.only('red_person')
admin.site.register(models.RedCard, RedAdmin)
