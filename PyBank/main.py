import os, sys
import re


os.chdir(r'C:\Users\wendi\My Drive\python-challenge\PyBank')
# print(os.getcwd())


def formatmoney(v):
    v = float(v)

    if v < 0:
        return('-$ {:,.2f}'.format(abs(v)))
    else:
        return('$ {:,.2f}'.format(v))


fw = open(r'analysis\budget_result.txt', 'w')

print('Financial Analysis', file=fw)
print('Financial Analysis')
print('-' * 100, file=fw)
print('-' * 100)

c = 0
totpnl = 0
pnl_d = {}

with open(r'Resources\budget_data.csv', 'r') as fr:
    next(fr)
    # print(fr.readline())

    for line in fr:
        if not line.strip():
            continue
        
        line = line.strip()
        tmp = line.split(',')
        # print(line, tmp)
        mth = tmp[0]
        pnl = tmp[1]
        # print(pnl)
        pnl_d[mth] =  pnl

        totpnl += int(pnl)
        c += 1
print(f'Total Months: {c}', file=fw)
print(f'Total Months: {c}')
print(f'Total: {formatmoney(totpnl)}', file=fw)
print(f'Total: {formatmoney(totpnl)}')


# print(pnl_d, len(pnl_d))
pnl_l = list(pnl_d.values())
# print(pnl_l)

chg_l = []
d = 0
totchg = 0
for i in range(1, len(pnl_d)):

    chg = float(pnl_l[i]) - float(pnl_l[i - 1])
    # print(chg)
    chg_l.append(chg)

    totchg += chg
    d += 1
avgchg = totchg / d
print(f'Average Change: {formatmoney(avgchg)}', file=fw)
print(f'Average Change: {formatmoney(avgchg)}')



mth_l = list(pnl_d.keys())
# print(mth_l)
mth_l.pop(0)

# print(mth_l, len(mth_l))
# print(chg_l, len(chg_l))

top = float('-inf')
btm = float('inf')

for k, v in zip(mth_l, chg_l):
    # print(k, v)

    if v > top:
        top = v
        top_k = k

    if v < btm:
        btm = v
        btm_k = k

print(f'Greatest Increase in Profits: {top_k} ({formatmoney(top)})', file=fw)
print(f'Greatest Increase in Profits: {top_k} ({formatmoney(top)})')
print(f'Greatest Decrease in Profits: {btm_k} ({formatmoney(btm)})', file=fw)
print(f'Greatest Decrease in Profits: {btm_k} ({formatmoney(btm)})')

fw.close()