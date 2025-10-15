from django.db import models

class OnCount(models.Model):
    # count = models.AutoField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at
