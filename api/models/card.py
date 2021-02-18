from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Card(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  notes = models.CharField(max_length=100)
  status = models.CharField(max_length=20)
  owner = models.ForeignKey(
      get_user_model(),
      related_name='cards',
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The kanban card for '{self.notes}' is currently {self.status}."

  def as_dict(self):
    """Returns dictionary version of Card models"""
    return {
        'id': self.id,
        'notes': self.notes,
        'status': self.status
    }
