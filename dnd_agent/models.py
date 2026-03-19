from pydantic import BaseModel


class Stat(BaseModel):
    id: int
    value: int | None

class ClassDefinition(BaseModel):
    name: str
    description: str
    cardDescription: str


class Class(BaseModel):
    definition: ClassDefinition
    subClassDefinition: ClassDefinition


class Race(BaseModel):
    fullName: str
    description: str


class BackgroundDefinition(BaseModel):
    name: str
    shortDescription: str


class Background(BaseModel):
    definition: BackgroundDefinition


class GetCharacterData(BaseModel):
    id: str
    username: str
    readOnlyUrl: str
    name: str
    baseHitPoints: int
    currentXp: int
    stats: list[Stat]
    bonusStats: list[Stat]
    race: Race
    classes: list[]


class GetCharacterResponse(BaseModel):
    success: bool
    message: str
    data: GetCharacterData
