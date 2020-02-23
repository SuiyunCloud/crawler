#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from .data_interface import ProcesserInputInterface


class PreProcesser(metaclass=ABCMeta):

    @abstractmethod
    def create_processer_input(self):
        return ProcesserInputInterface
