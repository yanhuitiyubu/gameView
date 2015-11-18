from django.db import models

class Match(models.Model):
    result = models.CharField(max_length = 100)
    time = models.DateTimeField()
    match_type = models.ForeignKey('MatchType', related_name = 'matchtypes')
    ball_type = models.ForeignKey('BallType', related_name = 'balltypes')
    status = models.BooleanField(default = False)
    team_A = models.ForeignKey('Team', related_name = 'Teams')
    team_B = models.ForeignKey('Team', related_name = 'Teams')
    news = models.ForeignKey('News', related_name = 'Newses')
    starting = models.TextField()
    substitution = models.TextField()

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.time,self.team_A,self.team_B)

class News(models.Model):
    title = models.CharField(max_length = 500)
    content = models.TextField()
    news_type = models.ForeignKey('NewsType', related_name = 'NewsTypes')
    image = models.ImageField()

    def _unicode__(self):
        return self.title

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

class Player(models.Model):
    name = models.CharField(max_length = 100)
    profile = models.ImageField()
    student_id = models.IntegerField(db_index = True)
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    academy = models.ForeignKey('Academy',related_name = 'academys')
    grade = models.ForeignKey('Grade', related_name = 'grades')
    des = models.TextField()
    prize = models.ForeignKey('PlayerPrize', related_name = 'playerprizes')

    def __unicode__(self):
        return u'{0} {1}'.format(self.student_id,self.name)

class FootballPlayer(models.Model):
    player = models.ForeighKey('Player','players')
    team = models.ForeighKey('Team', 'teams')
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)
    number = models.IntegerField()
    position = models.ForeignKey('Position',related_name = 'positions')
    on_stage_num = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.player

class BasketballPlayer(models.Model):
    player = models.ForeighKey('Player','players')
    team = models.ForeighKey('Team', 'teams')
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)
    number = models.IntegerField()
    position = models.ForeignKey('Position',related_name = 'positions')
    on_stage_num = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.player

class Grade(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Leader(models.Model):
    name = models.CharField(max_length = 100)
    profile = models.ImageField()
    student_id = models.IntegerField(db_index = True)
    position = models.ForeignKey('Position',related_name = 'positions')
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    academy = models.ForeignKey('Academy',related_name = 'academys')
    number = models.IntegerField()
    team = models.ForeignKey('Team',related_name = 'teams')

    def __unicode__(self):
        return u'{0} {1}'.format(self.student_id,self.name)

class Academy(models.Model):
    name = models.CharField(max_length = 100)
    team = models.ForeignKey('Team', related_name = 'teams')

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 100)
    year = models.IntegerField(max_length = 100)
    profile = models.ImageField()
    won = models.IntegerField(default = 0)
    even = models.IntegerField(default = 0)
    beaten = models.IntegerField(default = 0)
    captain = models.ForeignKey('Player', related_name = 'players')
    leader = models.ForeignKey('Leader', related_name = 'leaders')
    team_type = models.ForeignKey('BallType', related_name = 'balltypes')
    goal = models.IntegerField(default = 0)
    lost = models.IntegerField(default = 0)
    point = models.IntegerField(default = 0)
    #academy = models.ManyToManyField('Academy',related_name = 'teams')
    prize = models.ForeignKey('TeamPrize', related_name = 'teamprizes')

    def __unicode__(self):
        return self.name

    @property
    def net(self):
        return self.goal - self.lost

class Position(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Goal(models.Model):
    goal_id = models.IntegerField()
    goal_match = models.ForeignKey('Match', related_name = 'matches')
    goal_person = models.ForeignKey('Player',related_name='goal_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.goal_match,self.goal_person.student_id,self.goal_person.name)

class YellowCard(models.Model):
    yellow_id = models.IntegerField()
    yellow_match = models.ForeignKey('Match', related_name = 'matches')
    yellow_person = models.ForeignKey('Player',related_name='yellow_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.yellow_match,self.yellow_person.student_id,self.yellow_person.name)


class RedCard(models.Model):
    red_id = models.IntegerField()
    red_match = models.ForeignKey('Match', related_name = 'matches')
    red_person = models.ForeignKey('Player',related_name='red_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.red_match,self.red_person.student_id,self.red_person.name)
class Foul(models.Model):
    foul_id = models.IntegerField()
    foul_match = models.ForeignKey('Match', related_name = 'matches')
    foul_person = models.ForeignKey('Player',related_name='red_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.foul_match,self.foul_person.student_id,foul.red_person.name)

class TeamPrize(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        retrun self.name

class PlayerPrize(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        retrun self.name
