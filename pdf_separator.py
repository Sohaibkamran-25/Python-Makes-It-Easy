import os
import zipfile
from pypdf import PdfReader, PdfWriter

def split_pdf_and_zip(input_pdf_path, zip_name):
    # 1. Initialize the Reader
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    
    # Create a temporary directory for individual files
    temp_dir = "split_pages"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    pdf_files = []

    print(f"Splitting {total_pages} pages...")

    # 2. Extract each page
    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        
        output_filename = os.path.join(temp_dir, f"Certificate_Page_{i+1}.pdf")
        with open(output_filename, "wb") as out_file:
            writer.write(out_file)
        pdf_files.append(output_filename)

    # 3. Create the Zip file
    print(f"Creating {zip_name}...")
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in pdf_files:
            zipf.write(file, os.path.basename(file))
            # Clean up the individual file after adding to zip
            os.remove(file)

    # Clean up the temporary directory
    os.rmdir(temp_dir)
    print(f"Success! All {total_pages} pages are saved in {zip_name}")

# --- SETTINGS ---
file_to_split = "Certificate.pdf"  # Replace with your actual filename
output_zip = "Certificates_Bundle.zip"

split_pdf_and_zip(file_to_split, output_zip)