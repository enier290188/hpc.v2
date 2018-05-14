# -*- coding: utf-8 -*-
from .... import utils as hpc_utils
from src.security import (
    decorators as security_decorators,
)
from django import http


@security_decorators.required_request_is_ajax()
def index(request):
    data = dict()
    data['BOOLEAN_ERROR'] = False
    data['HTML_DIV_CENTER_DIV_CONTENT'] = hpc_utils.html_template(
        request=request,
        context=dict(),
        template='hpc/_include_/div_center/div_content/hpc/module02/div_content.html',
    )
    return http.JsonResponse(data)
