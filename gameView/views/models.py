from django.db import models

class FootballPlayer(models.Model):
    name = models.CharField(max_length = 100)
    student_id = models.IntegerField(db_index = True)
    position = models.ForeignKey(Position)
    height = models.IntegerField(blank = True, null = True)
    weight = models.IntegerFiedl(blan = True, null = True)
    birthdate = models.DateTimeField(blank = True, null = True)
    academy = models.ForeignKey(Academy)
    number = models.IntegerField()
    team = models.ForeignKey(Team)
    total_goal = models.IntegerField(default = 0)
    forbidden = models.BooleanField(default = False)

class Academy(models.Model):
    name = models.CharField(max_length = 100)

class Team(models.Model):
    name = models.CharField(max_length = 100)
    won = models.IntegerField(default = 0)
    even = models.IntegerField(default = 0)
    beaten = models.IntegerField(default = 0)
    goal = models.IntegerField(default = 0)
    lost = models.IntegerField(default = 0)
    point = models.IntegerField(defalt = 0)
    academy = models.ManyToManyField('Academy',related_name = 'teams')
    
    @property
    def net(self):
        return self.goal - self.lost

class Position(models.Model):
    name = models.CharField(max_length = 100)
