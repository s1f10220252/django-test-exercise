from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Moderate'),
        (3, 'Intermediate'),
        (4, 'Challenging'),
        (5, 'Difficult'),
    ]

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)
    task_memo = models.CharField(max_length=200, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)

    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt
