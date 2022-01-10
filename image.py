from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
		# creation d'une image vide
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        
        for i in range(self.W):
            for j in range(self.H):
                if self.pixels[j][i] <= S:
                    im_bin.pixels[j][i] = 0
                else:
                    im_bin.pixels[j][i] = 255
        
        return im_bin  

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        l_max=0
        l_min=0
        c_max=0
        c_min=0
        first_detection_l = True
        first_detection_c = True
        im_bin_resize = Image()
        for l in range (self.H):
            for c in range(self.W) :
                if self.pixels[l][c]==0 and first_detection_l==True:
                    l_min = l
                    first_detection_l = False
                elif self.pixels[l][c]==0 and first_detection_l==False:
                    l_max = l+1
        for c in range(self.W):
            for l in range(self.H):
                if self.pixels[l][c]==0 and first_detection_c==True:
                    c_min = c
                    first_detection_c = False
                elif self.pixels[l][c]==0 and first_detection_c==False:
                    c_max = c+1
        print ( l_max, l_min, c_max, c_min)
        im_bin_resize.set_pixels(np.zeros((l_max-l_min, c_max-c_min), dtype=np.uint8))
        for l in range (l_max-l_min):
            for c in range(c_max-c_min):
                im_bin_resize.pixels[l][c] = self.pixels[l+l_min][c+c_min]
        return im_bin_resize

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        #création d'une nouvelle image
        im = Image()
        # affectation a l'image im d'un tableau de pixels new_H et new_W dont les intensites, 
        # de type uint8 (8bits non signes),sont mises a 0
        im.set_pixels(np.zeros((new_H, new_W), dtype=np.uint8))
        #redimensionnement et conversion de l'image grace à la fonction resize et np.uint8
        im.pixels = np.uint8(resize(self.pixels, (new_H,new_W), 0)*255)
        
        return im

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        res = 0
        proportion = 0
        if self.H==im.H and self.W==im.W:
            for l in range (self.H):
                for c in range(self.W) :
                    if self.pixels[l][c]==im.pixels[l][c]:
                        res += 1
        proportion = res / (self.H*self.W)                
        return proportion
                        

