# -*- coding: utf-8 -*-
"""
RandomDaten-Generator v1.0
Generiert eindeutige deutsche/österreichische Identitätsdaten:
Namen, Passwörter, Geburtsdaten, Benutzernamen.
"""
import random
import tkinter as tk
from datetime import date, timedelta
from tkinter import font, messagebox

# ---------------------------------------------------------------------------
# DATENBANKEN
# ---------------------------------------------------------------------------

VORNAMEN_M = [
    "Martin","Stefan","Michael","Andreas","Thomas","Christian","Markus","Peter","Klaus","Johann",
    "Franz","Josef","Wolfgang","Hans","Georg","Karl","Lukas","Maximilian","Sebastian","David",
    "Daniel","Florian","Alexander","Julian","Tobias","Benjamin","Felix","Jonas","Leon","Elias",
    "Paul","Noah","Finn","Luis","Luca","Henry","Emil","Oskar","Anton","Moritz",
    "Jakob","Simon","Niklas","Tim","Jan","Philipp","Patrick","Dominik","Marcel","Rene",
    "Oliver","Sven","Marc","Kevin","Dennis","Mario","Robert","Ralf","Jürgen","Heinz",
    "Gerhard","Werner","Helmut","Alfred","Ernst","Herbert","Friedrich","Otto","Rudolf","Walter",
    "Hubert","Alois","Leopold","Bernhard","Bruno","Emil","Ignaz","Konrad","Matthias","Norbert",
    "Reinhard","Roland","Siegfried","Theodor","Ulrich","Vinzenz","Waldemar","Xaver","Yannick","Zacharias",
    "Bastian","Clemens","Fabian","Gustav","Hermann","Ivan","Jerome","Kilian","Lorenz","Manuel",
    "Nils","Otto","Pascal","Quirin","Raphael","Samuel","Theo","Udo","Valentin","Wilhelm",
    "Konstantin","Karsten","Maik","Torsten","Dirk","Gunnar","Holger","Ingo","Jens","Kay",
    "Armin","Benedikt","Christoph","Detlef","Egbert","Falk","Gerald","Harald","Ivo","Joachim",
    "Knut","Lothar","Meinhard","Niko","Olaf","Prinz","Quentin","Rainer","Steffen","Till",
    "Ulf","Viktor","Willy","Yves","Aaron","Ben","Carl","Dorian","Eduard","Frederik",
]

VORNAMEN_W = [
    "Maria","Anna","Julia","Sophie","Laura","Hannah","Lisa","Sarah","Lena","Emma",
    "Mia","Emilia","Marie","Lina","Klara","Charlotte","Frieda","Greta","Mathilda","Paula",
    "Johanna","Elisabeth","Katharina","Magdalena","Theresa","Verena","Sabrina","Nicole","Sandra","Petra",
    "Claudia","Barbara","Ursula","Brigitte","Monika","Angelika","Christina","Melanie","Stefanie","Andrea",
    "Martina","Silvia","Renate","Ingrid","Heidi","Gerda","Elfriede","Erika","Herta","Irmgard",
    "Hilde","Margarete","Rosa","Karolina","Valentina","Isabella","Victoria","Alexandra","Natalie","Tamara",
    "Jessica","Michelle","Denise","Vanessa","Jennifer","Nina","Carina","Sabine","Katrin","Birgit",
    "Diana","Esther","Franziska","Gabriele","Helena","Ines","Jasmin","Kirsten","Larissa","Mirjam",
    "Nadine","Olivia","Patricia","Ramona","Simone","Tanja","Ulrike","Viktoria","Waltraud","Xenia",
    "Yvonne","Zoe","Amelie","Beatrix","Celine","Dorothea","Eleonore","Fenja","Gisela","Henriette",
    "Ida","Josephine","Kornelia","Luise","Maren","Nora","Ottilie","Philine","Querida","Rebecca",
    "Sophia","Traudl","Ulrike","Veronika","Wilhelmine","Yasmin","Annika","Bettina","Cornelia","Delia",
    "Elena","Fee","Gloria","Hermine","Irene","Jana","Karla","Lilli","Marlene","Nele",
    "Oda","Pauline","Romy","Svea","Tilda","Ursula","Viola","Wilma","Yara","Zita",
    "Änne","Bärbel","Christa","Dagmar","Evelyn","Friederike","Gundula","Hannelore","Isabell","Judith",
]

NACHNAMEN = [
    "Müller","Schmidt","Schneider","Fischer","Weber","Meyer","Wagner","Becker","Hoffmann","Schulz",
    "Koch","Bauer","Richter","Klein","Wolf","Neumann","Schwarz","Zimmermann","Braun","Krüger",
    "Hofmann","Hartmann","Lange","Werner","Schmitt","Schmitz","Krause","Meier","Lehmann","Schmid",
    "Kohler","Maier","Herrmann","König","Walter","Mayer","Huber","Kaiser","Fuchs","Peters",
    "Lang","Scholz","Möller","Weiß","Jung","Hahn","Schubert","Vogel","Friedrich","Keller",
    "Günther","Frank","Berger","Winkler","Roth","Beck","Lorenz","Baumann","Franke","Albrecht",
    "Schuster","Simon","Ludwig","Böhm","Winter","Kraus","Martin","Schumacher","Krämer","Vogt",
    "Stein","Jäger","Otto","Sommer","Groß","Seidel","Heinrich","Brandt","Haas","Schreiber",
    "Graf","Schulte","Dietrich","Kühn","Ziegler","Engel","Pohl","Horn","Busch","Bergmann",
    "Thomas","Voigt","Sauer","Arnold","Wolff","Beyer","Seifert","Lindner","Hansen","Marx",
    "Meier","Fritz","Bartels","Wenzel","Nowak","Weiss","Mendler","Leitner","Eder","Gruber",
    "Hofer","Wimmer","Steiner","Mayr","Wieser","Egger","Haider","Fink","Burger","Moser",
    "Auer","Schmidbauer","Reiter","Schwaiger","Winklmair","Stadler","Aigner","Mauser","Grabner","Koller",
    "Löffler","Fritsch","Binder","Riegler","Unger","Schachner","Wagner","Perner","Pichler","Lackner",
    "Nagel","Hirsch","Hartl","Schmied","Berndt","Ritter","Kettner","Pfeiffer","Kirchner","Voit",
    "Mair","Baumgartner","Dörfler","Felder","Gassner","Holzer","Kaindl","Lendl","Matt","Neubauer",
    "Österreicher","Palm","Quandt","Raab","Sailer","Thaler","Ullmann","Vetter","Weigl","Zanger",
    "Althammer","Brandstätter","Czerny","Donhauser","Ebner","Forstner","Grillmayr","Hohensinn","Jandl","Kastner",
    "Lenz","Mandl","Nader","Pammer","Reisinger","Strasser","Traxler","Urban","Wachter","Zehetner",
    "Abendroth","Bachmair","Czernik","Degenhardt","Eichhorn","Falkner","Goldmann","Hammerschmidt","Imhof","Jauch",
    "Kettler","Limbach","Metzger","Nitschke","Obermeier","Probst","Quellmalz","Rumpf","Scherer","Tannhauser",
]

ADJ = [
    "Fröhlich","Vertraulich","Glücklich","Gutgelaunt","Wohlfühl","Behaglich","Herzlich","Lieb","Nett",
    "Freundlich","Entspannt","Locker","Lustig","Heiter","Munter","Sonnig","Zufrieden","Launisch","Ausgelassen",
    "Humorvoll","Witzig","Verspielt","Lebendig","Lebhaft","Aufgeweckt","Munter","Frohsinnig","Optimistisch","Euphorisch",
    "Lebensfroh","Silvester","Strahlend","Bekümmert","Fidel","Feierlich","Unbeschwert","Traumhaft","Zart","Sanft",
    "Wärmend","Inspirierend","Märchenhaft","Zauberhaft","Betörend","Köstlich","Kuschelig","Zuckersüß","Goldig","Tollkühn",
]

SUBST = [
    "Verkäufer","Rose","Himmel","Fröhlichkeit","Mond","Sonne","Stern","Wolke","Regenbogen","Blume",
    "Vogel","Schmetterling","Eichhörnchen","Zauberer","Elfe","Fee","Einhorn","Drache","Schiff","Kompass",
    "Anker","Leuchtturm","Laterne","Kerze","Teekessel","Brezel","Zimtstern","Marzipan","Keks","Bonbon",
    "Glücksbringer","Vierklee","Talisman","Herz","Seele","Melodie","Tanz","Wirbel","Sommerwind","Frühlingsduft",
    "Pusteblume","Libelle","Kolibri","Pfau","Flamingo","Delfin","Robbe","Igel","Reh","Luchs",
]

SPEZIAL = list("!@#$%&*?+-=~")

LEET = {
    "a": ["@", "4"], "ä": ["@"], "e": ["3", "€"], "i": ["!", "1"], "o": ["0"],
    "u": ["µ", "(_)"], "s": ["$", "5"], "t": ["7"], "l": ["1"], "g": ["9"],
    "b": ["8"], "z": ["2"], "c": ["(", "<"], "h": ["#"], "r": ["|2"], "n": ["|V"],
}
VOKALE = "aeiouäöü"

# ---------------------------------------------------------------------------
# GENERATOREN
# ---------------------------------------------------------------------------
class Generatoren:
    def __init__(self):
        self._used = {k: set() for k in ("name", "passwort", "geburtstag", "benutzername")}

    def _unique(self, key, fn, tries=10_000):
        for _ in range(tries):
            v = fn()
            if v not in self._used[key]:
                self._used[key].add(v)
                return v
        raise RuntimeError(f"Kombinationsraum für '{key}' erschöpft.")

    def name(self, geschlecht=None):
        g = geschlecht or random.choice(["m", "w"])
        pool = VORNAMEN_M if g == "m" else VORNAMEN_W
        return self._unique("name", lambda: f"{random.choice(pool)} {random.choice(NACHNAMEN)}")

    def passwort(self):
        """Passwort im Stil: M@rt!nSHcm!Dt + Zufallsvarianten."""
        def gen():
            first, last = self.name().split(" ", 1)
            f = list(first)
            l = list(last)
            # Vokale leetspeaken (zufällige Teilmenge)
            for arr in (f, l):
                for i, ch in enumerate(arr):
                    low = ch.lower()
                    if low in LEET and random.random() < 0.6:
                        arr[i] = random.choice(LEET[low]) if random.random() < 0.75 else ch.upper()
                    elif random.random() < 0.25:
                        arr[i] = ch.upper()
            # gelegentlich benachbarte Buchstaben tauschen
            for arr in (f, l):
                if len(arr) > 3 and random.random() < 0.5:
                    i = random.randrange(1, len(arr) - 1)
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            pw = "".join(f) + "".join(l)
            # Zusatz: Zahl + Sonderzeichen an zufälliger Stelle
            if random.random() < 0.7:
                pos = random.randrange(1, len(pw))
                pw = pw[:pos] + str(random.randint(1, 99)) + pw[pos:]
            if random.random() < 0.5:
                pos = random.randrange(1, len(pw))
                pw = pw[:pos] + random.choice(SPEZIAL) + pw[pos:]
            return pw
        return self._unique("passwort", gen)

    def geburtstag(self):
        start, end = date(1980, 1, 1), date(2000, 1, 1)
        def gen():
            d = start + timedelta(days=random.randint(0, (end - start).days))
            return d.strftime("%d.%m.%Y")
        return self._unique("geburtstag", gen)

    def benutzername(self):
        def gen():
            parts = [random.choice(ADJ)]
            if random.random() < 0.5:
                parts.append(random.choice(ADJ))
            parts.append(random.choice(SUBST))
            name = "".join(parts)
            roll = random.random()
            if roll < 0.3:
                name += str(random.randint(1, 999))
            elif roll < 0.5:
                name += random.choice(SPEZIAL) + str(random.randint(1, 99))
            return name
        return self._unique("benutzername", gen)

GEN = Generatoren()

# ---------------------------------------------------------------------------
# GUI
# ---------------------------------------------------------------------------
BG = "#14141f"; CARD = "#1e1e2e"; FG = "#e6e6f0"; ACCENT = "#7c5cff"
ACCENT2 = "#00d4b8"; FONT = "Segoe UI"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RandomDaten-Generator")
        self.geometry("460x560")
        self.configure(bg=BG)
        self.resizable(False, False)

        tk.Label(self, text="⚡ RandomDaten", bg=BG, fg=FG,
                 font=(FONT, 20, "bold")).pack(pady=(18, 2))
        tk.Label(self, text="Eindeutige Testdaten generieren", bg=BG, fg="#8888a0",
                 font=(FONT, 10)).pack()

        self.fields = {}
        rows = [
            ("👤 Name (m)", lambda: GEN.name("m")),
            ("👤 Name (w)", lambda: GEN.name("w")),
            ("🔑 Passwort", GEN.passwort),
            ("🎂 Geburtsdatum", GEN.geburtstag),
            ("🏷 Benutzername", GEN.benutzername),
        ]
        for label, fn in rows:
            card = tk.Frame(self, bg=CARD, highlightbackground="#2a2a40",
                            highlightthickness=1, bd=0)
            card.pack(fill="x", padx=24, pady=6)
            tk.Label(card, text=label, bg=CARD, fg=ACCENT2,
                     font=(FONT, 9, "bold"), width=14, anchor="w"
                     ).pack(side="left", padx=(12, 4), pady=10)
            val = tk.Entry(card, bg=CARD, fg=FG, relief="flat",
                           font=(FONT, 11, "bold"), width=26)
            val.pack(side="left", padx=4)
            tk.Button(card, text="📋", bg=CARD, fg="#8888a0", relief="flat",
                      activebackground=CARD, activeforeground=FG,
                      command=lambda v=val: self.copy(v)).pack(side="right", padx=8)
            self.fields[label] = (val, fn)

        tk.Button(self, text="🎲 ALLES GENERIEREN", bg=ACCENT, fg="white",
                  relief="flat", font=(FONT, 11, "bold"), cursor="hand2",
                  activebackground="#937cff", activeforeground="white",
                  command=self.generate_all).pack(fill="x", padx=24, pady=(14, 4))
        tk.Button(self, text="📄 Alle kopieren", bg=CARD, fg=ACCENT2, relief="flat",
                  font=(FONT, 9), cursor="hand2", activebackground="#26263a",
                  command=self.copy_all).pack(pady=(0, 10))
        self.status = tk.Label(self, text="Bereit", bg=BG, fg="#55556a",
                               font=(FONT, 8))
        self.status.pack()
        self.generate_all()

    def generate_all(self):
        try:
            for val, fn in self.fields.values():
                val.delete(0, "end")
                val.insert(0, fn())
            total = sum(len(GEN._used[k]) for k in GEN._used)
            self.status.config(text=f"Generiert – {total} einzigartige Werte bisher")
        except RuntimeError as e:
            messagebox.showwarning("Hinweis", str(e))

    def copy(self, entry):
        self.clipboard_clear()
        self.clipboard_append(entry.get())
        self.status.config(text="In Zwischenablage kopiert ✔")

    def copy_all(self):
        text = "\n".join(f"{k}: {v[0].get()}" for k, v in self.fields.items())
        self.clipboard_clear()
        self.clipboard_append(text)
        self.status.config(text="Alle Werte kopiert ✔")

if __name__ == "__main__":
    App().mainloop()
