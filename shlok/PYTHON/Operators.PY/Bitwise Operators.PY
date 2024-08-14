a = 2
b = 5

left_shift = b<<a
print(left_shift)

right_shift = b>>a
print(right_shift)

bit_and = a&b
print(bit_and)

bit_or = a | b # 010 | 101 ==> 111
print (bit_or)

bit_xor = a ^ b # 010 ^ 101 ==> 111 because XOR = ab'+ba'
print (bit_xor), bit_xor
bit_not = ~a # 010 ==> 011 because negate = -(x+1)
print (bit_not), bit_not
