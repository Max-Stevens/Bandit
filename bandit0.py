#!/usr/bin/python3

from pwn import *

username = 'bandit'
levelPass = []
levelPass.append('bandit0')

def getShell(level, passwords):
    session = ssh(username+str(level), 'bandit.labs.overthewire.org', 2220, password=passwords[level])
   
    return (session, session.process('/bin/sh', env={'PS1':''}))

session, sh = getShell(0,levelPass)

sh.sendline('cat readme')
levelPass.append((sh.recvline()).decode('utf-8').strip())
session.close()

print(levelPass)

session, sh = getShell(1,levelPass)
sh.sendline('cat ./-')
levelPass.append((sh.recvline()).decode('utf-8').strip())
session.close()

print(levelPass)

session, sh = getShell(2,levelPass)
sh.sendline('cat "spaces in this filename"')
levelPass.append((sh.recvline()).decode('utf-8').strip())
session.close()

print(levelPass)

session, sh = getShell(3,levelPass)
sh.sendline('cat ./inhere/.hidden')
levelPass.append((sh.recvline()).decode('utf-8').strip())
session.close()

print(levelPass)

session, sh = getShell(4,levelPass)
sh.sendline('cd inhere; cat ./-file07')
levelPass.append((sh.recvline()).decode('utf-8').strip())

print(levelPass)

session, sh = getShell(5,levelPass)
sh.sendline('cd inhere; cat $(find ./ -size 1033c)')
levelPass.append((sh.recvline()).decode('utf-8').strip())

print(levelPass)

