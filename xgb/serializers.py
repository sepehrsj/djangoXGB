from  rest_framework import serializers 


class FeatureSerializer(serializers.Serializer):
    Latitude = serializers.FloatField()
    Longitude = serializers.FloatField() 
    Gender = serializers.ChoiceField(choices=["male", "female"])
    Senior_Citizen = serializers.ChoiceField(choices=["yes", "no"])
    Partner = serializers.ChoiceField(choices=["yes", "no"])
    Dependents = serializers.ChoiceField(choices=["yes", "no"])
    
    Tenure_Months = serializers.IntegerField(min_value=0)
    
    Phone_Service = serializers.ChoiceField(choices=["yes", "no"])
    Multiple_Lines = serializers.ChoiceField(choices=["yes", "no", "no phone service"])
    
    Internet_Service = serializers.ChoiceField(choices=["dsl", "fiber optic", "no"])
    Online_Security = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    Online_Backup = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    Device_Protection = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    Tech_Support = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    Streaming_TV = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    Streaming_Movies = serializers.ChoiceField(choices=["yes", "no", "no internet service"])
    
    Contract = serializers.ChoiceField(choices=["month-to-month", "one year", "two year"])
    Paperless_Billing = serializers.ChoiceField(choices=["yes", "no"])
    
    Payment_Method = serializers.ChoiceField(choices=[
        "electronic check", "mailed check", "bank transfer (automatic)", "credit card (automatic)"
    ])
    
    Monthly_Charges = serializers.FloatField(min_value=0.0)
    Total_Charges = serializers.FloatField(min_value=0.0)
    

    def to_internal_value(self, data):
        new_data = data.copy()
        for key, value in new_data.items():
            if isinstance(value, str):
                new_data[key] = value.strip().lower()

        return super().to_internal_value(new_data)

        
    
        





