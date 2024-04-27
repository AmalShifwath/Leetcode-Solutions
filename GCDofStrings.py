class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = ""
        iter = len(str1)
        lon = len(str1)
        lonstr = str1

        if len(str1) > len(str2):
            iter = len(str2)
            lon = len(str1)
            lonstr = str1
        elif len(str2) > len(str1):
            iter = len(str1)
            lon = len(str2)
            lonstr = str2

        for i in range(iter):
            if str1[i] == str2[i]:
                x += str1[i]

        print(x)
        if len(x) == 0:
            return x

        if len(x) == 2:
            if lon % len(x) != 0:
                if x[0] == x[1]:
                    print("len 2 lon 1=0")
                    x = x[0]
        elif len(x) >= 4:
            for i in range(2, int(len(x) / 2 + 1)):
                if lon % len(x) == 0:
                    return x

                print("trying by ", i)

                print(int(len(x)) % i)

                if int(len(x)) % i == 0 and (int(len(x)) / i) != 1:
                    print("divisible by ", i)
                    ind = int(len(x) / i)
                    if x[:ind] == x[ind : (2 * ind)]:
                        x = x[:ind]

        x2 = x
        confirm1 = False
        confirm2 = False
        while len(x2) <= lon:
            if x2 == str1:
                confirm1 = True
                print("confirm1, ", x2)
            if x2 == str2:
                confirm2 = True
                print("confirm2, ", x2)
            x2 += x

        if (confirm1 == True) and (confirm2 == True):
            return x
        else:
            return ""
