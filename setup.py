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
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "openpyxl==3.1.2",
        "pandas==2.1.4"
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"]
    }
)
