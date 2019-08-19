from django.db import models


class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry #{self.id}| Date: {self.date_posted}"

    class Meta:
        verbose_name_plural = 'entries'
