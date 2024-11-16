game_input=input().strip()
if len(game_input.split())!=2:
    print("Invalid input")
else:
    vignesh,charan=game_input.split()
    
if(vignesh=='R' and charan=='S')or\
  (vignesh=='P' and charan=='R')or\
  (vignesh=='S' and charan=='P'):
    print("Vignesh")
elif(charan=='R' and vignesh=='S')or\
    (charan=='P' and vignesh=='R')or\
    (charan=='S' and vignesh=='P'):
    print("Charan")
else:
    print("NULL")
