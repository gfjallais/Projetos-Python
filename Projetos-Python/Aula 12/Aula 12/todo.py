# -*- coding: utf8


import threading
import requests


class Worker(threading.Thread):
    def __init__(self, id_, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self._id = id_
        self._num_lines = 0
    
    def run(self):
        book = requests.get('http://www.gutenberg.org/files/{}/{}-0.txt'.format(self._id, self._id))
        lines = book.text.split('\n')
        for line in lines:
            if line:
                self._num_lines += 1
    
    def get_result(self):
        return self._num_lines


def crawler():
    soma = 0
    with open('dados/ids.txt') as file:
        for line in file:
            id = line.strip()
            c = Worker(id)
            c.run()
            soma += c.get_result()
    return soma