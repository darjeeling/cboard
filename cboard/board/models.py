from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    subject = models.CharField(max_length=255)
    contents = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.PROTECT)
    create_datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
    comment_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    class Meta:
        app_label = 'board'
