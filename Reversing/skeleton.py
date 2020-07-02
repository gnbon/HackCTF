from pwn import *

p=process("./") #local; (PATH)
#p=remote("", ) #nc; (IP, PORT)
#gdb.attach(p) #for gdb
#raw_input("1") #pause procedure

p.recvline()
#p.recvuntil("")
#var=p.recv() #recv n int; (n)

#payload
payload=''* + p32(var)

#exploit
p.sendline(payload)
p.interactive()
