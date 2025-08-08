import pytest
import os
from FolderAgent.processor import FolderScanner
from dotenv import load_dotenv

load_dotenv()

def test_folder_scanner():
    folder_scanner = FolderScanner()
    test_folder = os.getenv("TEST_INPUT")
    
    results = folder_scanner.scan_folder(test_folder)
    
    # Real assertions
    assert isinstance(results, dict)
    assert 'files_processed' in results
    assert 'combined_text' in results
    assert 'failed_files' in results
    assert isinstance(results['files_processed'], int)
    assert isinstance(results['combined_text'], str)
