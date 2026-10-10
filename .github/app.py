import streamlit as st

st.title("🧠 KI-Lernspiel: Essen oder Trinken?")

# 1. Speicher für die Wortlisten
if "ess" not in st.session_state:
    st.session_state.ess = [# --- Grundnahrungsmittel & Beilagen (15) ---
    "apfel",
    "brot",
    "pizza",
    "reis",
    "nudeln",
    "spaghetti",
    "kartoffel",
    "pommes",
    "semmel",
    "brezel",
    "haferflocken",
    "müsli",
    "toast",
    "croissant",
    "püree",
    # --- Obst & Früchte (15) ---
    "banane",
    "birne",
    "orange",
    "erdbeere",
    "himbeere",
    "kirsche",
    "traube",
    "zitrone",
    "wassermelone",
    "ananas",
    "pfirsich",
    "pflaume",
    "kiwi",
    "mango",
    "avocado",
    # --- Gemüse & Salate (15) ---
    "tomate",
    "gurke",
    "karotte",
    "möhre",
    "salat",
    "paprika",
    "zwiebel",
    "knoblauch",
    "brokkoli",
    "blumenkohl",
    "spinat",
    "pilz",
    "bohne",
    "erbse",
    "mais",
    # --- Fast Food & Snacks (15) ---
    "burger",
    "döner",
    "sandwich",
    "wrap",
    "hotdog",
    "chips",
    "popcorn",
    "nüsse",
    "nachos",
    "chicken nugget",
    "taco",
    "flammkuchen",
    "falafel",
    "pretzel",
    "currywurst",
    # --- Fleisch, Fisch & Proteine (15) ---
    "fleisch",
    "hähnchen",
    "steak",
    "schnitzel",
    "wurst",
    "salami",
    "fisch",
    "lachs",
    "thunfisch",
    "tofu",
    "ei",
    "käse",
    "garnelen",
    "speck",
    "geflügel",
    # --- Fertiggerichte & Suppen (10) ---
    "suppe",
    "eintopf",
    "curry",
    "auflauf",
    "gulasch",
    "risotto",
    "sushi",
    "lasagne",
    "manti",
    "ramen",
    # --- Süßspeisen & Desserts (15) ---
    "kuchen",
    "torte",
    "schokolade",
    "eis",
    "keks",
    "donut",
    "muffin",
    "pudding",
    "waffel",
    "pancake",
    "pfannkuchen",
    "gummibärchen",
    "brownie",
    "bonbon",
    "müsli riegel",
]
Einbindung in deinen Streamlit-Code:
Ersetze in deinem Streamlit-Code einfach die Zeile zur Initialisierung:

Python
if "ess" not in st.session_state:
    st.session_state.ess = [
        "apfel",
        "brot",
        "pizza",
        "reis",
        "nudeln",
        "spaghetti",
        "kartoffel",
        "pommes",
        "semmel",
        "brezel",
        "haferflocken",
        "müsli",
        "toast",
        "croissant",
        "püree",
        "banane",
        "birne",
        "orange",
        "erdbeere",
        "himbeere",
        "kirsche",
        "traube",
        "zitrone",
        "wassermelone",
        "ananas",
        "pfirsich",
        "pflaume",
        "kiwi",
        "mango",
        "avocado",
        "tomate",
        "gurke",
        "karotte",
        "möhre",
        "salat",
        "paprika",
        "zwiebel",
        "knoblauch",
        "brokkoli",
        "blumenkohl",
        "spinat",
        "pilz",
        "bohne",
        "erbse",
        "mais",
        "burger",
        "döner",
        "sandwich",
        "wrap",
        "hotdog",
        "chips",
        "popcorn",
        "nüsse",
        "nachos",
        "chicken nugget",
        "taco",
        "flammkuchen",
        "falafel",
        "currywurst",
        "fleisch",
        "hähnchen",
        "steak",
        "schnitzel",
        "wurst",
        "salami",
        "fisch",
        "lachs",
        "thunfisch",
        "tofu",
        "ei",
        "käse",
        "garnelen",
        "speck",
        "geflügel",
        "suppe",
        "eintopf",
        "curry",
        "auflauf",
        "gulasch",
        "risotto",
        "sushi",
        "lasagne",
        "manti",
        "ramen",
        "kuchen",
        "torte",
        "schokolade",
        "eis",
        "keks",
        "donut",
        "muffin",
        "pudding",
        "waffel",
        "pancake",
        "pfannkuchen",
        "gummibärchen",
        "brownie",
        "bonbon"
        ]

if "tri" not in st.session_state:
    st.session_state.tri = ["wasser", "saft", "tee"]

# 2. Satz eingeben
was = st.text_input("Schreib einen Satz mit Essen oder Trinken drin:").lower()

if was:
    punkteEss = sum(1 for wort in st.session_state.ess if wort in was)
    punkteTri = sum(1 for wort in st.session_state.tri if wort in was)

    st.subheader("Auswertung")
    if punkteEss > punkteTri:
        st.success("essen! 🍎")
    elif punkteTri > punkteEss:
        st.success("trinken! 🥤")
    else:
        st.info("weiß nicht 🤔")

    st.divider()

    # 3. KI Lernen
    st.subheader("Bring der KI etwas bei 🧠")
    kategorie = st.radio(
        "Kategorie:", ["Nichts / Passt so", "Essen 🍎", "Trinken 🥤"]
    )
    neu = st.text_input("Welches Wort aus deinem Satz war das?").lower()

    if st.button("Wort speichern"):
        if neu and kategorie == "Essen 🍎":
            st.session_state.ess.append(neu)
            st.success(f"Gelernt! '{neu}' ist jetzt Essen 🍎")
        elif neu and kategorie == "Trinken 🥤":
            st.session_state.tri.append(neu)
            st.success(f"Gelernt! '{neu}' ist jetzt Trinken 🥤")

# Seitenleiste mit aktuellem Wissen
with st.sidebar:
    st.header("Aktuelles Wissen der KI")
    st.write("**Essen:**", ", ".join(st.session_state.ess))
    st.write("**Trinken:**", ", ".join(st.session_state.tri))