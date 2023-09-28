from django.db import models
from users.models import CustomUser

class Todo(models.Model):
    Status_Choices = [
            ('C', 'Completed'),
            ('P', 'Pending'),
            ('S', 'Started'),
        ]

    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=1, choices=Status_Choices)
    ToDO_User=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title