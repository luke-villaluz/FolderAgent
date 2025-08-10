import requests
import json
from FolderAgent.config import PERPLEXITY_API_KEY, PERPLEXITY_MODEL, PERPLEXITY_BASE_URL


class LLMClient:
    #change as needed for different LLMs
    def __init__(self, api_key=None, model=None, base_url=None):
        self.api_key = api_key or PERPLEXITY_API_KEY
        self.model = model or PERPLEXITY_MODEL
        self.base_url = base_url or PERPLEXITY_BASE_URL
    
    def send_prompt(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except KeyError as e:
            raise Exception(f"Unexpected API response format: {e}")
    
    def get_json_response(self, prompt):
        response_text = self.send_prompt(prompt)
        
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            raise Exception("LLM response is not valid JSON")
