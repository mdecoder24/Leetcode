from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        c=Counter(s)
        o=[x for x in c if c[x]&1]

        if len(o)>1:
            return ""

        m=o[0] if o else ""
        h=[]

        for x in range(26):
            h.extend([chr(97+x)]*(c[chr(97+x)]//2))

        k=len(h)
        q=target[:k]

        def build(a):
            x="".join(a)
            return x+m+x[::-1]

        def greater(a):
            a=a[:]

            for i in range(len(a)-2,-1,-1):
                if a[i]<a[i+1]:
                    j=len(a)-1

                    while a[j]<=a[i]:
                        j-=1

                    a[i],a[j]=a[j],a[i]
                    a[i+1:]=reversed(a[i+1:])
                    return a

            return None

        d=Counter(h)
        a=[]
        best=None

        for i in range(k):
            z=None

            for x in range(ord(q[i])-96,26):
                ch=chr(97+x)
                if d[ch]>0:
                    z=ch
                    break

            if z is not None:
                b=a+[z]
                e=d.copy()
                e[z]-=1

                for x in range(26):
                    ch=chr(97+x)
                    if e[ch]:
                        b.extend([ch]*e[ch])

                best=b

            if d[q[i]]==0:
                break

            a.append(q[i])
            d[q[i]]-=1
        else:
            p=build(a)

            if p>target:
                return p

            z=greater(a)

            if z:
                return build(z)

        if best is None:
            return ""

        return build(best)