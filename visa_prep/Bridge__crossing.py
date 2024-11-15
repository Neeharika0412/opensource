x,y,z=map(int,input().split())
max_weight=z
remaining_weight=max_weight-y
if remaining_weight>=x:
    max_mangoes=remaining_weight//x
else:
    max_mangoes=0
print(max_mangoes)    
    
