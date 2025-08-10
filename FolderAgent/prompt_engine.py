"""
Prompt engine for formatting text into LLM prompts.
"""
import os
from FolderAgent.config import PROMPT


class PromptEngine:
    def __init__(self, prompts_dir="prompts"):
        self.prompts_dir = prompts_dir
    
    def load_prompt_template(self, template_name=None):
        """Load a prompt template from the prompts directory."""
        if template_name is None:
            template_name = PROMPT
        
        template_path = os.path.join(self.prompts_dir, template_name)
        
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt template not found: {template_path}")
    
    def format_prompt(self, combined_text, template_name=None):
        """Format the prompt template with the combined text."""
        template = self.load_prompt_template(template_name)
        
        # Replace the placeholder with actual text
        formatted_prompt = template.replace("{COMBINED_TEXT}", combined_text)
        
        return formatted_prompt
    
    def get_formatted_prompt(self, combined_text):
        """Get a formatted prompt ready for the LLM client."""
        return self.format_prompt(combined_text)
