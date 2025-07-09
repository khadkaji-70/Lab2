def straight(l1):
  if(len(l1)<=2):
    print("They form straight line")
  x0,y0=l1[0]
  x1,y1=l1[1]
  dx=x1-x0
  dy=y1-y0

  #points form straight line if the slope is constant
  for i in range(2,len(l1)):
    xi,yi=l1[i]
    dx_i = xi - x0
    dy_i = yi - y0

    if dy * dx_i != dy_i * dx:
      print("Not straight line")
      return



n=int(input("Enter the number of points: "))
l1=[]
for i in range(n):
  x=int(input("Enter x coordinate: "))
  y=int(input("Enter y coordinate: "))
  l1.append((x,y))

print(l1)
straight(l1)



