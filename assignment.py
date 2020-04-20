

for i in range(10,0,-1):
  print("*"*(i))


for j in range(1,10):
  print("2 x {} = {}".format(j, j*2))


sum=0
for i in range(1,1001):
  if i%3==0:
    sum+=i 
  else:
    continue
print(sum)



mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
score_sum=0
for score in mutsa_scores:
  score_sum+=score 
print(score_sum/len(mutsa_scores))


