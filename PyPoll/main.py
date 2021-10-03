import os, sys
import re
from collections import defaultdict


os.chdir(r'C:\Users\wendi\My Drive\python-challenge\PyPoll')


fw = open(r'analysis\election_result.txt', 'w')

print('Election Results', file=fw)
print('Election Results')
print('-' * 100, file=fw)
print('-' * 100)

c = 0
dicy = defaultdict(int)

with open(r'Resources\election_data.csv', 'r') as fr:
    next(fr)

    for line in fr:
        if not line.strip():
            continue
        
        line = line.strip()
        tmp = line.split(',')
        cand = tmp[2]

        dicy[cand] +=1

        # totpnl += int(pnl)
        c += 1
print('Total Votes: {:,}'.format(c), file=fw)
print('Total Votes: {:,}'.format(c))
print('-' * 100, file=fw)
print('-' * 100)


# print(dicy)
for k in dicy:
    perc = float(dicy[k]) / c

    dicy[k] = f'{dicy[k]}-{perc}'
# print(dicy)

for k in dicy:
    votes = dicy[k].split('-')[0]
    percvotes = dicy[k].split('-')[1]

    print('{}: {:.2%} ({:,})'.format(k, float(percvotes), int(votes)), file=fw)
    print('{}: {:.2%} ({:,})'.format(k, float(percvotes), int(votes)))


print('-' * 100, file=fw)
print('-' * 100)
winner = max(dicy, key=lambda x: int(dicy[x].split('-')[0]))

print(f'Winner: {winner}', file=fw)
print(f'Winner: {winner}')

print('-' * 100, file=fw)
print('-' * 100)

fw.close()