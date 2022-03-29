# Exploratory_Air_Route_Analysis

Heutzutage geht die Informations-Technologie über das einfache Speichern und Anzeigen von Daten hinaus.
Die Teildisziplin Data Science, Daten zu akquirieren, auszuwerten und daraus Wissen zu generieren, gewinnt immer mehr an Bedeutung.
Vor allem um im wirtschaftlichen Umfeld die Unternehmenssteuerung zu optimieren,
die Entscheidungsfindung zu unterstützen oder im Kontext von Marketing sogar markante Sachlagen ausfindig zu machen und zu präsentieren. 
Dabei ist es nicht nur wichtig, zu welchen Aussagen die Daten führen, sondern auch, wie diese visualisiert werden. Entscheidend ist dabei, 
die akquirierten Daten für verschiedene Interessensgruppen individuell adäquat aufzubereiten. 
Im Folgenden geht es um drei Visualisierungsbeispiele aus der Logistikbranche. 
Hierzu werden Flugdaten auf verschiedene Weisen ausgewertet und aufbereitet.

Herangehensweise

Der erste Schritt ist es, die Rahmenbedingungen für alle folgenden Visualisierungen festzulegen. 
Die visuellen Auswertungen der Flugdaten können verschiedene Interessensgruppen adressieren, 
beispielweise die Interessenten oder Kunden der Airline, 
die sich für die angebotenen Flüge und insbesondere deren Verspätung und Zuverlässigkeit interessieren. 
Auf der anderen Seite sind auch den Airlines oder Flughäfen selbst ein Vergleich mit ihrer Konkurrenz wichtig. 
Zudem kann die Airline über eine Darstellung ihrer Flugdaten auf eigene Schwächen und Verbesserungen schließen. 
Im Folgenden werden die genannten Interessensvertreter adressiert. 
Bei den Darstellungen muss auf gewissere Grundcharakteristiken geachtet werden, 
wie sie beispielweise bei Dieter Rams Design Regeln aufgeführt sind (Rams, 2021). 
Davon sind für die folgenden Visualisierungen besonders die Verständlichkeit, die Ästhetik und die Innovation der Darstellung, 
sowie die Ehrlichkeit der Daten wichtig. 
Eine weitere Bedingung für die Visualisierungen ist das Medium, 
über das sie präsentiert werden. Bei den folgenden Visualisierungen handelt es sich um Web-Plots,
die man zum Beispiel auf einer Website finden könnte. 
Es besteht also nicht die Möglichkeit dem Publikum zu der Darstellung eine mündliche Erklärung zu liefern oder direkte Rückfragen zu ermöglichen.
Daher muss insbesondere darauf geachtet werden, alle benötigten Informationen mitzuliefern, damit der Betrachter eigene Schlüsse ziehen kann. 
Ein Vorteil der digitalen Darstellung ist die Möglichkeit, Animationen oder Interaktionsmöglichkeiten einzubauen,
mit denen der Betrachter selbst durch die Darstellung navigieren und somit seinen eigenen Fokus setzen kann.
Damit bekommt der Betrachter ein sogenanntes Exploratory-Erlebnis, bei dem er mit der Visualisierung interagieren kann. 
Da es sich bei den Daten ausschließlich um Flugdaten aus den USA handelt,
sind die Plots in internationaler Sprache beschriftet, da die meisten der Adressierten entweder aus den USA stammen
oder an Internationalen Reisen interessiert sind. 

Datenauswahl & visuelle Ansätze

Ein Großteil der Daten ist bereits durch die Aufgabenstellung vorgegeben.
Bei einigen Visualisierungen können aber noch externe Daten mit einbezogen werden, um die Dimensionen der Darstellungen zu erweitern.
Im Folgenden wird für jede Visualisierung beschrieben, um welchen Ausschnitt der Daten es sich handelt und warum dieser ausgewählt wurde.
Um einen ersten Eindruck der Daten zu bekommen, wurden zu Beginn mit den Python Libraries Pandas und Numpy die Durchschnitte, Minima, Maxima,
sowie der Meridian einiger Werte gewonnen (siehe firstview_inspect .py). Hieraus entstehen dann drei Aspekte, die im Folgenden näher betrachtet werden.
Im Folgenden ist die Dokumentation über die Umsetzung in Kommentaren in den angegebenen Python-Datei angefügt.
