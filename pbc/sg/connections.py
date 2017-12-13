import paramiko
import time
import socket


class SshClient:
    def __init__(self, host, user, password):
        self._host = host
        self._user = user
        self._password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # try:
        self.client.connect(self._host, username=self._user, password=self._password)
        # except paramiko.SshException, exception:
        #     raise exception
        # except paramiko.AuthenticationException, exception:
        #     message = "SshClient.__init__ failed to authenticate with private key" + exception
        #     raise paramiko.AuthenticationException(message)

    def execute(self, command):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(command)
            # wait for a command is completed
            while not stdout.channel.exit_status_ready():
                time.sleep(1)
            # get status
            execution_status = stdout.channel.recv_exit_status()
            if execution_status == 0:
                print 'Command:[ {} ] executed successfully'.format(command)
                return stdout.read().splitlines()
            else:
                print 'Error appears during execution. Error code:{}'.format(execution_status)
                return stderr.read().splitlines()

        else:
            raise Exception("Can't execute command cause no SSH Connection")

    def close(self):
        if self.client:
            self.client.close()
