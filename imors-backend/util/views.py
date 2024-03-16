from functools import wraps
from json import loads
from typing import Any, Dict

from django.http import HttpRequest, HttpResponseBadRequest


def get_query_params(request: HttpRequest) -> Dict[str, Any]:
    return request.GET


def get_body_params(request: HttpRequest) -> Dict[str, Any]:
    return loads(request.body)


def __get_param_error(given_params: Dict[str, Any], required_params: Dict[str, type]) -> str:
    def tn(t: type) -> str:
        return str(t).split("'")[1]

    for required_param_key, required_param_type in required_params.items():
        param_value = given_params.get(required_param_key, None)

        if param_value is None:
            return f"{required_param_key} is not given."

        param_type = type(param_value)

        if param_type != required_param_type:
            return f"Got {tn(param_type)} for {required_param_key}: Expected {tn(required_param_type)}"

    return None


def validate_params(required_query_params: Dict[str, type] = None, required_body_params: Dict[str, type] = None):
    def decorator(view_method):
        @wraps(view_method)
        def __wrapped_view(view, request, *args, **kwargs):
            if required_body_params:
                error_message = __get_param_error(get_body_params(request), required_body_params)

            if not error_message and required_query_params:
                error_message = __get_param_error(get_query_params(request), required_query_params)

            if error_message:
                return HttpResponseBadRequest(error_message)

            return view_method(view, request, *args, **kwargs)

        return __wrapped_view

    return decorator
