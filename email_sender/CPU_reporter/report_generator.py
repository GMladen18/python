from datetime import timedelta, datetime
from time import sleep

from pyspectator.processor import Cpu


def create_report(duration: timedelta):
    measurements = []
    cpu = Cpu(monitoring_latency=0.01)
    with cpu:
        end_time = datetime.now() + duration
        now = datetime.now()
        while now < end_time:
            measurements.append((now, cpu.load))
            now = datetime.now()
            sleep(0.02)

    return measurements
