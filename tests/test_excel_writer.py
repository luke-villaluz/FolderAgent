import pytest
import os
from FolderAgent.excel_writer import ExcelWriter

def test_excel_writer():
    # Mock JSON response from LLM
    mock_json_response = {
        "cool_fact": "I've seen 46 states",
        "most_common_topic": "traveling", 
        "summary_in_one_sentence": "Luke is a chill dude who loves traveling"
    }
    
    # Test-specific output path (overrides .env OUTPUT)
    test_output_path = "tests/test_output.xlsx"
    
    print("Testing Excel Writer")
    print("=" * 50)
    print(f"Mock JSON: {mock_json_response}")
    print("-" * 30)
    
    # Override the default OUTPUT path for testing
    excel_writer = ExcelWriter(test_output_path)
    
    # Test creating Excel with subfolder data
    excel_writer.process_subfolder("test_folder", mock_json_response)
    
    print(f"Excel file created: {test_output_path}")
    print("-" * 30)
    
    # Verify file exists
    assert os.path.exists(test_output_path)
    
    # DON'T delete the file - let you see it
    print("Excel file created successfully - check tests/test_output.xlsx")
    print("All assertions passed")

if __name__ == "__main__":
    test_excel_writer()
