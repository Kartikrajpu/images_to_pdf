import os
from PIL import Image
from fpdf import FPDF

def convert_images_to_pdf(input_folder="images", output_folder="output", pdf_name="output.pdf"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files from input folder
    image_files = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(os.path.join(input_folder, file))

    if not image_files:
        print("No images found in the 'images' folder!")
        return

    # Sort images by name
    image_files.sort()

    # Create PDF
    pdf = FPDF()
    
    for image_path in image_files:
        img = Image.open(image_path)
        
        # Convert image to RGB if it's in RGBA (to avoid errors with JPEG)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Save as temporary file if it was PNG
        temp_path = None
        if image_path.lower().endswith('.png'):
            temp_path = "temp.jpg"
            img.save(temp_path, "JPEG")
            img_path_for_pdf = temp_path
        else:
            img_path_for_pdf = image_path
        
        # Add image to PDF
        pdf.add_page()
        pdf.image(img_path_for_pdf, x=10, y=10, w=190)  # Adjust dimensions as needed
        
        # Remove temporary file if created
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

    # Save PDF
    output_path = os.path.join(output_folder, pdf_name)
    pdf.output(output_path)
    print(f"PDF created successfully at: {output_path}")

if __name__ == "__main__":
    convert_images_to_pdf()