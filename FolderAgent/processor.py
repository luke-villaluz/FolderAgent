import os
import fitz
import pytesseract
from PIL import Image
from docx import Document
import io


class PDFExtractor:
    def extract(self, file_path):
        try:
            doc = fitz.open(file_path)
            text_content = []
            
            for page_num, page in enumerate(doc, 1):
                text = page.get_text()
                if not text.strip():
                    # Only try OCR if tesseract is available
                    if hasattr(self, 'tesseract_available') and self.tesseract_available:
                        try:
                            print(f"Page {page_num}: No text found, attempting OCR...")
                            mat = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                            img = Image.open(io.BytesIO(mat.tobytes("png")))
                            text = pytesseract.image_to_string(img)
                            print(f"Page {page_num} OCR extracted: {len(text)} chars")
                        except Exception as e:
                            print(f"OCR failed for page {page_num}: {e}")
                            text = ""
                    else:
                        print(f"Page {page_num}: No text found, OCR unavailable")
                        text = ""
                else:
                    print(f"Page {page_num} text extracted: {len(text)} chars")
                
                text_content.append(text)
            
            doc.close()
            return '\n'.join(text_content)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return ""


class DocxExtractor:
    def extract(self, file_path):
        try:
            doc = Document(file_path)
            return '\n'.join([p.text for p in doc.paragraphs])
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return ""


class FolderScanner:
    def __init__(self):
        # Check if tesseract is available in PATH
        try:
            import pytesseract
            pytesseract.get_tesseract_version()
            self.tesseract_available = True
            print("Tesseract found - OCR enabled")
        except Exception as e:
            self.tesseract_available = False
            print("Warning: Tesseract not found in PATH - OCR will be unavailable")
        
        self.extractors = {
            '.pdf': PDFExtractor(),
            '.docx': DocxExtractor()
        }
        # Pass tesseract availability to PDF extractor
        self.extractors['.pdf'].tesseract_available = self.tesseract_available
    
    def scan_folder(self, folder_path):
        print(f"Scanning folder: {folder_path}")
        results = {
            'files_processed': 0,
            'total_text_length': 0,
            'combined_text': "",
            'failed_files': []
        }
        
        file_texts = []
        
        for root, dirs, files in os.walk(folder_path):
            print(f"Root: {root}, Files: {files}")
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                
                if file.endswith(('.pdf', '.docx')):
                    text = self._extract_text(file_path)
                    print(f"Extracted text length: {len(text)}")
                    
                    if text.strip():
                        results['files_processed'] += 1
                        results['total_text_length'] += len(text)
                        file_texts.append(text)
                    else:
                        results['failed_files'].append(file_path)
        
        results['combined_text'] = '\n\n'.join(file_texts)
        print(f"Total files processed: {results['files_processed']}")
        return results
    
    def _extract_text(self, file_path):
        ext = os.path.splitext(file_path)[1]
        extractor = self.extractors.get(ext)
        return extractor.extract(file_path) if extractor else ""
    
    def get_combined_text(self, folder_path):
        results = self.scan_folder(folder_path)
        return results['combined_text']