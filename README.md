# 🖼️ Image to PDF Converter

A simple Python script that converts multiple images into a single PDF using **Pillow** and **FPDF**.

---

## 🚀 Features

- 🖼️ Converts `.jpg`, `.jpeg`, `.png` images into PDF
- 🗃️ Merges all images into a single multipage PDF
- 🔢 Maintains image order (sorted by filename)
- 🧼 Cleans up temporary files (if needed)

---

## 📂 Folder Setup

> ⚠️ **Important:** You need to **manually create** the following folders in the same directory as the script **before running it**:

- `images/` — Place all your input images here
- `output/` — The final PDF will be saved here

Example structure:


---

## 🛠️ Requirements

Install required libraries using:

```bash
pip install pillow fpdf


python script.py


python script.py --input my_images --output my_pdfs --name vacation_album.pdf
