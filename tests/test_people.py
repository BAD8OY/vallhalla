import json
import pytest
import people

def test_read_all(app):
    with app.app_context():
        people.read_all()

