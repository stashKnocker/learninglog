from django.db import models

# Create your models here.
class Topic(models.Model):
    """info about topic."""
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """represent as string."""
        return self.text

class Entry(models.Model):
    """info about entry."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """represent as strings."""
        if self.text >= self.text[:50]:
            return self.text[:50] + "..."
        else:
            return self.text
    