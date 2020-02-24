import itertools

div = {}
sup = {}
filt_sup = {}

def generate_numbers():
  for i in range(1,101):
    div[i] = []
    for j in range(1,101):
      if i % j == 0:
        div[i].append(j)

def get_sup():
  for i in range(1,101):
    sup[i] = 0
    for j in range(1,101):
      if i in div[j]:
        sup[i] += 1

def filter_sup():
  for i in range(1,101):
    if sup[i] >= 5:
      filt_sup[i] = sup[i]

generate_numbers()

get_sup()

filter_sup()

combinations_two = list(itertools.combinations(list(filt_sup.keys()), 2))

two_sup = {}

for comb in combinations_two:
  two_sup[comb] = 0
  for d in div:
    count = 0
    for num in comb:
      if num in div[d]:
        count += 1
    if count == 2:
      two_sup[comb] += 1

# print(two_sup)

filt_two_sup = {}

for i in two_sup:
  if two_sup[i] >= 5:
    filt_two_sup[i] = two_sup[i]

print(filt_two_sup)

filt_nums = []

for i in filt_two_sup:
  for j in i:
    filt_nums.append(j)

# print(list(set(filt_nums)))