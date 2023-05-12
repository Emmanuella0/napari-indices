"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget
from napari.types import ImageData, LabelsData
import spectral.io.envi as envi
import numpy as np
import matplotlib.pyplot as plt
import tifffile as tiff

if TYPE_CHECKING:
    import napari


class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)

    def _on_click(self):
        print("napari has", len(self.viewer.layers), "layers")


def indices(file):
    # Ouvrir le fichier
    img = tiff.imread(file)
    
    # Charger les informations sur les longueurs d'onde
    header = spectral.envi.read_envi_header(r'C:\Users\EMMANUELLA\Documents\vert_emmanuella_8600_us_2x_2023-04-25T153039_corr_rad.hdr')
    wavelengths = header['wavelength']
    
    # Nombre de bandes et dimensions de l'image
    b, h, w = img.shape
    
    # Affichage de toutes les bandes avec leurs longueurs d'onde
    for i in range(b):
       plt.imshow(img[i], cmap='gray')
       plt.title(f"Bande {i+1} - Longueur d'onde : {wavelengths[i]} nm")
       plt.axis('off')
       plt.show()
    
    # Demander à l'utilisateur de choisir les bandes
    while True:
       red_band = int(input("Sélectionnez la bande rouge (indice entre 1 et %d) : " % b))
       if red_band < 1 or red_band > b:
           print("Bande invalide. Veuillez réessayer.")
           continue
       else:
           break
   
    while True:
       nir_band = int(input("Sélectionnez la bande proche infra-rouge (indice entre 1 et %d) : " % b))
       if nir_band < 1 or nir_band > b:
           print("Bande invalide. Veuillez réessayer.")
           continue
       else:
           break
   
    while True:
       green_band = int(input("Sélectionnez la bande verte (indice entre 1 et %d) : " % b))
       if green_band < 1 or green_band > b:
           print("Bande invalide. Veuillez réessayer.")
           continue
       else:
           break
   
    while True:
       blue_band = int(input("Sélectionnez la bande bleue (indice entre 1 et %d) : " % b))
       if blue_band < 1 or blue_band > b:
           print("Bande invalide. Veuillez réessayer.")
           continue
       else:
           break
   
    # Extraire les bandes sélectionnées
    red = img[red_band - 1]
    nir = img[nir_band - 1]
    green = img[green_band - 1]
    blue = img[blue_band-1]
    
    # Demander à l'utilisateur de choisir un indice
    while True:
        indice = input("Choisissez un indice (NDVI, TCARI, NPCI) : ")
        if indice not in ["NDVI", "TCARI", "NPCI"]:
            print("Indice invalide. Veuillez réessayer.")
            continue
        else:
            break
    
    # Calculer et afficher l'indice choisi
    if indice == "NDVI":
        ndvi = calculate_ndvi(red, nir)
        return ndvi
    elif indice == "TCARI":
        tcari = calculate_tcari(red, green, blue)
        return tcari
    elif indice == "NPCI":
        npci = calculate_npci(red, green)
        return npci

def calculate_ndvi(red, nir):
    # Calculer la NDVI
    ndvi = (nir - red) / (nir + red)
    
    # Afficher l'image de la NDVI avec un titre
    plt.imshow(ndvi, cmap='gray')
    plt.title("NDVI")
    plt.axis('off')
    plt.show()
    
    # Retourner l'image de la NDVI
    return ndvi

def calculate_tcari(red, green, blue):
    # Calculer le TCARI
    tcari = 3 * ((red - green) - 0.2 * (red - blue))
    
    # Afficher l'image du TCARI avec un titre
    plt.imshow(tcari, cmap='gray')
    plt.title("TCARI")
    plt.axis('off')
    plt.show()
    
    # Retourner l'image du TCARI
    return tcari

def calculate_npci(red, green):
    # Calculer le NPCI
    npci = (green - red) / (green + red)
    
    # Afficher l'image du NPCI avec un titre
    plt.imshow(npci, cmap='gray')
    plt.title("NPCI")
    plt.axis('off')
    plt.show()
    
    # Retourner l'image du NPCI
    return npci


@magic_factory(call_button=["Run NDVI", "Run TCARI", "Run NPCI"])
def calculate_indice(image_layer: ImageData, red_band: int = 0, nir_band: int = 0: green_band:int = 0, blue_band: int = 0) -> ImageData:

# widget = QWidget()
# layout = QHBoxLayout()
# button_select_bands = QPushButton("Select Bands")
# button_run_ndvi = QPushButton("Run NDVI")

ndvi = None
tcari = None
npci = None

if red_band == 0 or nir_band == 0 or blue_band == 0 or green_band == 0:
    print("select correct band")
    #*red, nir = select_bands(image_layer.data)
else:
    red = image_layer[red_band - 1,:,:]
    nir = image_layer[nir_band - 1,:,:]
    green = image_layer[green_band - 1,:,:]
    blue = image_layer[blue_band - 1,:,:]

    ndvi = calculate_ndvi(red, nir)
    tcari = calculate_tcari(red, green, blue)
    npci = calculate_npci(red, green)
    print(ndvi.shape)
    print(tcari.shape)
    print(npci.shape)
    return ndvi, tcari, npci
#button_select_bands.clicked.connect(select_bands_and_calculate_ndvi)
#button_run_ndvi.clicked.connect(select_bands_and_calculate_ndvi)

#layout.addWidget(button_select_bands)
#layout.addWidget(button_run_ndvi)
#widget.setLayout(layout)


