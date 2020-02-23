from dataclasses import dataclass


@dataclass
class ProcesserInputInterface:
    url: str
    parameter: list
    sleeping_time: int = 3


@dataclass
class AjaxProcesserInputInterface(ProcesserInputInterface):
    ajax_url: str = None
