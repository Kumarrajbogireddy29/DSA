class Solution:
    def myAtoi(self, s: str) -> int:
        ptr=0
        for i in range(len(s)):
            if s[i]==' ':
                ptr=ptr+1
            else:
                break
        sign=1
        for j in range(ptr,len(s)):
            if s[j]=='-':
                sign=sign*-1
                ptr=ptr+1
            elif s[j]=='+':
                ptr=ptr+1
            break
        for k in range(ptr,len(s)):
            if s[k]=='0':
                ptr=ptr+1
            else:
                break
        #string=""
        l=[]
        for i in range(ptr,len(s)):
            if s[i]>='0' and s[i]<='9':
                l.append(s[i])
            else:
                break
        if not l:
            return 0
        else:
            if sign*int("".join(l))>(2**31-1):
                return 2**31-1
            elif sign*int("".join(l))<((-2)**31):
                return (-2)**31
            else:
                return sign*int("".join(l))