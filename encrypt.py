import math


s = 'chillout'

s = s.translate(None, ' ')

# create grid R * C > L
l = math.sqrt(len(s))
r = int(math.floor(l))
c = int(math.ceil(l))

if r * c < len(s):
    r += 1
rows = []

# encrypt each column + space
for i in range(r):
    rows.append(s[i*c:(i+1)*c])

for i in rows:
    print i
print

msg_list = []
for i in range(c):
    msg = ''
    for j in range(r):
        if len(rows[j]) > i:
            msg += rows[j][i]
    msg_list.append(msg)

print ' '.join(msg_list)