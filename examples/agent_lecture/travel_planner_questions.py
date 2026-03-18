REQUIRED_FIELDS = [
    "destination",
    "duration",
    "budget",
    "season",
    "travel_company",
    "interests",
    "pace",
]

QUESTION_MAP = {
    "destination": "Vilket resmål tänker du dig, eller vilken typ av resa vill du göra?",
    "duration": "Hur länge vill du vara borta?",
    "budget": "Vilken ungefärlig budget har du för resan?",
    "season": "När ska du resa, eller vilken säsong gäller det?",
    "travel_company": "Reser du ensam, med partner, vänner eller familj?",
    "interests": "Vad gillar du mest på resor, till exempel storstad, mat, natur, sol och bad, kultur eller äventyr?",
    "pace": "Vilket tempo vill du ha på resan: lugnt, medel eller intensivt?",
}


def get_missing_fields(profile: dict) -> list[str]:
    missing = []
    for field in REQUIRED_FIELDS:
        value = profile.get(field, "").strip()
        if not value:
            missing.append(field)
    return missing


def get_next_question(profile: dict) -> str | None:
    missing_fields = get_missing_fields(profile)
    if not missing_fields:
        return None

    next_field = missing_fields[0]
    return QUESTION_MAP[next_field]


def update_profile(profile: dict, field: str, answer: str) -> dict:
    profile[field] = answer.strip()
    return profile