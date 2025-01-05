from ._persona import BuildPersona, BuildPersonaError
from ._conversation import Conversation
from typing import Optional, Union

class PersonaError(Exception):
    """Custom exception for persona-related errors"""
    pass

class Persona:
    def __init__(self, name: str, background: str, target: str, additional_info: str):
        self.name = name
        self.background = background
        self.target = target
        self.additional_info = additional_info

class Client:
    def __init__(self, key: str):
        """
        Initialize the AIChatEval module with an API key.
        """
        if not key:
            raise PersonaError("API key cannot be empty")
        self.api_key = key

    def build_persona(self, description: str) -> Union[Persona, PersonaError]:
        """
        Generate a persona description.

        Args:
            description (str): Description of the persona.

        Returns:
            Union[Persona, PersonaError]: Generated persona object or error.
        """
        try:
            if not description:
                raise PersonaError("Description cannot be empty")

            persona_builder = BuildPersona(api_key=self.api_key)
            persona_data = persona_builder.build(description)
            
            return Persona(
                name=persona_data.get("name", ""),
                additional_info=persona_data.get("additional_info", ""),
                background=persona_data.get("background", ""),
                target=persona_data.get("target", ""),
            )
        except BuildPersonaError as e:
            raise PersonaError(f"Failed to build persona: {str(e)}")
        except Exception as e:
            raise PersonaError(f"Unexpected error: {str(e)}")

    def conversation(self, persona: Persona):
        """
        Initialize a conversation agent with the given persona.

        Args:
            persona (Persona): Persona object to base the conversation on.

        Returns:
            Conversation: A conversation object for generating responses.
        """
        try:
            if not isinstance(persona, Persona):
                raise PersonaError("Invalid persona object")
            return Conversation(persona.__dict__, api_key=self.api_key)
        except Exception as e:
            raise PersonaError(f"Failed to create conversation: {str(e)}")
