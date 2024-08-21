from typing import Generator

import cashews
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from app import get_app
from settings import Settings
from workflow import workflow_manager


@fixture(scope="session")
def app() -> FastAPI:
    cashews.setup("mem://")
    settings = Settings()  # type: ignore
    fastapi_app = get_app(
        workflow_manager=workflow_manager(settings)
    )
    return fastapi_app


@fixture(scope="session")
def client(app) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
