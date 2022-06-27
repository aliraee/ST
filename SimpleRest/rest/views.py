# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def rest_method(request):
    if request.method == 'Get':
        # TODO:do somthinig
        pass


def test_method(request):
    if request.method == 'GET':
        # create your response dictionary
        response_data = {
            "my_key1": "my value1",
            "my_key2": "my value2",
            "my_key3": {"my value3": "val", "my value8": 'val2', "my value9": "val3"},
            "my_key4": ["my value4", "my value5", "my value6", "my value7"],
            "my_key5": 123123,
        }
        return JsonResponse(response_data)