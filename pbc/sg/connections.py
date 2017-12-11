class SshClient:
    def __init__(self, user, pasw):
        self._user = user
        self._pasw = pasw

    def execute(self, command):
        print '[{u}:{p} -> {c}]'.format(u=self._user, p=self._pasw, c=command)

    def close(self):
        print 'Closing [{u}:{p}]'.format(u=self._user, p=self._pasw)
