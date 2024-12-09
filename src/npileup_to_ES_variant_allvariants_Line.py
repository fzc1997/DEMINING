import sys
dic = {'a':[5,11],'c':[7,11],'g':[9,11],'t':[13,11]}
dui = {5:'a',7:'c',9:'g',13:'t'}

# f = sys.stdin
# with open(sys.stdin,'r') as f1:
# print(sys.argv[2],sys.argv[3])
for l1 in sys.stdin:
    l1 = l1.strip().split('\t')
    # print(l1)
    l1[1] = l1[1].lower()
    for i in range(5,15,2):
        if l1[1] in dic and i not in dic[l1[1]]:
            if int(l1[-3])>=int(sys.argv[3]):
                if float(l1[i])/int(l1[-3]) >float(sys.argv[2]):
                    print(('\t').join(l1[:3]+l1[5:]),'\t',dui[i],l1[i+1])