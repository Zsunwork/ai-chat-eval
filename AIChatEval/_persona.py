from pydantic import BaseModel
from openai import OpenAI
import json
from typing import Dict, Optional, Union

class PersonaFormat(BaseModel):
    name: str
    background: str
    target: str
    additional_info: str

class BuildPersonaError(Exception):
    """Custom exception for persona building errors"""
    pass

class BuildPersona:
    def __init__(self, api_key: str):
        try:
            self.api_key = api_key
            self.client = OpenAI(api_key=api_key)
        except Exception as e:
            raise BuildPersonaError(f"Failed to initialize OpenAI client: {str(e)}")

    def build(self, description: str) -> Union[Dict, BuildPersonaError]:
        """
        Generate a persona based on the given description.

        Args:
            description (str): Description of the target persona.

        Returns:
            Union[Dict, BuildPersonaError]: Generated persona attributes or error.
        """
        try:
            persona_format_schema = PersonaFormat.model_json_schema()

            messages = [
                {
                    "role": "system",
                    "content": "You are an AI assistant that creates detailed personas. Generate a persona with a name, description, background, and target behavior."
                },
                {
                    "role": "user",
                    "content": f"Create a persona based on this description: {description}"
                }
            ]

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Persona",
                        "description": "Generate a detailed persona with name, background, target behavior, and additional info",
                        "schema": persona_format_schema
                    }
                }
            )

            persona_data = json.loads(response.choices[0].message.content)
            
            return {
                "name": persona_data["name"],
                "additional_info": persona_data["additional_info"],
                "background": persona_data["background"],
                "target": persona_data["target"]
            }

        except json.JSONDecodeError as e:
            raise BuildPersonaError(f"Failed to parse API response: {str(e)}")
        except Exception as e:
            raise BuildPersonaError(f"Error building persona: {str(e)}")
