import collections

gen_ids_dict = {}
gen_families_dict = {}
tempdict = {}
exist_gen_id = False
i=1


#construction des ensembles des gen_ids 
with open('table.tsv','r') as f:
    for line in f:
        if(float(line.split('\t')[2]) >= float('45.00')) and  (float(line.split('\t')[10]) <= float('1.00e-20')): #selectinner les homologue a partir d'un seuil précis de pourcentage et de E-value
            gen_id1 = line.split('\t')[0]
            gen_id2 = line.split('\t')[1]
            if(gen_id1 not in gen_ids_dict):
                gen_ids_dict[gen_id1] = {gen_id2} 
            else:
                gen_ids_dict[gen_id1].add(gen_id2)

#triée mon dict
gen_ids_dict = collections.OrderedDict(sorted(gen_ids_dict.items(), key = lambda item : (len(item[1]),item[0]),reverse=True))

print('constructions des listes de familles ')
#listes des familles 
for gen_id, gen_set in gen_ids_dict.items():
    exist_gen_id = False
    tempdict=dict()
    for familyname, gen_big_set in gen_families_dict.items():
            if(gen_set & gen_big_set):
                 # print(familyname,gen_id)
                tempdict[familyname] = 1 #stocker les intersection possible
                exist_gen_id = True    
    if(not exist_gen_id):
        gen_families_dict[str(i)] = gen_set
        i += 1
    else:
        result = set()
        for familyname in tempdict:
             result = result.union(gen_families_dict[familyname])
             del gen_families_dict[familyname]
        result = result.union(gen_set)
        gen_families_dict[str(i)] = result
        i += 1

#print('nombre de familles: ',len(gen_families_dict))

    
print('done')       
print('nombre de familles: ',len(gen_families_dict))
#supprimer les family contenant 1 element
for familyname, gen_big_list in sorted(gen_families_dict.items()):
    if len(gen_big_list) ==1:
        del gen_families_dict [familyname]

	

print('nombre de familles: ',len(gen_families_dict))


# fichier contenant nos famills
fileoutput1 = open('E4_output_IDfamily.txt','w')
for familyname, gen_big_list in sorted(gen_families_dict.items()):
    #pour chaque element de mon genbigset cmb ya susE(other) selectionner au depart
    fileoutput1.write('\n' + familyname +'\t' )
    myStr=""
    for gen in sorted(gen_big_list):
        myStr+=gen +','
    fileoutput1.write(myStr[:len(myStr)-1])
fileoutput1.close()

#fichier contenant le numero de ma famille ainsi que sa longueur
fileoutput = open('E4_outputlongueurfam.ods','w')
for familyname, gen_big_list in sorted(gen_families_dict.items()):

    fileoutput.write(familyname + '\t' + str(len(gen_big_list)))
    fileoutput.write('\n')
fileoutput.close()


