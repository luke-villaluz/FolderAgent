import os
import fitz
import pytesseract
from PIL import Image
from docx import Document
import win32com.client
import pythoncom
import io


class FolderScanner:
    def __init__(self, tesseract_path=None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self.word_app = None
    
    def scan_folder(self, folder_path):
        print(f"Scanning folder: {folder_path}")
        results = {
            'files_processed': 0,
            'total_text_length': 0,
            'combined_text': "",
            'failed_files': []
        }
        
        file_texts = []
        
        try:
            for root, dirs, files in os.walk(folder_path):
                print(f"Root: {root}, Files: {files}")
                for file in files:
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    
                    if file.endswith(('.pdf', '.doc', '.docx')):
                        text = self._extract_text(file_path)
                        print(f"Extracted text length: {len(text)}")
                        
                        if text.strip():
                            results['files_processed'] += 1
                            results['total_text_length'] += len(text)
                            file_texts.append(text)
                        else:
                            results['failed_files'].append(file_path)
        
        finally:
            self._cleanup_word()
        
        results['combined_text'] = '\n\n'.join(file_texts)
        print(f"Total files processed: {results['files_processed']}")
        return results
    
    def _extract_text(self, file_path):
        if file_path.endswith('.pdf'):
            return self._extract_pdf(file_path)
        elif file_path.endswith('.docx'):
            return self._extract_docx(file_path)
        elif file_path.endswith('.doc'):
            return self._extract_doc(file_path)
        return ""
    
    def _extract_pdf(self, file_path):
        try:
            doc = fitz.open(file_path)
            text_content = []
            
            for page in doc:
                text = page.get_text()
                if not text.strip():
                    mat = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    img = Image.open(io.BytesIO(mat.tobytes("png")))
                    text = pytesseract.image_to_string(img)
                text_content.append(text)
            
            doc.close()
            return '\n'.join(text_content)
        except:
            return ""
    
    def _extract_docx(self, file_path):
        try:
            doc = Document(file_path)
            return '\n'.join([p.text for p in doc.paragraphs])
        except:
            return ""
    
    def _extract_doc(self, file_path):
        if not self.word_app:
            self._init_word()
        
        try:
            doc = self.word_app.Documents.Open(file_path)
            text = doc.Content.Text
            doc.Close()
            return text
        except:
            return ""
    
    def _init_word(self):
        try:
            pythoncom.CoInitialize()
            self.word_app = win32com.client.Dispatch("Word.Application")
            self.word_app.Visible = False
        except:
            self.word_app = None
    
    def _cleanup_word(self):
        if self.word_app:
            try:
                self.word_app.Quit()
                pythoncom.CoUninitialize()
            except:
                pass
    
    def get_combined_text(self, folder_path):
        results = self.scan_folder(folder_path)
        return results['combined_text']