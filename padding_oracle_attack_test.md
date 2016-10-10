# Example of padding oracle attack

###String data:
Hello World of Encryption using RC5

###Data:
```
48 65 6C 6C 6F 20 57 6F
72 6C 64 20 6F 66 20 45
6E 63 72 79 70 74 69 6F
6E 20 75 73 69 6E 67 20
52 43 35
```
###Encrypted data
```
Algorithm: RC5-CBC-PAD
F7 84 54 F4 C5 23 EB B3
F0 7D 42 C5 F8 99 4C FA
2F 28 16 78 CF 45 A7 02
7A 85 74 19 30 85 53 4C -> "IV" block target
97 89 BA 80 82 73 EC DB -> block target
```
###Attack:
```
28 c6 41 1c 35 80 56 49 -> oracle data last block
97 89 BA 80 82 73 EC DB -> Real last block
```
We have to do XOR between oracle data and the
block before the block target ("IV")
```
28 c6 41 1c 35 80 56 49 -> oracle data last b
7A 85 74 19 30 85 53 4C -> block before
52 43 35 05 05 05 05 05 -> Obtained data
```
