from langchain.agents import create_agent

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input

from .travel_planner_prompt import TRAVEL_PLANNER_SYSTEM_PROMPT


def run():
    model = get_model()

    agent = create_agent(
        model=model,
        system_prompt=TRAVEL_PLANNER_SYSTEM_PROMPT,
    )

    print("=== Travel Planner Agent ===")
    print("Jag hjälper dig att planera en resa steg för steg.")
    print("Skriv 'avsluta' om du vill avsluta.\n")

    messages = []

    while True:
        user_input = input("Du: ").strip()

        if user_input.lower() in ["avsluta", "exit", "quit"]:
            print("Agent: Tack! Ha en fin dag.")
            break

        messages.append({"role": "user", "content": user_input})

        response = agent.invoke({"messages": messages})

        assistant_message = response["messages"][-1].content
        print(f"\nAgent: {assistant_message}\n")

        messages.append({"role": "assistant", "content": assistant_message})


if __name__ == "__main__":
    run()