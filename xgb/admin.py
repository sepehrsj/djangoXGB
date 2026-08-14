from django.contrib import admin
from .models import PredictionLog

# Register your models here.
@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ("id", "created_time")
    list_filter = ("created_time",)
    readonly_fields = ("created_time", "input_data", "output_model")

    fieldsets = [
        (
            "data_info",
            {
                "fields": ["input_data", "output_model"],
            },
        ),
        (
            "data and time",
            {
                "fields": ["created_time"]
            })
        
        ]
        
    

