# 你需要将你的 token 填入下方的变量中
### BEGIN CONFIG
host = '210.45.70.126'
port = '32330'
token = '162:MEQCIA5yLagezqdsoOiBIjN/Tlj+UfYg09ozO0veFFh5hIYoAiAG+rt630DN4kLZb566CUzdZzBiWFKELz2TPNXa+LmP5g=='
### END CONFIG

import json, time, os, sys, traceback

try:
    from pwn import remote, xor
    from Crypto.Cipher import AES
except ModuleNotFoundError:
    print('[x] 缺少必须的依赖库!')
    print('    请使用 pip install pwntools pycryptodome 进行安装')
    sys.exit(1)

try:
    rn = remote(host, port)
    rn.sendlineafter(b'token:', token.encode())
    rn.recvuntil(b'[+]')
    target = bytes.fromhex(rn.recvline().decode().strip())
except:
    traceback.print_exc()
    print('[+] 在连接服务器的过程中出现错误!')
    sys.exit(1)
print('[+] 已经成功连接上服务器!')
print('[+] 本次的 target 为:', target.decode())

def pad(msg):
    n = AES.block_size - len(msg) % AES.block_size
    return msg + bytes([n]) * n

def unpad(msg):
    assert len(msg) > 0 and len(msg) % AES.block_size == 0
    n = msg[-1]
    assert 1 <= n <= AES.block_size
    assert msg[-n:] == bytes([n]) * n
    return msg[:-n]

def call(task_id: int, ciphertext: bytes) -> str:
    rn.sendlineafter(b'[>]', str(task_id).encode())
    rn.sendlineafter(b'[>]', ciphertext.hex().encode())
    return rn.recvline().decode().strip()

# 在接下来的部分写你的代码
# 你可以通过 target 变量来获取你要伪造的 bytes 串
# 可以通过调用 call(i, ciphertext) 来与题目交互
# 例: call(1, c) 将尝试解答题目的第 1 小问，并尝试将 bytes 类型的 c 作为答案
# call 函数将返回题目的结果
# 结果可能有三种: 该小题的 flag, 'Nope' 或者 'Invalid input'
# 你可以通过 s.startswith('flag{') 来判断 s 是不是合法的 flag
# 下方是一个如何使用 call 函数的示例
#
# 1 |  res = call(0, '行行好, 给个 flag 吧')
# 2 |  if res.startswith('flag{'):
# 3 |      print('[+] 得到 flag:', res)
# 4 |  else:
# 5 |      print('[x] 未能得到 flag:', res)
#
# 除此之外，你可能用到的辅助函数: xor
# xor(a, b) 可以将两个 bytes 对象 a, b 按字节进行异或
# 甚至 xor(a, b, c) 等更多个参数的写法都是合法的1
### BEGIN USER CODE
### END USER CODE