# Decision Lab

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/status-under%20utvikling-yellow)
![Lisens](https://img.shields.io/badge/lisens-MIT-green)

**Status:** Læringsprosjekt under utvikling.

## Innholdsfortegnelse

- [Om prosjektet](#om-prosjektet)
- [Funksjoner](#funksjoner)
- [Installasjon og oppsett](#installasjon-og-oppsett)
- [Sikkerhet og personvern](#sikkerhet-og-personvern)
- [Lisens](#lisens)

## Om prosjektet

Decision Lab er en chat i terminalen som selv velger hvilken språkmodell som skal svare på hver melding.

Ikke alle spørsmål trenger den kraftigste modellen. Et enkelt "hei" kan besvares raskt og billig, mens en kompleks analyse fortjener en grundigere modell. Decision Lab lar en egen beslutningsmodell vurdere kompleksiteten i hver prompt og sender den videre til modellen som passer best.

## Funksjoner

- **Automatisk modellvalg per melding:** Hver prompt vurderes på nytt, så modellen kan byttes underveis i samtalen.
- **To nivåer:**
  - **Fast** (`gpt-5.4-mini`) for enkle spørsmål og raske svar.
  - **Thorough** (`gpt-6-luna`) for spørsmål som krever grundig analyse.
- **Viser hvilken modell som er valgt**, og hvor sikker beslutningsmodellen var på valget (confidence).
- **Samtalehistorikk:** Modellen husker tidligere meldinger i samtalen, også når den bytter mellom Fast og Thorough. Dette gjøres med `previous_response_id`, så historikken holdes hos OpenAI og ikke i et lokalt array.
- **Strømming av svar:** Svaret skrives ut fortløpende mens det genereres, i stedet for at du venter på hele svaret.
- **Feilhåndtering:** Feil fra API-et, både før og under strømmingen, skrives ut uten at programmet krasjer.
- **Kontinuerlig samtale** i terminalen til du avslutter med `q`.

> **Merk:** Beslutningsmodellen ser bare meldingen du nettopp skrev, ikke resten av samtalen. Modellvalget baseres derfor kun på den siste prompten.

## Installasjon og oppsett

### Krav

- Python 3.13
- En OpenAI API-nøkkel med tilgang til modellene over

### 1. Klon prosjektet

```bash
git clone https://github.com/SondreHaugom/Decision-lab.git
cd Decision-lab
```

### 2. Lag et virtuelt miljø og installer avhengigheter

Med [uv](https://docs.astral.sh/uv/):

```bash
uv venv decision
source decision/bin/activate
uv pip install openai python-dotenv
```

Eller med vanlig `venv` og `pip`:

```bash
python3 -m venv decision
source decision/bin/activate
pip install openai python-dotenv
```

### 3. Legg inn API-nøkkelen

Lag en fil som heter `.env` i rotmappen til prosjektet:

```env
OPENAI_API_KEY=din-api-nøkkel-her
```

### 4. Start programmet

```bash
python openai_chat.py
```

Skriv meldingen din etter `You:`. Skriv `q` for å avslutte.

```text
You: Hei!
Model that is used: gpt-5.4-mini (confidence: ...)
---------------------------------------------------------------------
(svaret strømmes fra modellen)
You: q
Goodbye!
```

## Sikkerhet og personvern

### API-nøkkel

- API-nøkkelen leses fra `.env` og ligger aldri i koden.
- `.env` står i `.gitignore`, så den blir ikke lastet opp til GitHub. Sjekk at det fortsatt er slik før du committer.
- Ikke del nøkkelen med andre. Hvis den lekker, må du slette den i OpenAI-kontoen og lage en ny.

### Hva som sendes ut

- **Alt du skriver sendes til OpenAI**, og hver melding sendes **to ganger**: én gang til beslutningsmodellen og én gang til modellen som svarer.
- For at modellen skal huske samtalen, **lagres svarene hos OpenAI** og hentes med `previous_response_id`. Hvor lenge de lagres, styres av OpenAIs vilkår og innstillingene på API-kontoen din.
- **Ikke skriv inn personopplysninger, sensitive opplysninger eller taushetsbelagt informasjon** i chatten.

### Hva som lagres lokalt

- Programmet lagrer ingen samtalehistorikk på maskinen din. Når du avslutter, glemmes `response_id`, og neste kjøring starter en ny samtale.

## Lisens

Prosjektet er lisensiert under [MIT-lisensen](LICENSE).
