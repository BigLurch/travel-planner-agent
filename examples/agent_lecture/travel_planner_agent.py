from langchain.agents import create_agent
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

from util.models import get_model
from examples.agent_lecture.travel_planner_prompt import TRAVEL_PLANNER_SYSTEM_PROMPT
from examples.agent_lecture.travel_planner_questions import (
    REQUIRED_FIELDS,
    get_missing_fields,
    get_next_question,
    update_profile,
)


console = Console()


def build_travel_summary(profile: dict) -> str:
    return f"""
Du ska skapa ett reseförslag för en person med följande profil:

- Resmål / typ av resa: {profile.get("destination", "Ej angivet")}
- Reslängd: {profile.get("duration", "Ej angivet")}
- Budget: {profile.get("budget", "Ej angivet")}
- Säsong / tidpunkt: {profile.get("season", "Ej angivet")}
- Resesällskap: {profile.get("travel_company", "Ej angivet")}
- Intressen: {profile.get("interests", "Ej angivet")}
- Tempo: {profile.get("pace", "Ej angivet")}

Skapa nu ett komplett reseförslag enligt instruktionerna.
""".strip()


def show_header():
    console.print(
        Panel.fit(
            "[bold cyan]🌍 Travel Planner Agent[/bold cyan]\n[white]Jag hjälper dig att planera din resa steg för steg.[/white]",
            border_style="cyan",
        )
    )
    console.print("[dim]Skriv 'avsluta' om du vill avsluta.[/dim]\n")


def show_question(question: str):
    console.print(
        Panel(
            f"[bold yellow]Fråga:[/bold yellow]\n{question}",
            title="Agent",
            border_style="yellow",
        )
    )


def show_result(result_text: str):
    console.print(
        Panel.fit(
            "[bold green]✈️  Ditt reseförslag är klart! [/bold green]",
            border_style="green",
        )
    )
    console.print()
    console.print(Markdown(result_text))
    console.print()


def run():
    model = get_model()

    agent = create_agent(
        model=model,
        system_prompt=TRAVEL_PLANNER_SYSTEM_PROMPT,
    )

    profile = {field: "" for field in REQUIRED_FIELDS}

    show_header()
    show_question(get_next_question(profile))

    while True:
        user_input = Prompt.ask("[bold blue]Du[/bold blue]").strip()

        if user_input.lower() in ["avsluta", "exit", "quit"]:
            console.print("\n[bold red]Hej då! Lycka till med resan.[/bold red]")
            break

        missing_fields = get_missing_fields(profile)

        if missing_fields:
            current_field = missing_fields[0]
            update_profile(profile, current_field, user_input)

        missing_fields = get_missing_fields(profile)

        if missing_fields:
            next_question = get_next_question(profile)
            console.print()
            show_question(next_question)
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

            console.print()
            show_result(assistant_message)

            console.print(
                Panel(
                    "[bold magenta]Vill du planera en ny resa?[/bold magenta]\nSvara på första frågan igen, eller skriv [bold]avsluta[/bold].",
                    title="Ny planering",
                    border_style="magenta",
                )
            )

            profile = {field: "" for field in REQUIRED_FIELDS}
            console.print()
            show_question(get_next_question(profile))


if __name__ == "__main__":
    run()