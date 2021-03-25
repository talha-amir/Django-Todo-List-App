from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(("Title"), max_length=50)
    description = models.TextField(("Description"),null=True)
    complete = models.BooleanField(("Completed"),default=False)
    create =models.DateTimeField(("Created On"),  auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']