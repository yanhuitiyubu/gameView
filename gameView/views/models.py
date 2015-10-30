from django.db import models

class FootballPlayer(models.Model):
    name = models.CharField(max_length = 100)
    student_id = models.IntegerField(db_index = True)
    position = models.ForeignKey('Position',related_name = 'positions')
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    academy = models.ForeignKey('Academy',related_name = 'academys')
    number = models.IntegerField()
    team = models.ForeignKey('Team',related_name = 'teams')
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)

    def __unicode__(self):
        return u'{0} {1}'.format(self.student_id,self.name)


class Academy(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 100)
    won = models.IntegerField(default = 0)
    even = models.IntegerField(default = 0)
    beaten = models.IntegerField(default = 0)
    goal = models.IntegerField(default = 0)
    lost = models.IntegerField(default = 0)
    point = models.IntegerField(default = 0)
    academy = models.ManyToManyField('Academy',related_name = 'teams')
    

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
    goal_date = models.DateTimeField(db_index = True)
    goal_person = models.ForeignKey('FootballPlayer',related_name='goal_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.goal_date,self.goal_person.student_id,self.goal_person.name)

class YellowCard(models.Model):
    yellow_id = models.IntegerField()
    yellow_date = models.DateTimeField(db_index = True)
    yellow_person = models.ForeignKey('FootballPlayer',related_name='yellow_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.yellow_date,self.yellow_person.student_id,self.yellow_person.name)


class RedCard(models.Model):
    red_id = models.IntegerField()
    red_date = models.DateTimeField(db_index = True)
    red_person = models.ForeignKey('FootballPlayer',related_name='red_persons')

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.red_date,self.red_person.student_id,self.red_person.name)
    
    
