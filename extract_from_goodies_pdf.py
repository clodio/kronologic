import fitz  # PyMuPDF
from PIL import Image
import os


def extract_images_from_pdf(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    images = []
    
    doc = fitz.open(pdf_path)
    for page_number in range(len(doc)):
        for img_index, img in enumerate(doc[page_number].get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            img_ext = base_image["ext"]
            img_path = os.path.join(output_folder, f"page_{page_number}_img_{img_index}.{img_ext}")
            with open(img_path, "wb") as f:
                f.write(img_bytes)
            images.append(img_path)
    
    return images

def split_image(image_path, output_folder, crop_positions, crop_size,bonus):
    os.makedirs(output_folder, exist_ok=True)
    img = Image.open(image_path)
    width, height = img.size
    cropped_images = []
    for idx, (x, y) in enumerate(crop_positions):
        if x + crop_size[0] <= width and y + crop_size[1] <= height:
            cropped = img.crop((x, y, x + crop_size[0], y + crop_size[1]))
            folder_tmp = output_folder + f"/bijou_cantatrice_bonus_{bonus}" + "/"
            os.makedirs(folder_tmp, exist_ok=True)
            page_number = os.path.basename(image_path).split('_img')[0].split("page_")[1]
            if int(page_number) % 2:
                if idx == 0:
                    new_idx = 5
                if idx == 1:
                    new_idx = 6
                if idx == 2:
                    new_idx = 3
                if idx == 3:
                    new_idx = 5
                if idx == 4:
                    new_idx = 4
                if idx == 5:
                    new_idx = 1
                if idx == 6:
                    new_idx = 2
                if idx == 3:
                    crop_path = os.path.join(folder_tmp, "scenario.png")
                else:
                    crop_path = os.path.join(folder_tmp, f"place{new_idx}-informations.png")
                
            else:
                new_idx = 6 - idx
                if idx > 3: 
                    new_idx = new_idx + 1
                if idx == 3:
                    crop_path = os.path.join(folder_tmp, f"setup.png")
                else:
                    crop_path = os.path.join(folder_tmp, f"place{new_idx}.png")
            cropped.save(crop_path)
            cropped_images.append(crop_path)
    
    return cropped_images

# Exemple d'utilisation
pdf_path = "./enquetes/Export_Sc_III_EN.pdf"
output_folder = "enquetes_output"
crop_output_folder = "cropped_images"
# Pour pdf francais
crop_size = (372, 520)  # Largeur et hauteur de chaque sous-image
crop_positions = [(239, 80),(628, 80),(43, 618),(433, 618),(824, 618),(239, 1156),(628, 1156)]

# Pour pdf anglais
crop_size = (750, 1039)  # Largeur et hauteur de chaque sous-image
crop_positions = [(479, 155),(1251, 155),(84, 1233),(865, 1233),(1642, 1233),(479, 2312),(1251, 2312)]

# Étape 1 : Extraire les images du PDF
extracted_images = extract_images_from_pdf(pdf_path, output_folder)

bonus = 0
files = 1
# Étape 2 : Découper chaque image extraite
for img_path in extracted_images:
    if files % 2:
         bonus=bonus+1
    split_image(img_path, crop_output_folder, crop_positions, crop_size, bonus)
    files=files+1

