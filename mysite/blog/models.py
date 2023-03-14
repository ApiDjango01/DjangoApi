from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    com_date = models.DateTimeField('date published')

