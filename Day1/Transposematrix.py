a=[[12,1],
  [3,4],
  [5,6]]
x=[[0,0,0],
   [0,0,0]
  ]

for i in range(len(a)):
    for j in range(len(a[0])):
        x[j][i]=a[i][j]
for r in x:
    print(r)