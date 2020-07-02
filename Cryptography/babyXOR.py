from pwn import *

p = remote('ctf.j0n9hyun.xyz', 9001)

p.recvuntil("> ")
p.sendline('2')
p.recvuntil("key len: ")
p.sendline('8') # set key_len 8

p.recvuntil("> ")
p.sendline('1')

flag_XOR = p.recvline()
p.recvuntil("> ")

print(flag_XOR[2:-2])

flag_XOR = binascii.unhexlify(flag_XOR[2:-2])

flag_format = 'HackCTF{'
key = xor(flag_XOR[:8], flag_format)

dec=''

dec = xor(flag_XOR, key)
print(dec)

# HackCTF{X0R_1s_Very_Very_Strawberry_e4sy!!}