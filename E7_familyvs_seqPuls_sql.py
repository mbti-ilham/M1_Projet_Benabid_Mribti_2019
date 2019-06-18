others_list=[]
#supprime se qe j'ai deja ajouter dans mon fichier
open('E7_familyvs_othersPulssql.txt ','w').close()
#mettre tout mes othes dans une liste
with open('E7_IDPuls_sql.txt','r') as fi:
	for ligne in fi:
		others_list.append(ligne.replace('\n','').replace('\t',''))
fichoutput = open('E7_familyvs_othersPulssql.txt','a+')
#print(others_list)

with open('E4_output_IDfamily.txt','r') as f:
	for line in f:
		cpt = 0
		id_list = line.split('\t')[1].split(',')
		
		for i in range(len(id_list)):
			if id_list[i] in others_list:
			
			#print(id_list[i])
				cpt += 1
			
			
		print(line.split('\t')[0], cpt)   
		fichoutput.write(line.split('\t')[0] +'\t' +str(cpt))
		fichoutput.write('\n')
	
 
