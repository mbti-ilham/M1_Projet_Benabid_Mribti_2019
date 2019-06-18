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

        sql = "  SELECT gene_id FROM gene WHERE jbrowseTag != '' "
# Execute la commande SQL 
        cursor.execute(sql)

        
# Récupère les resultats afin de cree notre futur table de donnee
        results = cursor.fetchall()
        
        
        if results:
            newfile = open("E7_IDPuls_sql.txt","a+")
            newfile.write('gen_id'+"\n")

        for index in results:
            ltr=[]
            ltr.append(index['gene_id'])
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

