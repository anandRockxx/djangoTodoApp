from django.db import models

# Create your models here.
class list(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item + ' | ' + str(self.completed)