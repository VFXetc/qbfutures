from __future__ import absolute_import

from concurrent.futures import as_completed


from .. import Executor


def fail():
    raise ValueError('testing failure')


if __name__ == '__main__':
    executor = Executor(name="Python Exeception Test")
    executor.submit('qbfutures.test.fail:fail').result()
    

