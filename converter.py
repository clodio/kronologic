import os
from PIL import Image

def convertir_png_en_webp(dossier_source, dossier_destination):
    """
    Convertit toutes les images PNG d'un dossier en images WebP.

    Args:
        dossier_source (str): Chemin du dossier contenant les images PNG.
        dossier_destination (str): Chemin du dossier où enregistrer les images WebP.
    """

    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    # Parcourir les fichiers du dossier source
    for nom_fichier in os.listdir(dossier_source):
        if nom_fichier.lower().endswith(".png"):
            chemin_source = os.path.join(dossier_source, nom_fichier)
            chemin_destination = os.path.join(dossier_destination, os.path.splitext(nom_fichier)[0] + ".webp")

            try:
                # Ouvrir l'image PNG avec Pillow
                image = Image.open(chemin_source)

                # Convertir et enregistrer l'image au format WebP
                image.save(chemin_destination, "webp")

                print(f"Converti : {nom_fichier} -> {os.path.basename(chemin_destination)}")

            except Exception as e:
                print(f"Erreur lors de la conversion de {nom_fichier} : {e}")

# Exemple d'utilisation
iters = [1,2,3,4,5,6,7]
for iter in iters:
    dossier_source = f"./\images/bijou_cantatrice_bonus_{iter}"  # Remplacez par le chemin de votre dossier PNG
    dossier_destination = f"./\images/bijou_cantatrice_bonus_{iter}"  # Remplacez par le chemin où vous voulez enregistrer les WebP

    convertir_png_en_webp(dossier_source, dossier_destination)
