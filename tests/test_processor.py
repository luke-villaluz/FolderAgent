import pytest
import os
from FolderAgent.processor import FolderScanner

def test_folder_scanner():
    folder_scanner = FolderScanner()
    test_folder = "tests/test_folder"
    
    print("Testing Folder Scanner")
    print("=" * 50)
    print(f"Test folder: {test_folder}")
    print("-" * 30)
    
    results = folder_scanner.scan_folder(test_folder)
    
    print("Results:")
    print(results)
    print("-" * 30)
    
    assert isinstance(results, dict)
    assert 'files_processed' in results
    assert 'combined_text' in results
    assert 'failed_files' in results
    assert isinstance(results['files_processed'], int)
    assert isinstance(results['combined_text'], str)
    
    print("All assertions passed")

if __name__ == "__main__":
    test_folder_scanner()
