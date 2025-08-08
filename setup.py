from setuptools import setup, find_packages

setup(
    name="folderagent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyMuPDF==1.23.8",
        "pytesseract==0.3.10", 
        "Pillow==10.1.0",
        "python-docx==1.1.0",
        "pywin32==306",
        "python-dotenv==1.0.0"
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"]
    }
)
