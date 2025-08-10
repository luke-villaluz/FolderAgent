"""
Main orchestration for FolderAgent document processing.
"""
import os
from FolderAgent.config import INPUT, OUTPUT
from FolderAgent.processor import FolderScanner
from FolderAgent.prompt_engine import PromptEngine
from FolderAgent.llm_client import LLMClient
from FolderAgent.excel_writer import ExcelWriter

def main():
    print(f"Starting FolderAgent")
    print(f"INPUT: {INPUT}")
    print(f"OUTPUT: {OUTPUT}")
    
    # Initialize components
    scanner = FolderScanner()
    prompt_engine = PromptEngine()
    llm_client = LLMClient()
    excel_writer = ExcelWriter(OUTPUT)
    
    # Get input folder from config
    if not INPUT:
        raise ValueError("INPUT path not set in .env")
    
    if not os.path.exists(INPUT):
        raise ValueError(f"Input folder does not exist: {INPUT}")
    
    print(f"Processing folder: {INPUT}")
    print(f"Output Excel: {OUTPUT}")
    print("-" * 50)
    
    # Process each subfolder individually
    subfolders = os.listdir(INPUT)
    print(f"Found {len(subfolders)} items in INPUT")
    
    for subfolder in subfolders:
        subfolder_path = os.path.join(INPUT, subfolder)
        
        if not os.path.isdir(subfolder_path):
            continue
            
        print(f"Processing subfolder: {subfolder}")
        
        try:
            # Scan subfolder and extract text
            scan_results = scanner.scan_folder(subfolder_path)
            print(f"Extracted {scan_results['files_processed']} files ({scan_results['total_text_length']} chars)")
            
            if not scan_results['combined_text'].strip():
                print(f"No text extracted from {subfolder}")
                continue
                
            # Format prompt with extracted text
            formatted_prompt = prompt_engine.format_prompt(scan_results['combined_text'])
            print(f"Prompt length: {len(formatted_prompt)} chars")
            
            # Get LLM response
            print(f"Calling LLM...")
            json_response = llm_client.get_json_response(formatted_prompt)
            print(f"LLM response: {json_response}")
            
            # Write to Excel
            excel_writer.process_subfolder(subfolder, json_response)
            print(f"Added to Excel: {subfolder}")
            
        except Exception as e:
            print(f"Error processing {subfolder}: {e}")
            continue
            
        print("-" * 30)
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
