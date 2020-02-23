"""This module define a pipeline to organize whole work process, including how
to shedule job for processer."""
import random
from copy import deepcopy
from time import sleep

from .Processer import get_processer


class Pipeline:
    def __init__(self, processer_input, processer, post_process=None):
        self.processer = get_processer(processer)
        self.processer_input = processer_input
        self.post_process = post_process

    def run(self):
        one_crawl_input = deepcopy(self.processer_input)
        rst = []
        for data in self.processer_input.parameter:
            one_crawl_input.parameter = data
            one_crawl = self.__post_process(
                self.processer(one_crawl_input).run())
            rst.append(one_crawl)
            print(one_crawl)
            sleep(self.processer_input.sleeping_time * (1 + random.randrange(1, 100) / 1000))
        return self.__post_process(rst)

    def __post_process(self, rst):
        if self.post_process:
            return self.post_process(rst)
        return rst
