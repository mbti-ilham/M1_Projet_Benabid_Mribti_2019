others_list=[]
#supprime se que j'ai deja ajouter dans mon fichier
open('E5_familyvs_nosothers.txt ','w').close()
#mettre tout mes othes dans une liste
with open('E2_table-of-IDothers.txt','r') as fi:
	for ligne in fi:
		others_list.append(ligne.replace('\n','').replace('\t',''))
fichoutput = open('E5_familyvs_nosothers.txt','a+')
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
	
 
