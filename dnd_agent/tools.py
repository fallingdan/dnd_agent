import requests

from dnd_agent.models import GetCharacterResponse


def get_character_sheet(character_id: int) -> GetCharacterResponse:

    requests.get(url="")

    return GetCharacterResponse(status="error", error_message="Something went wrong")
