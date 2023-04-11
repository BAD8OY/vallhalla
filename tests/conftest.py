import pathlib
from json import JSONEncoder
import connexion
import pytest
from flask import Flask
import config


@pytest.fixture
def app():
    app = create_app()
    return app