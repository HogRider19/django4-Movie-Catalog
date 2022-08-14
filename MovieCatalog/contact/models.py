from django.db import models


class Contact(models.Model):
    """Модель подписки по email"""
    email = models.EmailField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
