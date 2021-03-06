from django.db import models

class Clan_Meta_Data(models.Model):
    coins = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    name = models.CharField(max_length=40, default="")
    members = []

    def __str__(self):
        return self.name

    def member_count(self):
        return len(self.members)


# Create your models here.
