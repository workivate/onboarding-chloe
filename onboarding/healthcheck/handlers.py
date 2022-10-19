from lw_api_status import ApiStatus
from onboarding.application import app  # noqa: E999
from chocs import HttpRequest, HttpResponse, HttpStatus


@app.get("/ping")
def get_ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse(status=HttpStatus.NO_CONTENT)


@app.get("/status")
def get_status(request: HttpRequest) -> HttpResponse:
    return ApiStatus(api_id="onboarding").generate_status_response()


@app.options("/status")
def options_status(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status=HttpStatus.OK,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "accept, Authorization",
            "Access-Control-Allow-Methods": "OPTIONS, GET",
        }
    )
