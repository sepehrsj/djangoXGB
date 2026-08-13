import pandas as pd
import xgboost as xgb
import joblib
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeatureSerializer
from utilities.transformer import CustomTransformer



# Create your views here.
expected_columns = [
    'Latitude', 'Longitude', 'Tenure_Months', 'Monthly_Charges', 'Total_Charges', 
    'Gender', 'Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 
    'Multiple_Lines', 'Contract', 'Internet_Service', 'Payment_Method', 
    'Online_Security', 'Online_Backup', 'Device_Protection', 'Tech_Support', 
    'Streaming_TV', 'Streaming_Movies', 'Paperless_Billing'
]

xgboost = joblib.load("best_telco_model.joblib")["model"]


class PublicPredView(APIView):
    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = FeatureSerializer(data=request.data, many=is_many)
        if serializer.is_valid():
            df = pd.DataFrame(serializer.validated_data if is_many else list(serializer.validated_data))
            prediction = xgboost.predict(df)
            return Response({"prediction": prediction.tolist()}, status=200)
    
        return Response({"message": "data is not valid"}, status=400)


    def get(self, request):
        return Response({
            "message": "fill the values",
            "features": {
                "Latitude": "",
                "Longitude": "",
                "Gender": "",
                "Senior_Citizen": "",
                "Partner": "",
                "Dependents": "",
                "Tenure_Months": "",
                "Phone_Service": "",
                "Multiple_Lines": "",
                "Internet_Service": "",
                "Online_Security": "",
                "Online_Backup": "",
                "Device_Protection": "",
                "Tech_Support": "",
                "Streaming_TV": "",
                "Streaming_Movies": "",
                "Contract": "category",
                "Paperless_Billing": "",
                "Payment_Method": "",
                "Monthly_Charges": "",
                "Total_Charges": "",
            }
        })