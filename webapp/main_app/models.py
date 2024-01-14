# models.py

from django.db import models

class WordPair(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    progress = models.IntegerField(default=5)
    # time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.word} - {self.translation} - {self.id}'
