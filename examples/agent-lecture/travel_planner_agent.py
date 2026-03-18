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

    user_input = get_user_input("Beskriv din resa eller ställ en resefråga")

    process_stream = agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        stream_mode=STREAM_MODES,
    )

    handle_stream(process_stream, agent_name="Travel Planner Agent")


if __name__ == "__main__":
    run()