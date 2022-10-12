import os
from pathlib import Path

from chocs.application import Application
from chocs_middleware.openapi import OpenApiMiddleware
from chocs_middleware.trace import TraceMiddleware
from onboarding.bootstrap import bootstrap_di  # noqa: E999


def get_openapi_file_path() -> str:
    file_path = Path(__file__)
    package_path = file_path.parent.parent
    openapi_file = os.path.join(package_path, "docs", "openapi.yaml")

    return openapi_file


bootstrap_di()

app = Application(
    OpenApiMiddleware(get_openapi_file_path(), validate_body=True, validate_query=True),
    TraceMiddleware(id_prefix="onboarding-"),
)
