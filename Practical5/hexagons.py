#start from n = 1
n = 1
#repeat
for i in range(1,6)
#     calculate nth hexagonal number
      h = 2*n*(2*n-1)/2
#     print the hexagonal number
      print(n,"th hexagonal number =",h)
#     go to the next hexagon number
      n = n+1
