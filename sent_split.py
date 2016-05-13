################## read a para and split it into sentences ########################################

with open ("text.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

# taking care of Mr. Mrs. Dr. Ms. changing . to ,

for p in range(2,len(data)):
  if( ((data[p-2]=='M' and data[p-1]=='r') or(data[p-2]=='D' and data[p-1]=='r' )  or (data[p-2]=='M' and data[p-1]=='s')) and data[p]=='.'):
    data= data[:p]+','+data[p+1:]

for p in range(3,len(data)):
  if( data[p-3]=='M' and data[p-2]=='r'and data[p-1]=='s'  and data[p]=='.'):
    data= data[:p]+','+data[p+1:]

# sentence breaker

ll=[]
pos=0

for i in range(len(data)-1):
  if( (data[i-1]!=' ' and (data[i]=='.' or data[i]=='?' or data[i]=='!') and data[i+1]!=' ' and data[i+1]!='\"') or (data[i-1]!='i' and data[i]=='.' and data[i+1]!='e') or (data[i-1]!=' ' and (data[i]=='.' or data[i]=='?' or data[i]=='!') and data[i+1]==' ')  ):
    ll.append(data[pos : i+1])
    pos=i+1

ll.append(data[pos : len(data)])

# converting , back to .

lll=[]

for d in ll:

  d=str(d)

  for p in range(2,len(d)):
      if( ((d[p-2]=='M' and d[p-1]=='r') or(d[p-2]=='D' and d[p-1]=='r' )  or (d[p-2]=='M' and d[p-1]=='s')) and d[p]==','):
        d= d[:p]+'.'+d[p+1:]

  for p in range(3,len(d)):
    if( d[p-3]=='M' and d[p-2]=='r'and d[p-1]=='s'  and data[p]==','):
      d= d[:p]+'.'+d[p+1:]
    
  lll.append(d)

for line in lll:
 
  print (line)
  print ("\n")
