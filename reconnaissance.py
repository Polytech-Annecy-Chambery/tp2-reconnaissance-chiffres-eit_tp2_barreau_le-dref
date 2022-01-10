from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    #binarisation et localisation de l'image à reconnaitre
    im_bin = image.binarisation(S)
    im_local = im_bin.localisation()
    proportion = 0
    prop_max = 0
    rang = 0
    for i in range(len(liste_modeles)) : 
        proportion = liste_modeles[i].similitude(im_local.resize(liste_modeles[i].H,liste_modeles[i].W))
        if proportion > prop_max :
            prop_max = proportion
            rang=i
    return rang 
        
    

