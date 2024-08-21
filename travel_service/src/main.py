import uvicorn

from app import get_app
from settings import Settings
from workflow import workflow_manager


def run_app(settings: Settings) -> None:
    app = get_app(
        workflow_manager=workflow_manager(settings)
    )

    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=settings.service_port
    )


def main() -> None:
    settings = Settings()  # type: ignore[reportCallIssue]

    run_app(settings=settings)


if __name__ == '__main__':
    main()
