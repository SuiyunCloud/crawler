#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module only define processer to do specific action."""

from abc import ABCMeta, abstractmethod
from urllib.parse import urlencode

import requests

from crawler.data_interface import (
    AjaxProcesserInputInterface,
    ProcesserInputInterface,
)


def get_processer(processer_name):
    if processer_name == 'ajax_processer':
        return AjaxProcesser


class Processer(metaclass=ABCMeta):
    def __init__(self, input_data: ProcesserInputInterface):
        self.url = input_data.url
        self.parameter = input_data.parameter

    @abstractmethod
    def run(self):
        pass

    def get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
                          "537.36 (KHTML, like Gecko) Chrome/68.0.3029.110 "
                          "Safari/537.36 SE 2.X MetaSr 1.0",
            "Referer": self.url,
            'x-requested-with': 'XMLHttpRequest'
        }


class AjaxProcesser(Processer):
    def __init__(self, input_data: AjaxProcesserInputInterface):
        super().__init__(input_data)
        self.ajax_url = input_data.ajax_url

    def run(self):
        request_url = self.ajax_url + '?' + urlencode(self.parameter)
        return requests.post(request_url, headers=self.get_headers())
