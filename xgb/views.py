import pandas as pd
import xgboost as xgb
import joblib
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeatureSerializer, PredictionLogSerializer
from utilities.transformer import CustomTransformer
from rest_framework import status
import logging


logger = logging.getLogger('xgb')

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
    def get(self, request):
        logger.info("GET request received for prediction endpoint.")
        return Response({"message": "Send a POST request with features to get a prediction."}, status=status.HTTP_200_OK)

    def post(self, request):
        is_many = isinstance(request.data, list)
        logger.info(f"Received incoming POST prediction request. Batch mode: {is_many}")

        serializer = FeatureSerializer(data=request.data, many=is_many)

        if serializer.is_valid():
            try:
                df = pd.DataFrame(serializer.validated_data if is_many else [serializer.validated_data])
                prediction = xgboost.predict(df)
                prediction_list = prediction.tolist()

                log_data = {
                        "input_data": request.data,
                        "output_model": prediction_list  
                    }
                
                log_serializer = PredictionLogSerializer(data=log_data)
                if log_serializer.is_valid():
                    log_serializer.save()
            
                logger.info("Prediction pipeline executed successfully.")
                return Response({"prediction": prediction}, status=status.HTTP_200_OK)

            except Exception as e:
                logger.error(f"Critical error during model inference: {str(e)}", exc_info=True)
                return Response({"error": "Internal processing error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.warning(f"Validation failed for incoming payload: {serializer.errors}")
        return Response({"message": "data is not valid", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)