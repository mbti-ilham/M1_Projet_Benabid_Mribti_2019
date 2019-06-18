
i=0
list=[]
gen_id_lists=[]
with open("E6_othersPuls_sql.txt") as f:
    next(f)
    for linef in f:
        list.append(linef)
        line = linef.split('	')
        #si Trans and - voir avant SusD ---> other
        if(line[2]=='Trans' and line[3]=='-' and i>1):
          # if((line[0] == list[i-1].split('	')[0]) and (line[0] == list[i-2].split('	')[0]) and #gen_id
          if((line[1] == list[i-1].split('	')[1]) and (line[1] == list[i-2].split('	')[1]) and #pul_id
                (list[i-2].split('	')[2] != '' and list[i-1].split('	')[2] == 'SusD')):
                  #print ("----- %s" % list[i-2].split('	')[0])
                  gen_id_lists.append(list[i-2].split('	')[0])	
              
              
              
         #si other et + voir avant SusD ---> Trans
        elif(line[2]!='' and line[3] == '+' and i>1):
           #  if((line[0] == list[i-1][0]) and (line[0] == list[i-2][0]) and #gen_id
             if((line[1] == list[i-1].split('	')[1]) and (line[1] == list[i-2].split('	')[1]) and #pul_id
              (list[i-2].split('	')[2] == 'Trans' and list[i-1].split('	')[2] == 'SusD')):
                  print ("++++++ %s" % line[2], line[0])
                  gen_id_lists.append(line[0])

        i += 1


            #Création d'un fichier contenant tous les identifiants de nos others


newfile = open("E6_tabledersusD.txt","a+")  
#Création d'un fichier s'il n'existe pas avant
#newfile.write('gen_id of all others'+"\n")  

for index in gen_id_lists:
      #pour chaque élement de notre liste d'other nous allons l'ecrire sur le fichier
	ltr=[]
	ltr.append(index)
	lenltr=len(ltr)

	for i in range(lenltr):
		newfile.write('{}'.format(ltr[i]))
		newfile.write("\t")
		print(ltr[i])
	newfile.write("\n")
            
