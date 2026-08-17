import pytest
from django.urls import reverse
import json
from .serializers import FeatureSerializer

ALL_FEATURES = [
    "Latitude", "Longitude", "Gender", "Senior_Citizen", "Partner", 
    "Dependents", "Tenure_Months", "Phone_Service", "Multiple_Lines", 
    "Internet_Service", "Online_Security", "Online_Backup", "Device_Protection", 
    "Tech_Support", "Streaming_TV", "Streaming_Movies", "Contract", 
    "Paperless_Billing", "Payment_Method", "Monthly_Charges", "Total_Charges"
]

VALID_PAYLOAD = {
    "Latitude": "39.578792",
    "Longitude": "-120.780786",
    "Gender": "male",
    "Senior_Citizen": "no",
    "Partner": "yes",
    "Dependents": "yes",
    "Tenure_Months": "72",
    "Phone_Service": "yes",
    "Multiple_Lines": "yes",
    "Internet_Service": "fiber optic",
    "Online_Security": "yes",
    "Online_Backup": "yes",
    "Device_Protection": "yes",
    "Tech_Support": "yes",
    "Streaming_TV": "yes",
    "Streaming_Movies": "yes",
    "Contract": "two year",
    "Paperless_Billing": "yes",
    "Payment_Method": "credit card (automatic)",
    "Monthly_Charges": "114.05",
    "Total_Charges": "8289.2"
}

def test_get(client):
    url = reverse("prediction")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_one_sample(client):
    url = reverse("prediction")
    response = client.post(url, VALID_PAYLOAD, format="json")
    assert response.status_code == 200

@pytest.mark.django_db
def test_multiple_samples(client):
    url = reverse("prediction")
    payload = [VALID_PAYLOAD, VALID_PAYLOAD]
    response = client.post(
        url, 
        data=json.dumps(payload), 
        content_type="application/json"
    )
    assert response.status_code == 200

@pytest.mark.django_db
@pytest.mark.parametrize("missing_field", ALL_FEATURES)
def test_missing_data(client, missing_field):
    url = reverse("prediction")
    payload = VALID_PAYLOAD.copy()
    payload.pop(missing_field)
    
    response = client.post(
        url, 
        data=json.dumps(payload), 
        content_type="application/json"
    )
    assert response.status_code == 400
    assert missing_field in response.json()["errors"]

@pytest.mark.django_db
@pytest.mark.parametrize("none_field", ALL_FEATURES)
def test_null_featuers(client, none_field):
    url = reverse("prediction")
    payload = VALID_PAYLOAD.copy()
    payload[none_field] = None
    
    response = client.post(
        url, 
        data=json.dumps(payload), 
        content_type="application/json"
    )

    if FeatureSerializer().fields[none_field].allow_null:
        assert response.status_code == 200
    else:
        assert response.status_code == 400

@pytest.mark.django_db
@pytest.mark.parametrize("empty_field", ALL_FEATURES)
def test_empty_data(client, empty_field):
    url = reverse("prediction")
    payload = VALID_PAYLOAD.copy()
    payload[empty_field] = "" 
    
    response = client.post(
        url, 
        data=json.dumps(payload), 
        content_type="application/json"
    )
    assert response.status_code == 400