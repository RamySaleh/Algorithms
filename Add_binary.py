input1 = "1010"
input2 = "1011"
#Output: "10101"

input1 = "11"
input2 = "1"

input1 = "11"
input2 = "11"
#Output: "100"

def addBinary(input1: str, input2: str) -> str:
    while len(input1) < len(input2):
        input1 = "0" + input1

    while len(input2) < len(input1):
        input2 = "0" + input2

    max_len = len(input1) #if len(input1) > len(input2) else len(input2)
    idx = max_len - 1
    res = ""
    rem = 0
    while idx + rem >= 0:
        a = input1[idx] if (0 <= idx < len(input1)) else "0"
        b = input2[idx] if (0 <= idx < len(input2)) else "0"
        if a == "0" and b == "0":
            if rem == 0:
                res = "0" + res
            else:
                res = "1" + res
                rem = rem - 1
        elif a == "1" and b == "1":
            if rem == 0:
                res = "0" + res
                rem = rem + 1
            else:
                res = "1" + res
        else:
            if rem == 0:
                res = "1" + res
            else:
                res = "0" + res
        idx = idx - 1
    return res

def addBinary2(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

def addBinary3(self, a: str, b: str) -> str:

    result = []
    carry = 0

    for i in range(1, max(len(a) + 1, len(b) + 1)):
        summed = carry
        if len(a) >= i: summed += int(a[-1 * i])
        if len(b) >= i: summed += int(b[-1 * i])
        carry = summed // 2
        val = summed % 2
        result.insert(0, str(val))

    if carry > 0:
        result.insert(0, str(carry))

    return "".join(result)

print(addBinary(input1,input2))