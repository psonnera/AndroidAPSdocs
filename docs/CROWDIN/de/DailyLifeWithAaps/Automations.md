# Automatisierung

## Was ist eine Automatisierung?

"**Automation**" is a feature which can automate task for AAPS.

Automations performs specific actions based on one or more conditions or triggers. Triggers can include irregular events like low or high blood glucose (BG) levels, or a set amount of negative insulin on board (IOB). Automations can also handle recurring events, such as meals or exercise at certain times of day, or when the user is within a specific distance of a GPS location or a WIFI SSID area. Automation can execute AAPS settings backups based on a schedule or on every Pod change.

Automations rules are created and modified from the Automations tab. Each rule is defined by two properties:

- One or more conditions or 'triggers' that start an action.

    Think of a certain time schedule, an event or properties value in AAPS

- One or more actions to perform.

    Such as an alarm or settings a profile percentage or exporting the AAPS settings on Pod change.


Es gibt eine Vielzahl von Automatisierungsmöglichkeiten und Du solltest Dich mit ihnen in der AAPS-App im Abschnitt „Automatisierung“ vertraut machen. You can also search the AAPS user groups on ![**Facebook**](https://www.facebook.com/groups/AndroidAPSUsers) and ![**Discord**](https://discord.gg/4fQUWHZ4Mw) for Automation examples from other users.

## Wie Automatisierung helfen kann

1. **Automate reoccurring tasks:** Automatically executing programmed actions without user interaction.

1. **Entscheidungsmüdigkeit verringern:** Der Hauptvorteil von **Automatisierungen** ist, den Nutzenden von der Last manueller **AAPS**-Eingriffe zu befreien. Die [Forschung](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6286423/#ref4) schätzt, dass Menschen mit Diabetes Typ 1 täglich durchschnittlich 180 zusätzliche Entscheidungen treffen müssen. **Automatisierungen** können diese mentale Belastung verringern und so Freiräume für andere Dinge des Lebens schaffen können.

1. **Potentiell verbesserte glykämische Kontrolle:** **Automatisierungen** können zum Beispiel dabei helfen, dass auch bei vollen Terminkalendern oder Vergesslichkeitsphasen, **temporäre Ziele** trotzdem gesetzt werden, wo es notwendig ist. Ein Kind mit Diabetes hat z.B. dienstags um 10.00 Uhr und donnerstags um 14.00 Uhr Sport, der ein hohes Temp Target („TT“) von 30 Minuten vor der sportlichen Aktivität aktiv notwendig macht. Dieses **Temp Target** kann über eine **Automatisierung** aktiviert werden.

1. **Ermöglicht es AAPS sehr individuell** in speziellen Situation, im Rahmen der eigenen Einstellungen, mehr oder weniger aggressiv zu arbeiten. Wenn sich beispielsweise eine längere Phase mit negativem **IOB** mitten in der Nacht, als Zeichen für ein zu starkes **Profil**, abzeichnet, kann automatisiert ein temporäres schwächeres **Profil** (in %) gesetzt werden.

Im Beispiel unten wird gezeigt, wie mit einer **Automatisierung** einzelne manuelle Schritte überflüssig gemacht werden.

Du machst jeden Morgen um 6 Uhr Sport: Du musst um 5 Uhr daran denken, in AAPS manuell ein temporäres Ziel „Aktivität“ zu setzen, bevor Du mit dem Sport beginnst.

![Alt text](../images/automation_2024-02-12_20-54-50.png)

Du hast eine **Automatisierung** erstellt, die um 5.00 Uhr am Morgen ein „temporäres Ziel für Aktivität“ setzt, um mit optimalem **Glukosewert** und **IOB** in das um 6.00 Uhr beginnende Training gehen zu können:

![Alt text](../images/automation_2024-02-12_20-54-49.png)

## Wichtige Vorüberlegungen, bevor mit Automatisierung gestartet wird

1. Before setting up certain Automations, you should have reasonable **BG** control with **AAPS**. Automatisierungen sollten nicht dazu verwendet werden schiefe/schlechte Einstellungen (Basalraten, Korrekturfaktoren (**ISF**) oder Mahlzeitenfaktoren (**CR**)) auszugleichen (wird in Tiefe weiter unten beschrieben). Vermeide automatisierte **Profilwechsel**, um einen **Glukosewert**-Anstieg durch _z.B._ Mahlzeiten abzufangen. Diese Anstiege sind durch bestehende AAPS-Funktionen (SMBs etc.) besser abgedeckt.

1. So wie bei jeder Technik: **CGMs**, **Pumpen** und Smartphones können versagen: Technische Probleme oder Sensorfehler können eine laufende **Automatisierung** stören und müssen eventuell durch manuelles Eingreifen behoben werden.

1. Der **Automatisierungsbedarf** wird sich mit ändernden Tagesabläufen über die Zeit verändern**. Wenn zwischen Arbeits-, Schul- und Urlaubsphasen gewechselt wird, macht eine Kalendererinnerung zur Überprüfung der laufenden **Automatisierungen** Sinn (Automatisierungen lassen sich leicht aktivieren und de-aktiveren). Ein Beispiel ist: Du machst Urlaub und deswegen können/sollten Automatisierungen für Schulsport oder Dein tägliches Training ausgesetzt oder deren Timing angepasst werden.

1. **Automatisierungen** können miteinander in Konflikt stehen. Daher sollten neue **Automatisierungen** in einer gesicherten Umgebung sehr genau geprüft werden. Wichtig ist zu verstehen, warum eine bestimmte **Automatisierung** ggf. nicht, wie Du es erwartet hast, ausgelöst wurde.

1. Wenn Du die Autosens-Funktionalität nutzt, versuche, anstelle von **Profilwechseln** **temporäre Ziele** zu nutzen. **Temporäre Ziele** setzen Autosens nicht auf 0 zurück. **Profilwechsel** setzen Autosens zurück (reset).

1. Die meisten **Automatisierungen** sollten nur für einen **beschränkten Zeitraum** laufen. Danach kann **AAPS** die Situation erneut bewerten und die **Automatisierung** erneut starten, sofern das notwendig ist und die Startbedingungen weiterhin erreicht sind. Zum Beispiel: „Setze ein temporäres Ziel mit 120 mg/dl für 30 Minuten“ oder „Setze ein **Profil** mit 110% für 10 Minuten“ _und_ „Setze ein temporäres Ziel mit 90 mg/dl für 10 Minuten“. **Automatisierungen** zu nutzen, um dauerhafte Änderungen (z.B. das Profil prozentual anzuheben), kann Hypoglykämien zur Folge haben.

## Wann kann ich mit Automatisierungen beginnen?

**Automatisierungen** können im **Ziel 10** gestartet werden.

## Wo finden sich die Automatisierungen in AAPS?

Depending on your [Config builder > General](../SettingUpAaps/ConfigBuilder.md) settings, **Automation** is located either in the ‘hamburger’ menu or as a tab with **AAPS**.

## Wie kann ich eine Automatisierung einrichten?

Um eine **Automatisierung** einzurichten, erstelle in **AAPS** eine 'Regel/Aufgabe'. Das kann so aussehen:

![Automation create](../images/automation_create.png)

* Vergebe einen Namen für die Aufgabe (Regel);
* Wähle mindestens eine „Bedingung“ oder einen „Auslöser“ aus; und

![Automation condition](../images/automation_condition.png)

* Wähle eine „Aktion“;

![Automation action](../images/automation_action.png)

* markiere das rechte obere Kästchen im **Automatisierungs-Ereignis**, um die **Automatisierung** zu aktivieren:

![Automatisierung](../images/automation_2024-10-26_17-48-05.png)



Um eine **Automatisierungsregel** zu deaktivieren, deaktiviere das Kästchen links neben dem Namen der **Automatisierung**. Das folgende Beispiel zeigt eine **Automatisierung** mit dem Titel „Low Glucose TT“ als aktiviert („angehakt“) oder deaktiviert („ausgehakt“).

![Alt text](../images/automation_2024-02-12_20-56-08.png)


Beim Einrichten einer **Automatisierung** kannst Du sie zuerst dadurch testen, dass Du unter „Aktion“ die Option „Benachrichtigung“ aktivierst. **AAPS** löst damit zunächst nur eine Benachrichtigung aus und nicht eine tatsächliche automatisierte Aktion. Wenn Du dann sicher bist, dass die Benachrichtigung zur richtigen Zeit bzw. Bedingung ausgelöst worden ist, kannst Du die **Automatisierungsregel** anpassen und die 'Benachrichtigung' durch die tatsächlich gewünschte 'Aktion' ersetzen.

![Alt text](../images/automation_2024-02-12_20-55-05.png)

```{admonition} Important note
:class: note

**Automatisierungen** sind auch dann aktiv, wenn der Loop deaktiviert ist!
```


## Sicherheitsbeschränkungen

Es gibt Sicherheitsbeschränkungen für **Automatisierungen**:

* Der **Glukosewert** muss zwischen 72 und 270 mg/dl (bzw. zwischen 4 und 15 mmol/l) liegen.
* Der **Prozentsatz des Profils** muss zwischen 70% und 130% liegen.
* Es müssen 5 Minuten zwischen der Ausführung der einzelnen **Automatisierungen** (und der erstmaligen Ausführung) liegen.

## Negative Werte richtig nutzen

```{admonition} Warning
:class: warning

Vorsicht bei der Auswahl eines negativen Wertes in der **Automatisierung**
```

Besonderer Vorsicht bedarf es, wenn in einer **Automatisierung** ein 'negativer Wert' innerhalb einer "kleiner als"-Bedingung genutzt werden soll. Zum Beispiel:

![Alt text](../images/automation_2024-02-12_20-56-25.png-500x.png)

**Beispiel 1:** Erstelle eine Bedingung **„ist kleiner als"** „-0.1 mmol/l“ (bzw. „-2 mg/dl“) wird:

eine **Automatisierung** für jeden Wert, der **kleiner als** -0,1 (bzw. -2) ist, auslösen. Das sind dann die Zahlen wie -0,2, -0,3, -0,4 (bzw. -4, -6, -8) usw. Der Wert -0,1 (bzw. -2) selber **ist in der Bedingung nicht enthalten**. (Die Bedingung „ist kleiner oder gleich -0,1 mmol/l (-2 mg/dl)“ _würde_ den Wert -0,1 mmol/l oder -2 mg/dl mit einschließen).

**Beispiel 2:** Erstelle eine Bedingung „ist größer als" -0,1 mmol/l (-2 mg/dl) wird:

Eine **Automatisierung** für jeden Wert, der **größer als** -0.1 mmol/l (-2mg/dl) ist, auslösen. Das schließt beispielsweise auch die Werte 0, 0,2, 0,4 mmol/l (0, 4, 8 mg/dl), und jede andere positive Zahl mit ein.

Bei der Auswahl Deiner **Automatisierung** und der Wahl der Bedingungen und Werte, ist es wichtig genau zu wissen, welches Ziel damit erreicht werden soll.

(automations-automation-triggers)=
## Automation Triggers

![Automation Triggers](../images/automation_triggers.png)

There are various ‘Triggers’ that can be selected by the user. Triggers are the conditions that must be met in order for the automation to execute. Die folgende Liste ist nicht vollständig:

**Trigger:** connect conditions

**Optionen:**

Mehrere Auslöser können mit den folgenden Bedingungen miteinander verknüpft werden
* „Und“
* „Oder“
* „Entweder oder“ (d. h. eine (und nur eine) der Bedingungen muss zutreffen, damit die Aktion ausgeführt wird)

**Trigger:** time vs. recurring time

**Optionen:**

* Zeit = einmaliges Ereignis
* Wiederholungszeit = etwas, das regelmäßig passiert (z. B. einmal pro Woche, jeden Werktag etc.)

**Trigger:** location

**Optionen:**

* In den **Einstellungen** der Automatisierungen, kann der gewünschte Standortdienst ausgewählt werden.

**Trigger:** location service

**Optionen:**

* Passiven Standort verwenden: **AAPS** nutzt nur die Standorte, wenn sie von anderen Apps angefordert werden.
* Netzwerkstandort: Standort Ihres Wi-Fi.
* GPS-Standort (Achtung! Kann zu übermäßigem Akkuverbrauch führen!)

**Triggers** : pump and sensor data

* Cannula age trigger: Available for all pumps
* Insulin age trigger: Available for supported pumps
* Battery age trigger: Available for supported pumps
* Sensor age trigger: always available
* Pod Activation trigger: Available for patch pumps

Note that for all age related triggers the equal comparison is unlikely to trigger, so in that case two triggers are required to create a range

* Reservoir level trigger: Available for all pumps, comparison "NOT\_AVAILABLE" is not working for this trigger as the value is always filled in **AAPS**
* Pump battery level trigger: Available for supported pumps, comparison "NOT\_AVAILABLE" is not working for this trigger as the value is always filled in **AAPS**

## Aktion

![Automation Triggers](../images/automation_actions.png)

**Aktion:** **Temporäres Ziel** (TT) starten

**Optionen:**

* **Glukosewert** muss zwischen 72 mg/dl und 270 mg/dl (bzw. zwischen 4 mmol/l und 15 mmol/l) liegen
* **TT**> funktioniert nur, wenn aktuell kein temporäres Ziel eingestellt ist

**Aktion:** **Temporäres Ziel** (TT) stoppen

**Optionen:**

kein(e)

**Aktionen:** **Profil Prozentsatz**

**Optionen:**

* **Prozentsatz** muss zwischen 70% und 130% liegen
* funktioniert nur, wenn das Profil zu dem Zeitpunkt mit 100% läuft

Sobald die Aktion hinzugefügt wurde, müssen die voreingestellten Werte durch Klicken auf Deine Wünsche angepasst werden.

![Alt text](../images/automation_2024-02-12_20-57-07.png)

(Automations-the-order-of-the-automations-in-the-list-matters)=
## Die Reihenfolge innerhalb der Liste der **Automatisierungen** ist entscheidend
 **AAPS** ordnet die Regeln in der Reihenfolge, wie sie erstellt wurden und beginnt bei der oberen Automatisierung mit dem Abarbeiten der **Automatisierungsliste**. Wenn beispielsweise **Automatisierung** „Low“ (dt. Hypobehandlung) unter allen **Automatisierungsregeln** die wichtigste **Automatisierung** ist, sollte diese ganz oben auf der Liste Deiner **Automatisierungen** erscheinen:


![Alt text](../images/automation_2024-02-12_20-57-48.png-500x.png)

Um die Reihenfolge der **Automatisierungsregeln** zu ändern, drücke und halte den Button mit den vier Strichen am rechten Rand der Anzeige. Sortiere die  **Automatisierungen** neu, indem Du die entsprechende Regel nach oben oder unten verschiebst.

![Alt text](../images/automation_2024-02-12_20-58-00.png-500x.png)

## Löschen von Automatisierungsregeln

Klicke auf das Papierkorbsymbol, um eine **Automatisierungsregel** zu löschen.

![Alt text](../images/automation_2024-02-12_20-58-26.png-500x.png)

# Beispiele für Automatisierungen

Es folgen nun einige Beispiele für **Automatisierungen**. Weiterführende und tiefere Diskussionen über **Automatisierungen** im allgemeinen und einige Praxisbeispiele findest Du entweder in den Facebook-Gruppen oder auf Discord. Die folgenden Beispiele sollten nicht blind übernommenen werden. Wichtig ist, die genaue Funktionsweise der jeweiligen </strong>Automatisierung** zu verstehen, bevor sie genutzt wird.</p>

### Temporäres Ziel bei niedrigem Blutzucker

Diese **Automatisierung** setzt beim Erreichen eines bestimmten **Glukosewerts** ein niedriges temporäres Ziel.

![Alt text](../images/automation_2024-02-12_21-04-01.png-500x.png)

### Temporäres Ziel zur Mittagszeit (abhängig vom 'Standort')

![Alt text](../images/automation_2024-02-12_21-04-25.png-500x.png)

Diese **Automatisierung** wurde für eine Person erstellt, die das Mittagessen an Werktagen (Mo - Fr) ungefähr zur gleichen Zeit auf der Arbeit isst, und nur ausgeführt wird, wenn die Person an einem bestimmten 'Standort' ist.  Sollte die Person nicht auf der Arbeit sein, wird diese **Automatisierung** folglich nicht ausgeführt werden.

Diese **Automatisierung** setzt in Vorbereitung auf das Mittagsessen um 13.00h für 30 Minuten ein niedriges **temporäres Ziel** (Bald Essen), um den Glukosewert auf bis 90 mg/dl (oder 5 mmol/l) zu bringen.

Der Standort wird als 'Auslöser' eingestellt, indem die Koordinaten für Breitengrad und Längengrad wie unten angegeben werden:

![Alt text](../images/automation_2024-02-12_21-04-40.png-500x.png)

Aufgrund der ‘Und’-Verknüpfung wird die **Automatisierung** nur dann ausgeführt, wenn die Person sich zum gewählten Zeitpunkt am hinterlegten Standort aufhält.

Diese **Automatisierung** wird zu keinem anderen Zeitpunkt an diesem Standort ausgeführt. Sie wird auch nicht ausgeführt, wenn man sich zum gewählten Zeitpunkt weiter als 50 Meter von der hinterlegten GPS-Position aufhält.

### WLAN SSID und Standort-Automatisierungen

Wenn eine **Automatisierung** nur dann ausgelöst werden soll, wenn man sich in einem bestimmten WLAN-Bereich befindet, ist 'WLAN SSID' ist ein guter Weg das umzusetzen. Die WLAN SSID ist im Vergleich zur GPS Position recht genau, nutzt dabei weniger Akkuleistung und funktioniert auch in geschlossenen Räumen an denen GPS oder andere Standortdienste eventuell nicht verfügbar sind.

Hier nun ein weiteres Beispiel für das frühzeitige Setzen eines **temporären Ziels** an Werktagen für das Frühstück (1).


Die **Automatisierung** wird montags - freitags (2), wenn man sich im heimischen WLAN (3) befindet, ausgelöst.


Es wird dann ein **temporäres Ziel** von 75 mg/dl für 30 Minuten (4) gesetzt. Den Standort zu berücksichtigen hat den Vorteil, dass die Automatisierung (zum Beispiel auf Reisen) nicht gestartet wird.

![Alt text](../images/automation_2024-02-12_21-05-02.png-500x.png)

Der Screenshot zeigt die detaillierten Auslöser der **Automatisierung**:

1) Im “UND”-Rahmen (beide Bedingungen müssen erfüllt sein, damit ausgelöst wird) 1) Wiederholungszeit = Mo, Di, Mi, Do, Fr um 5:30h  
1) WIFI SSID = My_Home_WiFi_Name

![Alt text](../images/automation_2024-02-12_21-05-16.png-500x.png)

# Automating Preference Settings Export

### Unattended Exports: scheduled (daily)

Screenshots detailing the Automation triggers:

1) Condition: Recurring time = M,T,W,T,F At 8:00am 1) Action: Settings Export (For "Text in treatments" enter "Daily")

![Scheduled exports](../images/Automations/automation_settingsexport_scheduled_400px.png)

Note: Export execution will be logged on Careportal

### Unattended Exports: Pod Activation (patch pump only)

Screenshots detailing the Automation triggers:

1) Condition: Pod Activation 1) Action: Settings Export (For "Text in treatments" enter "Pod Activation: settings export")

![Export on Pod activation](../images/Automations/automation_settingsexport_podactivation_400px.png)

Note: Export execution will be logged on Careportal. Note : Automation will not trigger **at all** if you have not done a manual settings export before. See [Preferences > Maintenance](#preferences-maintenance-settings) for proper activation of unattended settings export.


# Automatisierungsprotokolle (Logs)

Es gibt unten am Rand des Reiters eine **AAPS**Protokollierung der zuletzt ausgelösten **Automatisierung**.

Im Beispiel unten wird das Protokoll angezeigt:

(1) um 01:58 Uhr wird „Low BG Trigger temp hypo profil“ ausgelöst
* der Glukosewert ist kleiner als 75mg/dl;
* das Delta ist negativ (d.h. der Glukosewert sinkt);
* die aktuelle Zeit liegt zwischen 01:00h und 06:00h.

Die **Automatisierung** wird:
* ein **temporäres Ziel** auf 110mg/dl für 40 Minuten setzen;
* eine **Profilanpassung** auf 50% für 40 Minuten vornehmen.

(2) um 03:38 Uhr wird „High carb after low at night“ ausgelöst
* die aktuelle Zeit liegt zwischen 01:05h und 06:00h;
* der Glukosewert ist größer (höher) als 110mg/dl.

Die **Automatisierung** wird:
* einen **Profilwechsel** zum LocalProfile1 ausführen (d.h. das temporäre Profil wird beendet, sofern es aktiv ist)
* ein **temporäres Ziel** beenden (sofern eines aktiv ist)

![Alt text](../images/automation_2024-02-12_21-05-56.png-500x.png)

## Problembehandlung

* Problem: __Meine Automatisierungen werden durch AAPS nicht gestartet__

Setze einen Haken im Kästchen neben der **Automatisierung**, um sicherzustellen, dass die Regel aktiviert ist.

## Problembehandlung

![Alt text](../images/automation_2024-02-12_21-06-12.png-500x.png)

* Problem: __Meine Automatisierungen werden in der falschen Reihenfolge gestartet.__

Überprüfe die Reihenfolge der Regeln in Deiner Liste, so es oben beschrieben wurde.

## Alternativen zu einer Automatisierung

Für fortgeschrittene Benutzer gibt es andere Möglichkeiten, Aufgaben mit IFTTT oder einer Drittanbieter-Android-App namens Automate zu automatisieren. 
