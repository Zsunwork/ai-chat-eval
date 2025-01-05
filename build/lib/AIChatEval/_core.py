from ._persona import Persona
from ._conversation import Conversation

class AIChatEval:
    def __init__(self, key: str):
        """
        Initialize the AIChatEval module with an API key.
        """
        self.api_key = key

    def persona(self, description: str) -> dict:
        """
        Generate a persona description.

        Args:
            description (str): Description of the persona.

        Returns:
            dict: Generated persona data.
        """
        persona = Persona(api_key=self.api_key)
        return persona.build(description)

    def conversation(self, persona: dict):
        """
        Initialize a conversation agent with the given persona.

        Args:
            persona (dict): Persona data to base the conversation on.

        Returns:
            Conversation: A conversation object for generating responses.
        """
        return Conversation(persona, api_key=self.api_key)
