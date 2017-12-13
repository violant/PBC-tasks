from abc import ABCMeta, abstractmethod
from time import sleep
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

    @abstractmethod
    def download_json(self):
        pass

    @abstractmethod
    def clean(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def start_hub(self):
        print 'Start hub'
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
        sleep(15)

    def download(self):
        print 'Download'
        self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
        sleep(5)

    def add_node(self):
        print 'Add node'
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node -nodeConfig sg-node.json >> log.txt 2>&1 &')
        sleep(5)

    def download_json(self):
        print 'Download JSON configuration for Selenium Node'
        self._client.execute(
            'wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
        sleep(5)

    def is_downloaded(self):
        if 'True' in self._client.execute('[ -f selenium-server-standalone-3.8.0.jar ] && echo \'True\''):
            return True
        else:
            return False

    def clean(self):
        print 'Clean VM after test'
        self._client.execute('killall java')
        self._client.execute('rm -r selenium*')
        self._client.execute('rm -r sg-node*')
        self._client.execute('rm -r log*')


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid
        self._g.is_downloaded = grid.is_downloaded()

    def start_hub(self):
        self._g.start_hub()

    def download(self):
        if not self._g.is_downloaded:
            print 'Download Selenium server'
            self._g.download()
        else:
            print 'Selenium server already downloaded'

    def download_json(self):
        self._g.download_json()

    def add_node(self):
        self._g.add_node()

    def clean(self):
        self._g.clean()
