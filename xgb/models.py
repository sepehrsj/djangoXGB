from django.db import models

# Create your models here.

class PredictionLog(models.Model):
    input_data = models.JSONField()
    output_model = models.JSONField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"created at: {self.created_time}"

