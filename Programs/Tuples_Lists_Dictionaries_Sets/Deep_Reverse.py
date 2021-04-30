#Double/Deep Reverse
L = [[2,3,4,5],[3,6,7,8],[6,7,8,9],[9,4,5,6]]
L1 = L[::-1]
L_res =[]
for i,j in enumerate(L1):
  L_res.append(j[::-1])
print(L_res)