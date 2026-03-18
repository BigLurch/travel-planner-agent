from langchain.agents import create_agent

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input

from .travel_planner_prompt import TRAVEL_PLANNER_SYSTEM_PROMPT
from examples.agent_lecture.travel_planner_questions import (
    REQUIRED_FIELDS,
    get_missing_fields,
    get_next_question,
    update_profile,
)


def build_travel_summary(profile: dict) -> str:
    return f"""
Här är informationen som användaren har gett:

- Resmål / typ av resa: {profile.get("destination", "Ej angivet")}
- Reslängd: {profile.get("duration", "Ej angivet")}
- Budget: {profile.get("budget", "Ej angivet")}
- Säsong / tidpunkt: {profile.get("season", "Ej angivet")}
- Resesällskap: {profile.get("travel_company", "Ej angivet")}
- Intressen: {profile.get("interests", "Ej angivet")}
- Tempo: {profile.get("pace", "Ej angivet")}

Skapa nu ett komplett reseförslag enligt instruktionerna.
""".strip()


def run():
    model = get_model()

    agent = create_agent(
        model=model,
        system_prompt=TRAVEL_PLANNER_SYSTEM_PROMPT,
    )

    profile = {field: "" for field in REQUIRED_FIELDS}
    current_field_index = 0

    print("=== Travel Planner Agent ===")
    print("Jag hjälper dig att planera en resa steg för steg.")
    print("Skriv 'avsluta' om du vill avsluta.\n")

    print("Agent:", get_next_question(profile))

    while True:
        user_input = input("Du: ").strip()

        if user_input.lower() in ["avsluta", "exit", "quit"]:
            print("Agent: Tack! Lycka till med resplaneringen.")
            break

        missing_fields = get_missing_fields(profile)

        if missing_fields:
            current_field = missing_fields[0]
            update_profile(profile, current_field, user_input)

        missing_fields = get_missing_fields(profile)

        if missing_fields:
            next_question = get_next_question(profile)
            print(f"\nAgent: {next_question}\n")
        else:
            final_prompt = build_travel_summary(profile)

            response = agent.invoke(
                {
                    "messages": [
                        {"role": "user", "content": final_prompt}
                    ]
                }
            )

            assistant_message = response["messages"][-1].content

            print("\nAgent: Här kommer ditt reseförslag:\n")
            print(assistant_message)
            print("\n---\n")
            print("Agent: Vill du planera en ny resa? Skriv gärna igen, eller skriv 'avsluta'.\n")

            profile = {field: "" for field in REQUIRED_FIELDS}
            print("Agent:", get_next_question(profile))


if __name__ == "__main__":
    run()