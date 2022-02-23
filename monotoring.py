#c'est un simple script python pour une simple supervision système 
import psutil    #pour installer psutil " pip install psutil"
import datetime
import pandas   #pour installer pandas " ip install pandas "

#defenir des liste vides pour stocker les les détails du processus

pids = []
nom = []
utisation_CPU = []
utilisation_memoire = []
pourcentage_utilisation_memoire =[]
statut =[]
temps_decreation =[]
threads =[]

for process in psutil.process_iter():  #la fonction process_iter() pour itére sur tous les processus exécuter sur le systeme local
    pids.append(process.pid)  #pid() renvoie l'ID de processus
    nom.append(process.name())  # name renvoie le nom du processus

    utisation_CPU.append(process.cpu_percent(interval=1)/psutil.cpu_count())  #cpu_percent() renvoie le pourcentage d'utilisation CPU de processus

    utilisation_memoire.append(round(process.memory_info().rss/(1024*1024),2))  #memory_info() renvoie le dictionnaire des differentes types d'utilisation de la mémoir par la processus

    pourcentage_utilisation_memoire.append(round(process.memory_percent(),2))  #memory_percent() renvoie le pourcentage de mémoire du processus en comarant la mémoire du processus à la mémoire système

    temps_decreation.append(datetime.datetime.fromtimestamp(process.create_time()).strftime("%Y%m%d - %H:%M:%S"))  #create_time renvoie l'heure de création du processus en secondes.

    statut.append(process.status())  #status renvoie le statut du processus

    threads.append(process.num_threads())  #threads renvoie le nombre de threads utilisés par le processus.


#création d'un dictionnaire de données qui contient tous les détails du processus
data = {"PIDs":pids,
        "NOM": nom,
        "Utilisation de CPU":utisation_CPU,
        "Utilisation du mémoire en (MB)":utilisation_memoire,
        "Pourcentage de mémoire(%)": pourcentage_utilisation_memoire,
        "Statut": statut,
        "Temps de creation": temps_decreation,
        "Threads": threads,
        }
#convertir le dictionnaire en pandas DataFrame en utilisant la fonction Data Frame.
process_df = pandas.DataFrame(data)
#sdéfinir la valeur de l'index sur PIds
process_df =process_df.set_index("PIDs")

#strier les processus en fonction de leur utilisation de la mémoire,
process_df =process_df.sort_values(by='Utilisation du mémoire en (MB)', ascending=False)

#ajouter MB à la fin de la mémoire
process_df["Utilisation du mémoire en (MB)"] = process_df["Utilisation du mémoire en (MB)"].astype(str) + " MB"

print(process_df)
