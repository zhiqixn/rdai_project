"""
This module is to test the endpoint.
"""

import sys
import os

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import app

client = TestClient(app)
data = {"instructions": "Who are you?"}
response = client.post("http://0.0.0.0:8001/answer", json=data)
print(response.json())
