  def fa(num):
    if num<3:
        return 1
    else:
        return fa(num-1)+fa(num-2)
for i in range(1,50):
    print(fa(i),end = ' ')
