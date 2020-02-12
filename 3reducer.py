s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0


for line in s:
  
  data = line.strip().split('\t')
  paymentType, amount = data
  #print("count: ",count)
  if paymentType != thisKey:
    count=0
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
      count+=1
    else:
      count+=1
      
      
    # start over when changing keys
    thisKey = paymentType 
    thisValue = 0.0
    
  
  # apply the aggregation function
  thisValue += count

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
