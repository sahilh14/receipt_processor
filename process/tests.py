import json
import unittest
from django.urls import reverse
from rest_framework import status
from .services import calculate_points
from rest_framework.test import APITestCase


class CalculatePointsTestCase(unittest.TestCase):

    def test_basic_functionality(self):
        receipt = {
            "retailer": "ABC Store",  # 8
            "total": "100.00",  # 75
            "items": [  # 5
                {"shortDescription": "Item 1", "price": "10.00"},  # 2
                {"shortDescription": "Item 2", "price": "20.00"},  # 4
            ],
            "purchaseDate": "2024-03-01",  # 6
            "purchaseTime": "15:00",  # 10
        }
        self.assertEqual(calculate_points(receipt), 110)

    def test_retailer_special_chars(self):
        receipt = {
            "retailer": "XYZ&Co",  # 5
            "total": "50.00",  # 75
            "items": [{"shortDescription": "Item 1", "price": "25.00"}],  # 5
            "purchaseDate": "2024-03-02",
            "purchaseTime": "16:30",
        }
        self.assertEqual(calculate_points(receipt), 85)


class ProcessReceiptViewTestCase(APITestCase):

    def test_valid_receipt_processing(self):
        receipt_data = {
            "retailer": "Test Retailer",
            "purchaseDate": "2024-03-01",
            "purchaseTime": "15:00",
            "items": [
                {"shortDescription": "Item 1", "price": "10.00"},
                {"shortDescription": "Item 2", "price": "20.00"},
            ],
            "total": "30.00",
        }
        response = self.client.post(
            reverse("process_receipt"),
            json.dumps(receipt_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("id" in response.data)
        self.assertTrue(response.data["id"])

    def test_invalid_empty(self):
        invalid_receipt_data = {}
        response = self.client.post(
            reverse("process_receipt"),
            json.dumps(invalid_receipt_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("message" in response.data)

    def test_invalid_missing_retailer(self):
        invalid_receipt_data = {
            "purchaseDate": "2024-03-01",
            "purchaseTime": "15:00",
            "items": [
                {"shortDescription": "Item 1", "price": "10.00"},
                {"shortDescription": "Item 2", "price": "20.00"},
            ],
            "total": "30.00",
        }
        response = self.client.post(
            reverse("process_receipt"),
            json.dumps(invalid_receipt_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("message" in response.data)

    def test_invalid_empty_items(self):
        invalid_receipt_data = {
            "retailer": "Test Retailer",
            "purchaseDate": "2024-03-01",
            "purchaseTime": "15:00",
            "items": [],
            "total": "30.00",
        }
        response = self.client.post(
            reverse("process_receipt"),
            json.dumps(invalid_receipt_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("message" in response.data)

    def test_invalid_price_pattern(self):
        invalid_receipt_data = {
            "retailer": "Test Retailer",
            "purchaseDate": "2024-03-01",
            "purchaseTime": "15:00",
            "items": [
                {"shortDescription": "Item 1", "price": "10.00"},
            ],
            "total": "30",
        }
        response = self.client.post(
            reverse("process_receipt"),
            json.dumps(invalid_receipt_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("message" in response.data)
