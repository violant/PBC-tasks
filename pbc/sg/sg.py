from abc import ABCMeta, abstractmethod
import time
from pbc.sg.connections import SshClient


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def start_hub(self):
        print 'Start hub'
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def download(self):
        print 'Download'
        self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')

    def add_node(self):
        print 'Add node'
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')

    def is_downloaded(self):
        if 'True' in self._client.execute('[ -f selenium-server-standalone-3.8.0.jar ] && echo \'True\''):
            return True
        else:
            return False


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid
        self._is_downloaded = grid.is_downloaded()

    def start_hub(self):
        self._g.start_hub()

    def download(self):
        if not self._is_downloaded:
            print 'Download Selenium server'
            self._g.download()
        else:
            print 'Selenium server already downloaded'

    def add_node(self):
        self._g.add_node()
