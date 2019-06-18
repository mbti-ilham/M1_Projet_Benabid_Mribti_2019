"""
ce script table_de_données.py permet d'exécuter une requête Sql, dans le but de récupérer à partir de notre fichier stage_light.Sql un tableau contenant seulement les informations qui nous sont nécessaires comme : l’identifient de chacun des gènes, ainsi que leurs locus tag, leurs positions, le numéro de leurs PULS, et leurs orientations.
À condition que chacun des PULS récupérés possède obligatoirement un Trans et un susD.
"""
import pymysql.cursors
import pymysql
import sys
import os


# se conneter a  notre base de donnée
connection = pymysql.connect(host='localhost',							#connecxion a notre serveur local
                             user='admin',							#identifiant
                             password="lina.1997",							#mot de passe
                             db='cul',							#nom de la base de donnee ou ce trouve nos tables 
                             cursorclass=pymysql.cursors.DictCursor)	#on definit notre curseur 

# prépare un objet curseur à l'aide de la méthode cursor ()

with connection.cursor() as cursor:
    
# Préparer une requête SQL pour sélectionner les informations dans notre base de donnée.
    try:																  
		
        sql = "select * from (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as table1 where (EXISTS (SELECT 1 FROM (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE        pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as  table2 where table1.pul_id = table2.pul_id AND table2.jbrowseTag = 'other') AND EXISTS (SELECT 1 FROM (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as  table3 where table3.pul_id = table1.pul_id AND table3.jbrowseTag = 'SusD') AND EXISTS (SELECT 1 FROM (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as  table4 where table1.pul_id = table4.pul_id AND table4.jbrowseTag = 'Trans'))"
        
# Executer la commande sql
        cursor.execute(sql)

        
# Récupère les resultats afin de cree notre futur table de donnees.
        results = cursor.fetchall()
        
#enregister les informations recuperer sous forme de tableau txt 
        if results:
            newfile = open("E1_tableau-data.txt","a+")
            newfile.write('gen_id'+"    "+'pul_id'+"   "+"jbrowseTag"+" "+'orientation'+" "+'number'+"\n")

        for index in results:
            ltr=[]
            ltr.append(index['gene_id'])
            ltr.append(index['pul_id'])
            ltr.append(index['jbrowseTag'])
            ltr.append(index['orientation'])
            ltr.append(index['number'])
            lenltr=len(ltr)

            for i in range(lenltr):
                newfile.write('{}'.format(ltr[i]))
                newfile.write("\t")
                #print(ltr[i])
            newfile.write("\n")


    except:
        print ("Error: unable to fecth data")
# déconnecter le serveur
connection.close()
newfile.close()

print(results)

	

