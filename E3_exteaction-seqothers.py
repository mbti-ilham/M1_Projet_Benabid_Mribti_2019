"""
récupérer les séquences d’interet de notre fichier prot.fa a partir des identifiants others.posisined "mes_others.py"
"""

from Bio import SeqIO

#mettre tous mes gen_ids autant que clés dans un dictionnaire
gen_idliste={}
records={}
with open('E2_table-of-IDothers.txt','r') as f:								#ouvrir fichier E2_table-of-IDothers.txt
	next(f)
	for line in f:
		for items in gen_idliste:			
			gen_idliste.update(line.split('\t')[0])						#chaque identidiant et la cles du dictionnaire


print('fini')

#ajouté comme valeur du dictionnaire les sequence associer a chaque identifient
inputfile = 'prot.fa'
for seq_record in SeqIO.parse(inputfile, "fasta"):
	#si les id existes dans les gene_id du dictionnaire 
	if(seq_record.id.split('||')[0] in gen_idliste):
		#lui associer en valeur la sequence correspondant
		for items in records:
			#print(" Existe dans ma liste  ",seq_record.id.split('||')[0])
			records.update(seq_record)

#sauvegarde
outputfile = 'E3_outputseqothers.fa'
print("mon fichier est done ")
SeqIO.write(records,outputfile, "fasta")





