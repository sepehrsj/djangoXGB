from  rest_framework import serializers
from .models import PredictionLog

class FeatureSerializer(serializers.Serializer):
    Latitude = serializers.FloatField(required=True, allow_null=False)
    Longitude = serializers.FloatField(required=True, allow_null=False) 
    Gender = serializers.ChoiceField(choices=["male", "female"], required=True, allow_null=False)
    Senior_Citizen = serializers.ChoiceField(choices=["yes", "no"], required=True, allow_null=False)
    Partner = serializers.ChoiceField(choices=["yes", "no"], required=True, allow_null=False)
    Dependents = serializers.ChoiceField(choices=["yes", "no"], required=True, allow_null=False)
    
    Tenure_Months = serializers.IntegerField(min_value=0, required=True, allow_null=False)
    
    Phone_Service = serializers.ChoiceField(choices=["yes", "no"], required=True, allow_null=False)
    Multiple_Lines = serializers.ChoiceField(choices=["yes", "no", "no phone service"], required=True, allow_null=False)
    
    Internet_Service = serializers.ChoiceField(choices=["dsl", "fiber optic", "no"], required=True, allow_null=False)
    Online_Security = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    Online_Backup = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    Device_Protection = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    Tech_Support = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    Streaming_TV = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    Streaming_Movies = serializers.ChoiceField(choices=["yes", "no", "no internet service"], required=True, allow_null=False)
    
    Contract = serializers.ChoiceField(choices=["month-to-month", "one year", "two year"], required=True, allow_null=False)
    Paperless_Billing = serializers.ChoiceField(choices=["yes", "no"], required=True, allow_null=False)
    
    Payment_Method = serializers.ChoiceField(choices=[
        "electronic check", "mailed check", "bank transfer (automatic)", "credit card (automatic)"
    ], required=True, allow_null=False)
    
    Monthly_Charges = serializers.FloatField(min_value=0.0, required=True, allow_null=False)
    Total_Charges = serializers.FloatField(min_value=0.0, required=True, allow_null=True)

    

    def to_internal_value(self, data):
        new_data = data.copy()
        for key, value in new_data.items():
            if isinstance(value, str):
                new_data[key] = value.strip().lower()

        return super().to_internal_value(new_data)

        
class PredictionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionLog
        fields = ["input_data", "output_model", "created_time"]



