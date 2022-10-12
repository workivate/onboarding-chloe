# onboarding

## Project Description

This is a standard **Python AWS Serverless** template. This template contains the healthcheck endpoints, `/status` and `/ping`, as described in [Monitoring](https://workivate.atlassian.net/wiki/spaces/BE/pages/3839295511/Monitoring) out of the box. The payload for the `/status` is generated by the [lw-api-status](https://github.com/workivate/lw-api-status)-library.

This template includes the Chocs framework, a [GitHub - kodemore/chocs: Modern HTTP framework for AWS Serverless and WSGI compatible servers](https://github.com/kodemore/chocs), to simplify API development. The following Chocs middleware is included as well:

- [GitHub - kodemore/chocs-openapi: OpenApi middleware for chocs library.](https://github.com/kodemore/chocs-openapi)

- [GitHub - kodemore/chocs-trace: Http tracing middelware and utilities for chocs library](https://github.com/kodemore/chocs-trace)


The OpenApi-middleware is used to parse the openapi specification in `./docs/` and the Trace-middleware is used to send the following HTTP-headers as outlined in [Correlation and Causation Id Reference](https://workivate.atlassian.net/wiki/spaces/BE/pages/3779002373/Correlation+and+Causation+Id+Reference):

- x-request-id

- x-causation-id

- x-correlation-id


Furthermore, Kink, a [GitHub - kodemore/kink: Dependency injection container made for Python](https://github.com/kodemore/kink) is included to enable dependency injection. Although not used in the healthcheck endpoints, an example of the `chocs-trace` `Logger` dependency injection is included in `bootstrap.py`.

## Architectural Design

## Requirements

- [Python](https://www.python.org/)

- [Poetry](https://python-poetry.org/)


## Development Environment Setup

Run `poetry install` to install the virtual environment.

##

## Running Tests

Run `poetry run pytest` to run pytest, includes the coverage plugin.

##

## References
