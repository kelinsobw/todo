from django.db import models
from threading import current_thread


class Note(models.Model):
   title = models.CharField(max_length=50)
   text = models.TextField()
   created_at = models.DateTimeField(
       auto_now_add=True, db_index=True
   )