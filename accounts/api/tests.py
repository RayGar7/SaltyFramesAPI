from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase


from django.contrib.auth import get_user_model

User = get_user_model()