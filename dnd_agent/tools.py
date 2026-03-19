import requests

from dnd_agent.constants import DND_BEYOND_URL
from dnd_agent.models import GetCharacterResponse


def get_character_sheet(character_id: int) -> GetCharacterResponse:
    """
    get_character_sheet: Returns the chracter sheet for the given character_id
        from DND Beyond

    Args:
        character_id: (int) This will be the DND beyond character ID for the users character

    Returns:
        Returns a GetCharacterResponse object which will contain a slimmed down version
        of the data representing the relevant information for the agent
    """

    try:
        response = requests.get(url=f"{DND_BEYOND_URL}{character_id}")
        character = GetCharacterResponse.model_validate(response.json())
        return character

    except:
        return GetCharacterResponse(
            success=False, message="Failed to retrive from service", data=None
        )
