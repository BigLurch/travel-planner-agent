# Travel Planner Agent (LangChain)

En AI-agent byggd med LangChain som hjälper dig att planera resor steg för steg ✈️

Agenten samlar först in information om din resa och genererar sedan ett komplett reseförslag med aktiviteter, turer och packningslista.

---

## Funktioner

* 🧠 Interaktiv agent som ställer frågor
* 📋 Samlar in reseinformation (budget, resmål, intressen m.m.)
* 🗺️ Genererar färdiga reseplaner
* 🎒 Skapar packningsförslag
* ✨ Snygg terminal-UI med `rich`
* ⚙️ Byggd med LangChain

---

## Hur agenten fungerar

Agenten arbetar i två steg:

### 1. Datainsamling

Agenten ställer frågor om:

* resmål
* reslängd
* budget
* säsong
* resesällskap
* intressen
* tempo

### 2. Generering av reseplan

När all information är insamlad:

* skickas datan till en LLM via LangChain
* ett strukturerat reseförslag genereras

---

## Installation

### 1. Klona projektet

```bash
git clone https://github.com/DITT-NAMN/travel-planner-agent.git
cd travel-planner-agent
```

### 2. Skapa virtuell miljö

```bash
python -m venv .venv
```

Aktivera:

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. Installera dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Installera extra (för UI)

```bash
pip install rich
```

---

### 5. Skapa .env

```bash
cp .env.example .env
```

Fyll i:

```env
OLLAMA_BASE_URL=http://nackademin.icedc.se
OLLAMA_BEARER_TOKEN=DIN_TOKEN_HÄR
```

---

## Kör agenten

```bash
python -m examples.agent_lecture.travel_planner_agent
```

---

## Exempel

**Användare:**

```
Jag vill resa i sommar
```

**Agent:**

```
Vilket resmål tänker du dig?
```

Efter några frågor får du:

* 🌍 Sammanfattning
* 📍 Sevärdheter
* 🗺️ Dagsplan
* 🎒 Packningslista
* 💡 Tips

---

## Teknisk design

Agenten kombinerar:

* **LangChain** → för textgenerering
* **Systemprompt** → styr struktur och stil
* **Python-logik** → styr vilka frågor som ställs
* **Rich** → förbättrar UI i terminalen

---

## Projektstruktur

```
examples/
├── agent_lecture/
|   ├── travel_planner_agent.py
|   ├── travel_planner_prompt.py
|   └── travel_planner_questions.py
├── util/
│   ├── embeddings.py
│   ├── models.py
│   ├── streaming_utils.py
│   ├── tools.py
│   └── pretty_print.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

## Syfte

Detta projekt är skapat som en del av en MLOps/AI-kurs och demonstrerar:

* hur man bygger en AI-agent med LangChain
* hur man kombinerar LLM + programlogik
* hur man skapar en strukturerad systemprompt
* hur man bygger en interaktiv CLI-applikation

---

## Möjliga förbättringar

* Spara reseplaner till fil (Markdown/PDF)
* Integrera riktiga API:er (väder, flyg, hotell)
* Webbaserat UI
* Fler personliga rekommendationer

---

## Författare

Skapad av Jonas Johansson som en del av kursprojekt.