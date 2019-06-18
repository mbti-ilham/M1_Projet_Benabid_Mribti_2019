import pymysql.cursors
import pymysql
import sys
import os


# prépare un objet curseur à l'aide de la méthode cursor ()
connection = pymysql.connect(host='localhost',
                             user='admin',
                             password="lina.1997",
                             db='stage',
                             cursorclass=pymysql.cursors.DictCursor)

# prépare un objet curseur à l'aide de la méthode cursor ()

with connection.cursor() as cursor:
    
#Préparer une requête SQL pour sélectionner les informations dans notre base de donnée.
    try:

        sql = "select * from (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as table1 where (EXISTS (SELECT 1 FROM (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE        pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as  table2 where table1.pul_id = table2.pul_id AND table2.jbrowseTag != '') AND EXISTS (SELECT 1 FROM (SELECT pul_gene.gene_id, pul_gene.pul_id, gene.jbrowseTag, gene.orientation, pul_gene.number FROM gene, pul_gene WHERE pul_gene.gene_id = gene.gene_id ORDER BY pul_gene.pul_id ASC) as  table3 where table3.pul_id = table1.pul_id AND table3.jbrowseTag = 'SusD') )"
# Execute la commande SQL 
        cursor.execute(sql)

        
# Récupère les resultats afin de cree notre futur table de donnee
        results = cursor.fetchall()
        
        
        if results:
            newfile = open("E6_othersPuls_sql.txt","a+")
            
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



        #print(index)
    except:
        print ("Error: unable to fecth data")
#déconnecter le serveur
connection.close()
newfile.close()

