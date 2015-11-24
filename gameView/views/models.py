# -*- coding:utf-8 -*-
from django.db import models

class Match(models.Model):
    result = models.CharField(max_length = 100)
    time = models.DateTimeField()
    match_type = models.ForeignKey('MatchType')
    ball_type = models.ForeignKey('BallType')
    status = models.BooleanField(default = False)    #是否开赛
    team_A = models.ForeignKey('Team', related_name = 'matches_A')
    team_B = models.ForeignKey('Team', related_name = 'matches_B')
    news = models.ForeignKey('News')    #战报
    starting = models.TextField()    #首发
    substitution = models.TextField()    #换人

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.time,self.team_A,self.team_B)

class Goal(models.Model):
    goal_id = models.IntegerField()
    goal_match = models.ForeignKey('Match', related_name = 'goals')
    goal_person = models.ForeignKey('Player',related_name='goals')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.goal_match,self.goal_person.student_id,self.goal_person.name)

class RedCard(models.Model):
    red_id = models.IntegerField()
    red_match = models.ForeignKey('Match')
    red_person = models.ForeignKey('Player')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.red_match,self.red_person.student_id,self.red_person.name)

class YellowCard(models.Model):
    yellow_id = models.IntegerField()
    yellow_match = models.ForeignKey('Match')
    yellow_person = models.ForeignKey('Player')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.yellow_match,self.yellow_person.student_id,self.yellow_person.name)

class Foul(models.Model):
    foul_id = models.IntegerField()
    foul_match = models.ForeignKey('Match', related_name = 'fouls')
    foul_person = models.ForeignKey('Player',related_name='fouls')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.foul_match,self.foul_person.student_id,foul.red_person.name)

class Team(models.Model):
    name = models.CharField(max_length = 100)
    year = models.IntegerField(max_length = 100)
    profile = models.ImageField(upload_to = 'images')
    won = models.IntegerField(default = 0)
    even = models.IntegerField(default = 0)
    beaten = models.IntegerField(default = 0)
    captain = models.ForeignKey('Player', related_name = 'teams')
    leader = models.ForeignKey('Leader', related_name = 'teams')
    team_type = models.ForeignKey('BallType', related_name = 'teams')
    goal = models.IntegerField(default = 0)
    lost = models.IntegerField(default = 0)
    point = models.IntegerField(default = 0)
    #academy = models.ManyToManyField('Academy',related_name = 'teams')
    prize = models.ForeignKey('TeamPrize', related_name = 'teams')

    def __unicode__(self):
        return self.name

    @property
    def net(self):
        return self.goal - self.lost

class Player(models.Model):
    name = models.CharField(max_length = 100)
    profile = models.ImageField(upload_to = 'images')
    student_id = models.IntegerField(default = 0)
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    academy = models.ForeignKey('Academy',related_name = 'players')
    grade = models.ForeignKey('Grade', related_name = 'players')
    des = models.TextField()
    prize = models.ForeignKey('PlayerPrize', related_name = 'players')

    def __unicode__(self):
        return u'{0} {1}'.format(self.student_id,self.name)

class FootballPlayer(models.Model):
    player = models.ForeignKey('Player',related_name = 'footballplayers')
    team = models.ForeignKey('Team', related_name = 'footballplayers')
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)
    number = models.IntegerField()
    position = models.ForeignKey('Position',related_name = 'footballplayers')
    on_stage_num = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.player

class BasketballPlayer(models.Model):
    player = models.ForeignKey('Player',related_name = 'basketballplayers')
    team = models.ForeignKey('Team', related_name = 'basketballplayers')
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)
    number = models.IntegerField()
    position = models.ForeignKey('Position',related_name = 'basketballpalyers')
    on_stage_num = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.player

class Grade(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Leader(models.Model):    #领队信息
    name = models.CharField(max_length = 100)
    profile = models.ImageField(upload_to = 'images')
    student_id = models.IntegerField(db_index = True)
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    number = models.IntegerField()
    team = models.ForeignKey('Team',related_name = 'leaders')

    def __unicode__(self):
        return u'{0} {1}'.format(self.student_id,self.name)

class Academy(models.Model):
    name = models.CharField(max_length = 100)
    team = models.ForeignKey('Team', related_name = 'academys')

    def __unicode__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length = 500)
    content = models.TextField()
    news_type = models.ForeignKey('NewsType', related_name = 'newses')
    image = models.ImageField(upload_to = 'images')

    def _unicode__(self):
        return self.title

class TeamPrize(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class PlayerPrize(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class NewsType(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class MatchType(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class BallType(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

