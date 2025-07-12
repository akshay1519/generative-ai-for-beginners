import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import pytest
from app.main import app

def test_index_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200