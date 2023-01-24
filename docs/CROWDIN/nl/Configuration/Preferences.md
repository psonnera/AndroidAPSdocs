# Instellingen

- **Open preferences** by clicking the three-dot menu on the top right side of the home screen.

  ```{image} ../images/Pref2020_Open2.png
  :alt: Open instellingen
  ```

- Je kunt direct naar voorkeuren springen voor een bepaald tabblad (bijv. pump tab) by opening this tab and clicking Plugin preferences.

  ```{image} ../images/Pref2020_OpenPlugin2.png
  :alt: Open plugin instellingen
  ```

- **Submenu's** kun je openen door te klikken op de driehoek onder de sub-menu titel.

  ```{image} ../images/Pref2020_Submenu2.png
  :alt: Open submenu
  ```

- Met de **filter** functie bovenaan het instellingenscherm kun je snel naar bepaalde voorkeuren gaan. Begin simpelweg een deel van de tekst die je zoekt, te typen.

  ```{image} ../images/Pref2021_Filter.png
  :alt: Instellingen filter
  ```

```{contents}
:backlinks: entry
:depth: 2
```

## Algemeen

**Eenheden**

- Stel eenheden in op mmol/l of mg/dl, afhankelijk van wat je gewend bent.

**Taal**

- Nieuwe optie om de standaard ingestelde taal van jouw telefoon te gebruiken (aanbevolen).

- In case you want AAPS in a different language than your standard phone language you can choose from a broad variety.

- Let op: Als je een andere taal kiest dan de standaardtaal van jouw telefoon, dan zie je soms een mix van talen. This is due to an android issue that overriding the default android language sometimes doesn't work.

  ```{image} ../images/Pref2020_General.png
  :alt: Instellingen > Algemeen
  ```

**Naam patiënt**

- Handig als je onderscheid moet maken tussen meerdere setups (er zijn bijvoorbeeld twee mensen met diabetes in jouw gezin).

### Beveiliging

#### Masterwachtwoord

- Noodzakelijk om instellingen te kunnen [exporteren](../Usage/ExportImportSettings.md) als ze zijn versleuteld. (Geldt vanaf AAPS versie 2.7).
  **Biometric protection may not work on OnePlus phones. This is a known issue of OnePlus on some phones.**

- Open Preferences (three-dot menu on top right of home screen)

- Klik op de driehoek onder "Algemeen"

- Klik op "Masterwachtwoord"

- Voer het wachtwoord in, bevestig het wachtwoord en klik op ok.

  ```{image} ../images/MasterPW.png
  :alt: Masterwachtwoord instellen
  ```

#### Instellingenbeveiliging

- Bescherm jouw instellingen met een wachtwoord of met de biometrische verificatie van jouw telefoon (bijv. [een kind gebruikt AAPS](../Children/Children.md)).

- Er moet een aangepast wachtwoord worden gebruikt als je het masterwachtwoord alleen wilt gebruiken voor het beveiligen van [geëxporteerde instellingen](../Usage/ExportImportSettings.md).

- Als je een aangepast wachtwoord gebruikt, klik op de regel "Instellingen wachtwoord" om het wachtwoord in te stellen zoals [boven](../Configuration/Preferences#masterwachtwoord) beschreven.

  ```{image} ../images/Pref2020_Protection.png
  :alt: Beveiliging
  ```

#### App beveiliging

- Als de app is beveiligd moet je het wachtwoord invoeren of de biometrische verificatie van de telefoon gebruiken om AAPS te openen.
- De app zal onmiddellijk worden afgesloten als er een verkeerd wachtwoord is ingevoerd-maar nog steeds op de achtergrond worden uitgevoerd als de app al succesvol geopend was.

#### Bolus beveiliging

- Bolus beveiliging kan nuttig zijn als AAPS wordt gebruikt door een klein kind en u [bolus via SMS](../Children/SMS-Commands.md) gebruikt.

- In het voorbeeld hieronder zie je dat de app vraagt om biometrische verificatie. Mocht de biometrische verificatie niet werken, klikt dan in de ruimte boven het witte venster en voer het masterwachtwoord in.

  ```{image} ../images/Pref2020_PW.png
  :alt: Vraag biometrische verificatie
  ```

#### Skin

- Je kunt kiezen uit drie soorten skins:

  ```{image} ../images/Pref2021_SkinWExample.png
  :alt: Kies skin + voorbeelden
  ```

- 'Lage resolutie skin' komt met korter label en leeftijds/niveau verwijderd om meer beschikbare ruimte te hebben op een zeer laag resolutie scherm.

- Dit verschilt, afhankelijk van de oriëntatie van de telefoon.

##### Staande stand

- **Klassiek weergave thema** en **Knoppen worden altijd weergegeven aan de onderkant van het scherm** zijn identiek
- **Large Display** has an increased size of all graphs compared to other skins

##### Liggende stand

- Wanneer je voor **Klassiek weergave thema** en **Groot scherm**, moet je naar beneden scrollen om de knoppen onder aan het scherm te zien

- **Large Display** has an increased size of all graphs compared to other skins

  ```{image} ../images/Screenshots_Skins.png
  :alt: "Skins afhankelijk van de ori\xEBntatie van de telefoon"
  ```

## Overzicht

- In deze sectie kun je instellen hoe het Overzicht scherm eruit ziet.

  ```{image} ../images/Pref2020_OverviewII.png
  :alt: Instellingen > Overzicht
  ```

### Laat scherm aan

- Handig wanneer je een presentatie geeft.
- Het verbruikt wel veel energie, dus het is verstandig om je telefoon hierbij aan een lader te hebben.

### Knoppen

- Kies welke knoppen zichtbaar zijn onderaan jouw Overzicht-scherm.

- Je vind hier ook enkele keuzeopties voor het dialoogvenster dat je gaat zien na het indrukken van zo'n knop.

  ```{image} ../images/Pref2020_OV_Buttons.png
  :alt: Instellingen > Knoppen
  ```

### Vaste maaltijd

- Via Vaste maaltijd instellingen kun je een knop toevoegen aan het Overzicht-scherm voor een snack of maaltijd die je vaker eet. Je kunt instellen hoeveel koolhydraten de maaltijd bevat, en instellen hoe AAPS de bolus moet berekenen.

- Je kunt maar één Vaste maaltijdknop tegelijkertijd op het Overzicht scherm laten weergeven. In de instellingen stel je in gedurende welk tijdsvak een bepaalde maaltijdknop wordt weergegeven.

- Als je op op jouw Overzicht scherm op de Vaste maaltijdknop hebt gedrukt, dan zal AAPS een bolus voorstellen voor de koolhydraten uit die maaltijd. AAPS gebruikt hiervoor jouw actieve profiel instellingen (hij neemt hierbij jouw bloedglucose of insuline aan boord mee in zijn berekeinging, als je dat zo hebt ingesteld).

- Je moet het voorstel bevestigen voordat de insuline wordt afgeleverd.

  ```{image} ../images/Pref2020_OV_QuickWizard.png
  :alt: Instellingen > Vaste maaltijdknop
  ```

### Standaard tijdelijke streefdoelen

- [Temp targets (TT)](../Usage/temptarget.md) allow you to define change your blood glucose target for a certain time period.

- Je kunt zelf instellen welke BG waarde en welke tijdsduur AAPS gebruikt bij de verschillende standaard tijdelijke streefdoelen: activiteit, eet binnenkort en hypo.

- Om een bepaald tijdelijk streefoel te activeren heb je drie opties: houd het streefdoel in de rechterbovenhoek van jouw Overzicht scherm lang ingedrukt, of gebruik de knop op het Activiteit tabblad, of zet een vinkje via de oranje "Koolhydraten" knop aan de onderkant. Alledrie hebben hetzelfde resultaat.

  ```{image} ../images/Pref2020_OV_DefaultTT.png
  :alt: Instellingen > Standaard tijdelijke streefdoelen
  ```

### Ontlucht/Vul standaard insuline hoeveelheden

- If you want to fill tube or prime cannula through AAPS you can do this through [actions tab](../Getting-Started/Screenshots#action-tab).
- Je kunt zelf kiezen welke standaardhoeveelheden AAPS laat zien in het dialoogvenster dat ontlucht/vul knop zit.

### Bereik voor visualisatie

- Bepaal tussen welke waardes de BG grafiek op het Overzicht scherm het voor jou 'groene gebied' weergeeft. NB: dit bepaalt alleen het uiterlijk van jouw grafiek, verwar deze waardes niet met het BG streefdoel uit jouw profiel!

  ```{image} ../images/Pref2020_OV_Range2.png
  :alt: Instellingen > Bereik voor visualisatie
  ```

### Afgekorte tab titels

- Hiermee passen er meer tabbladen naast elkaar op je scherm.

- Bijvoorbeeld het 'CONFIGURATOR' tabblad wordt 'CONF', 'ACTIES' wordt 'ACT' etc.

  ```{image} ../images/Pref2020_OV_Tabs.png
  :alt: Instellingen > Tabbladen
  ```

### Toon notities veld in behandeling dialoogvensters

- Hiermee krijg je de optie om notities toe te voegen wanneer je een behandeling invoert via één van de dialoogvensters (bolus calculator, koolhydraten, insuline, ...)

  ```{image} ../images/Pref2020_OV_Notes.png
  :alt: Instellingen > Notities in behandeldialogen
  ```

### Statusindicatoren

- Statusindicatoren geven een visuele waarschuwing voor

  Sensor Leeftijd
  \* Sensor batterijniveau voor bepaalde sensor-opzetstukken (bijv Miaomiao) Zie [screenshots pagina](../Getting-Started/Screenshots#sensorniveau-batterij) voor details.
  \* Insuline leeftijd (aantal dagen dat reservoir wordt gebruikt)
  \* Reservoir niveau (eenheden)
  \* Infuus leeftijd
  \* Pompbatterij leeftijd
  \* Pompbatterij niveau (%)

- Als de drempelwaarde voor waarschuwing wordt overschreden, worden de waarden in geel weergegeven.

- Als de drempelwaarde voor alarm wordt overschreden, worden de waarden in rood weergegeven.

- In versies ouder dan AAPS 2.7 moest je de instellingen voor statusindicatoren nog aanpassen in Nightscout, nu kan dit direct hier in AAPS.

  ```{image} ../images/Pref2020_OV_StatusLights2.png
  :alt: Istellingen > Statusindicatoren
  ```

### Geavanceerde instellingen (Overzicht)

```{image} ../images/Pref2021_OV_Adv.png
:alt: Istellingen > Statusindicatoren
```

#### Voer dit deel van het boluscalculator resultaat uit

- Met deze instelling laat je slechts een deel toedienen van de uitkomst van de boluscalculator.
- Alleen het ingestelde percentage (moet tussen 10 en 100 liggen) van de berekende bolus wordt afgeleverd wanneer de boluscalculator wordt gebruikt.
- Het percentage zie je terug in de boluscalculator.

#### Bolusadviseur

- Als je de [Bolus calculator](../Getting-Started/Screenshots#bolus-calculator) gebruikt en je glucose waarde is hoger dan 10 mmol/l (180 mg/dl) wordt een correctie bolus voorgesteld.

- If correction bolus is accepted **no carbs** will be recorded.

- Er zal een alarm afgaan wanneer de glucosewaarde genoeg is gedaald om te beginnen met eten.

- Je moet op dat moment de [Bolus calculator](../Getting-Started/Screenshots#bolus-calculator) opnieuw gebruiken en daar de hoeveelheid koolhydraten invoeren die je wilt eten.

  ```{image} ../images/Home2021_BolusWizard_CorrectionOffer.png
  :alt: Bolusadviseur bericht
  ```

#### Superbolus

- Geeft de superbolus optie weer in de boluswizard.
- Dmv [Superbolus](https://www.diabetesnet.com/diabetes-technology/blue-skying/super-bolus/) kun je wat insuline "naar voren halen" van de basaal die je de komende twee uur zou hebben gekregen. Dit om (maaltijd)pieken te voorkomen.

## Behandelingen veiligheid

### Patient type

- Veiligheidslimieten worden ingesteld op basis van de leeftijd die je in deze instelling selecteert.
- Als je tegen de beperkingen van zo'n zogenaamde 'harde limiet' (zoals max bolus) aanloopt, dan is het tijd om te kiezen voor de daaropvolgende categorie.
- It's a bad idea to select higher than real age because it can lead to overdosing by entering the wrong value in insulin dialog (by skipping the decimal dot, for example).
- Als je wilt weten wat de precieze getallen zijn voor deze veiligheidslimieten, ga dan naar [deze pagina](../Usage/Open-APS-features.md) en scroll naar het algoritme dat jij gebruikt.

### Max toegestane bolus \[E\]

Dit is de maximale hoeveelheid bolus insuline die AAPS mag leveren.
\* Deze instelling is een veiligheidslimiet om te voorkomen dat er per ongeluk een enorme bolus wordt afgegeven door een misrekening of typfout van de gebruiker.
\* Het wordt aangeraden om deze in te stellen op de maximale hoeveelheid bolus insuline die je ooit voor een maaltijd of correctie nodig zult hebben.
\* Deze beperking wordt ook toegepast op de resultaten van de Boluscalculator.

### Max toegestane koolhydraten \[g\]

- Dit is de maximale hoeveelheid koolhydraten waarvoor de Boluscalculator insuline mag geven.
- Deze instelling is een veiligheidslimiet om te voorkomen dat er per ongeluk een enorme bolus wordt afgegeven door een misrekening of typfout van de gebruiker.
- Het wordt aangeraden om deze in te stellen op de maximale hoeveelheid koolhydraten die je ooit zult eten bij een maaltijd.

## Loop

### APS Mode

- Schakelt tussen open loop, gesloten loop en 'stop bij laag'
- **Open loop** betekent dat AAPS indien nodig suggesties doet voor hogere/lagere basaalstanden. After manual confirmation, the command to dose insulin will be transferred to pump.
- **Closed loop** (gesloten loop) betekent dat hogere/lagere basaalstanden (en SMBs, als je dat aan hebt staan) automatisch naar je pomp worden verzonden zonder bevestiging of invoer van jou.
- **Low glucose suspend** is similar to closed looping, but overrides the maxIOB setting to zero. This means that if blood glucose is dropping it can reduce the basal rate, but if blood glucose is rising then it will only increase the basal rate if the basal IOB is negative (e.g. from a previous Low Glucose Suspend).

### Minimale verzoek voor aanpassing \[%\]

- Bij het gebruik van open loop ontvangt je meldingen telkens wanneer AAPS een suggestie doet om de basaalstand aan te passen.
- Om het aantal meldingen te verminderen, kun je een breder bereik voor BG gebruiken of een hier hoger percentage van het minimale verzoek voor aanpassing instellen.
- Hiermee stel je de minimale relatieve TBR aanpassing in waarbij AAPS een suggestie doet.

## Advanced Meal Assist (AMA) of Super Micro Bolus (SMB)

Afhankelijk van jouw instellingen in de [Configurator](../Configuration/Config-Builder.md) kun je kiezen tussen twee algoritmes:

- [Advanced Meal Assist (OpenAPS AMA)](../Usage/Open-APS-features#geavanceerde-maaltijdhulp-ama) (Geavanceerde maaltijdhulp) - status van het algoritme in 2017
- [Super Micro Bolus (OpenAPS SMB)](../Usage/Open-APS-features#super-micro-bolus-smb) - meest recente algoritme voor ervaren gebruikers

### OpenAPS AMA instellingen

- Dankzij de geavanceerde maaltijdhulp (Advanced Meal Assist, AMA) kan het systeem na een maaltijdbolus sneller een hogere tijdelijke basaalstand geven, zolang je wel je koolhydraten correct hebt ingevoerd.
- Meer details over de instellingen en Autosens zijn te vinden in de \` OpenAPS docs \<<https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autosens.html>>\` \_\_.

#### Maximaal instelbaar basaal E/u

- Deze instelling is een veiligheidslimiet om te voorkomen dat AAPS ooit een gevaarlijk hoge basaalstand kan instellen.
- Dit getal wordt weergegeven in eenheden per uur (E/uur).
- We raden je aan je verstand te gebruiken bij het invullen van deze waarde. Een goede aanbeveling is om de hoogste basaalstand in je profiel te nemen en die te **vermenigvuldigen met 4**.
- Als de hoogste basaalstand in je profiel bijvoorbeeld 0,5 E/uur is, dan moet je dat vermenigvuldigen met 4 om een waarde van 2 E/uur te krijgen.
- Zie ook de [gedetailleerde functiebeschrijving](../Usage/Open-APS-features#maximale-e-uur-dat-een-tijdelijke-basaalstand-kan-toedienen-openaps-max-basal).

#### Max totaal IOB dat OpenAPS niet kan overschrijden \[E\]

- Hoeveelheid extra basale insuline (in eenheden) tot waaraan OpenAPS de hoeveelheid insuline in jouw lichaam mag laten oplopen, bovenop je normale basale insuline.
- Zodra deze waarde is bereikt, zal AAPS stoppen met het geven van extra basale insuline totdat jouw basale Insulin On Board (IOB, insuline aan boord) naar binnen dit bereik is teruggelopen.
- Deze waarde **laat bolus IOB buiten beschouwing**, alleen basale insuline wordt meegerekend.
- Het berekenen en sturen op deze waarde gebeurt onafhankelijk van jouw normale basale insuline. Alleen de extra basale insuline die werd afgegeven bovenop je normale basaalstand, wordt meenomen.

Wanneer je begint met loopen, wordt tijdens een van de leerdoelen een tijd lang Max Basal IOB beperkt naar 0, zodat je gewend raakt aan het systeem. Dit zorgt ervoor dat AAPS helemaal geen extra basale insuline kan geven. Terwijl AAPS wel je basale insuline naar beneden kan bijstellen, of zelfs helemaal uitschakelen om een hypo te helpen voorkomen. Dit is een belangrijke stap omdat:

- Je de tijd krijgt om veilig gebruik te maken van het AAPS-systeem en rustig kunt observeren hoe het werkt.
- Je nu de kans hebt om jouw basaalprofiel en insuline gevoeligheidsfactor (ISF, Insulin Sensitivity Factor) perfect te maken.
- Je kunt zien hoe AAPS jouw basale insuline naar beneden bijstelt om hypo's te voorkomen.

Pas na een tijd mag je het systeem toestaan om extra basale insuline te geven door de Max Basal IOB waarde te verhogen. Als eerste start wordt aangeraden om de hoogste basaalstand in je profiel te nemen en die te **vermenigvuldigen met 3**. Als de hoogste basaalstand in je profiel bijvoorbeeld 0,5 E/uur is, dan moet je dat vermenigvuldigen met 3 om een waarde van 1.5 E/uur te krijgen.

- Je kunt voorzichtig beginnen met deze waarde en deze langzaam verhogen.
- Dit zijn alleen richtlijnen; ieder mens is anders. Je kunt onderweg merken dat jij zelf minder of meer nodig hebt dan wat hier wordt aanbevolen, begin altijd voorzichtig en pas langzaam aan.

**Opmerking: om veiligheidsredenen geldt er voor Max Basal IOB een 'harde limiet' (voor volwassenen is die 7E). Zie ook de pagina over "OpenAPS functies" elders in deze wiki.**

#### Gevoeligheidsdetectie (Autosens)

- [Autosens](../Usage/Open-APS-features#autosens) kijkt naar bloedglucoseafwijkingen (positieve/negative/neutrale).
- Op basis van deze afwijkingen kijkt AAPS of je gevoeliger (of, juist ongevoeliger) bent voor insuline, en zal vervolgens jouw basaalstanden en ISF aanpassen.
- Als je "Autosens past ook het streefdoel aan" selecteert, zal het algoritme ook je BG streefdoel wijzigen.

#### Geavanceerde instellingen (OpenAPS AMA)

- Normaal gesproken hoef je deze instellingen niet te wijzigen!
- Als je ze toch wilt veranderen, zorg er dan voor dat je de details in de [OpenAPS docs](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/preferences-and-safety-settings.html#) leest en begrijpt wat je doet.

### OpenAPS SMB instellingen

- In tegenstelling tot AMA gebruikt [SMB](../Usage/Open-APS-functies#super-micro-bolus-smb) meestal geen tijdelijke basaalstanden om glucosewaarden bij te sturen, maar voornamelijk kleine bolusen: de zgn super micro bolussen.

- You must have started [objective 9](../Usage/Objectives#objective-9-enabling-additional-oref1-features-for-daytime-use-such-as-super-micro-bolus-smb) to use SMB.

- De eerste drie instellingen worden [hierboven](../Configuration/Preferences#maximaal-instelbaar-basaal-e-u) uitgelegd.

- De verschillende opties voor inschakelen van SMB worden beschreven op de pagina met [OpenAPS functies](../Usage/Open-APS-features#activeer-smb).

- *Tijdsinterval in minuten tussen afgeven van SMBs* is een beperking voor hoe snel na elkaar twee SMBs mogen worden gegeven, dit staat standaard op 4 min. Deze waarde voorkomt dat het systeem te vaak SMB afgeeft (bijvoorbeeld in geval van een tijdelijk streefdoel). Wijzig deze instelling alleen als je precies weet wat de gevolgen zijn.

- Als 'Gevoeligheid verhoogt het doel' of 'Resistentie verlaagt het doel' is ingeschakeld dan zal [Autosens](../Usage/Open-APS-features#gevoeligheidsdetectie-autosens) jouw BG streefdoel overeenkomstig aanpassen.

- Als Autosens het streefdoel wijzigt, dan wordt het streefdoel op jouw Overzicht scherm in groen weergegeven.

  ```{image} ../images/Home2020_DynamicTargetAdjustment.png
  :alt: Streefdoel gewijzigd door autosens
  ```

#### Waarschuwing 'koolhydraten nodig'

- Deze functie is alleen beschikbaar als je het SMB-algoritme gebruikt.

- Wanneer het algoritme denkt dat je extra koolhydraten nodig hebt om te voorkomen dat je een hypo krijgt, zal hij een waarschuwing geven.

- Je hebt de mogelijkheid om deze waarschuwing te snoozen voor 5, 15 of 30 minuten.

- De benodigde hoeveelheid koolhydraten wordt ook weergegeven in de COB sectie op het Overzicht scherm.

- A threshold can be defined - minimum amount of carbs needed to trigger a notification.

- 'Koolydraten nodig' meldingen kunnen worden gepusht naar Nightscout als je dat wenst, dan zal er een notitie worden gemaakt en naar Nightscout gestuurd.

  ```{image} ../images/Pref2020_CarbsRequired.png
  :alt: Koolhydraten nodig op het startscherm
  ```

#### Geavanceerde instellingen (OpenAPS SMB)

- Normaal gesproken hoef je deze instellingen niet te wijzigen!
- Als je ze toch wilt veranderen, zorg er dan voor dat je de details in de [OpenAPS docs](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/preferences-and-safety-settings.html#) leest en begrijpt wat je doet.

## Opname instellingen

```{image} ../images/Pref2020_Absorption.png
:alt: Opname instellingen
```

### min_5m_carbimpact

- Het algoritme maakt gebruik van BGI (bloedglucose impact) om te bepalen wanneer koolhydraten zijn geabsorbeerd.

- Deze waarde wordt gebruikt om de hoeveelheid opgenomen koolhydraten (Carbs On Board, COB) te laten afnemen wanneer jouw bloedsuiker niet zoveel stijgt als het algoritme had verwacht nadat je koolhydraten hebt gegeten. Deze waarde wordt alleen gebruikt in speciale gevallen: wanneer jouw CGM geen gegevens doorgeeft, of wanneer bijv. fysieke activiteit de koolhydraten "opeet".

- At times when carb absorption can’t be dynamically worked out based on your blood's reactions it inserts a default decay to your carbs. Het is in feite een vangnet.

- Om het simpel te stellen: Het algoritme "weet" hoe jouw BGs zich *zouden* moeten gedragen, adhv jouw huidige hoeveelheid insuline icm ISF.

- Wanneer jouw BG sneller daalt dan het algoritme had verwacht, dan betekent dit dat er koolhydraten worden geabsorbeerd (COB neemt af). Hierbij geldt: grote verandering = veel koolhydraten.

- De min_5m_carbimpact is wat het algoritme gebruikt als minimale hoeveel koolhydraten die per 5 minuten worden geabsorbeerd. Zie voor meer informatie [OpenAPS docs](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/preferences-and-safety-settings.html?highlight=carbimpact#min-5m-carbimpact).

- Standaard waarde voor AMA is 5, voor SMB is het 8.

- De COB-grafiek op het Overzicht scherm geeft dmv een oranje stip op de COB lijn weer wanneer min_5m_impact wordt gebruikt.

  ```{image} ../images/Pref2020_min_5m_carbimpact.png
  :alt: COB grafiek
  ```

### Maximale maaltijd absorptie tijd

- Als je vaak maaltijden met een hoog vet- of eiwitgehalte eet, moet je de opnametijd verhogen.

### Geavanceerde instellingen - autosens ratio

- Stel jouw min. en max. [autosens](../Usage/Open-APS-features#autosens) ratio in.
- Standaard waarden (max. 1,2 en min. 0,7) zouden niet gewijzigd hoeven worden. NB: deze getallen komen overeen met 120% en 70%.

## Pomp instellingen

De opties hier zijn afhankelijk van welke pomp je hebt geselecteerd in de [Configurator](../Configuration/Config-Builder#pomp).  Koppel en stel je pomp in volgens de instructies van jouw pomp:

- [DanaR](../Configuration/DanaR-Insulin-Pump.md)
- [DanaRS](../Configuration/DanaRS-Insulin-Pump.md)
- [Accu Chek Combo pomp](../Configuration/Accu-Chek-Combo-Pump.md)
- [Accu Chek Insight pomp](../Configuration/Accu-Chek-Insight-Pump.md)
- [Medtronic pomp](../Configuration/MedtronicPump.md)

Als je AndroidAPS gebruikt in 'open loop' modus, zorg er dan voor dat je Virtuele Pomp hebt geselecteerd in de Configurator.

## NSClient

```{image} ../images/Pref2020_NSClient.png
:alt: NSClient
```

- Stel de *Nightscout URL* in (bijv. <https://yourwebsitename.herokuapp.com>) en het *API geheim* (een wachtwoord van 12 tekens dat is vastgelegd in jouw Heroku-variabelen).

- Hierdoor kunnen gegevens zowel worden uitgelezen als weggeschreven tussen de Nightscout website en AndroidAPS.

- Als je vastzit in Doel 1, controleer dan goed of je hier geen typfouten hebt gemaakt.

- **Zorg ervoor dat de URL is ingevuld ZONDER /api/v1/ aan het eind.**

- Log app start naar Nightscout' zal elke keer dat de app is gestart, een notitie maken.  De app zou niet vaker dan één keer per dag opnieuw moeten starten; gebeurt dit vaker dan wijst dat op een probleem. Vaak wordt dit veroorzaakt doordat de accubesparings-functie van jouw telefoon steeds de app afsluit. Los dit op door de accubesparings-instellingen van jouw telefoon aan te passen. Het kan ook zijn dat jouw telefoon te weinig (werk)geheugen beschikbaar heeft. Zorg dan dat je niet teveel zware apps draait of maak geheugenruimte vrij.

- If activated changes in [local profile](../Configuration/Config-Builder#local-profile) are uploaded to your Nightscout site.

### Verbindings instellingen

```{image} ../images/ConfBuild_ConnectionSettings.png
:alt: NSClient verbindingsinstellingen
```

- Beperk Nightscout upload naar alleen Wi-Fi of zelfs naar bepaalde Wi-Fi SSID's.
- Als je alleen een specifiek WiFi-netwerk wil gebruiken, kun je de WiFi SSID invoeren.
- Meerdere SSID's kunnen worden gescheiden door puntkomma's.
- Om alle SSIDs te verwijderen vul je een spatie in in dit veld.

### Alarm opties

- Met de alarmopties kun je kiezen welke standaard Nightscout alarmen via de AAPS app moeten binnenkomen.
- Om een alarm te laten klinken moet je de Urgent High, High, Low en Urgent Low (Urgent Hoog, Hoog, Laag en Urgent Laag) alarmwaarden in jouw [Heroku variabelen](https://nightscout.github.io/nightscout/setup_variables/#alarms) instellen.
- Ze zullen alleen werken terwijl je een verbinding hebt met Nightscout en zijn bedoeld voor ouders/verzorgers die hun kind met diabetes willen volgen.
- Als jij zelf de CGM-bron op je telefoon hebt (bijv. xDrip+ or BYODA \[Build your own dexcom app\]) then use those alarms instead.

### Geavanceerde instellingen (NSClient)

```{image} ../images/Pref2020_NSClientAdv.png
:alt: NSClient geavanceerde instellingen
```

- De meeste opties in geavanceerde instellingen spreken voor zich.

- *Activeer lokaal delen* zal jouw gegevens doorsturen naar andere apps op je telefoon, zoals xDrip+.

  - Daarom kun je [via AAPS](../Configuration/Config-Builder#bg-bron) de Activeer lokaal delen optie aanzetten, en op die manier jouw gegevens naar xDrip+ sturen. Handig als je liever de uitgebreide alarm instellingen in xDrip+ gebruikt dan de alarm instellingen van de Dexcom app.

- *Gebruik altijd absolute basale waarden* moet geactiveerd worden als je Autotune correct wilt gebruiken. Zie [OpenAPS documentatie](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/understanding-autotune.html) voor meer informatie over Autotune.

## SMS Communicator

- Opties worden alleen weergegeven als de SMS-communicator is geselecteerd in [Configurator](../Configuration/Config-Builder#sms-communicator).
- Deze instelling maakt het mogelijk om de AAPS app op afstand (vanaf een andere telefoon) te bedienen, door SMS instructies te sturen naar de telefoon die de patiënt bij zich heeft. Bijvoorbeeld het uitschakelen van de loop of het geven van een bolus.
- Meer informatie in [SMS Commando's](../Children/SMS-Commands.md).
- Bediening via SMS is beveiligd dmv een authenticator app en een extra PIN code die achter het token moet worden gezet.

## Automatisering

Selecteer welke locatieservice moet worden gebruikt:

- Gebruik passieve locatie: AAPS neemt alleen locaties als andere apps erom vragen
- Gebruik netwerk locatie: Locatie van jouw Wifi
- Gebruik GPS-locatie (Let op! Dit kan veel batterijverbruik geven!)

## Lokaal gegenereerde waarschuwingen

```{image} ../images/Pref2020_LocalAlerts.png
:alt: Lokale waarschuwingen
```

- Instellingen spreken voor zich.

## Data Keuzes

```{image} ../images/Pref2020_DataChoice.png
:alt: Data keuzes
```

- Je kunt AAPS helpen verder te ontwikkelen door crashrapporten naar de ontwikkelaars te laten sturen.

## Onderhoud instellingen

```{image} ../images/Pref2020_Maintenance.png
:alt: Onderhoud instellingen
```

- Standaard mailadres om de logs heen te sturen is <mailto:logs@androidaps.org>.
- Als je *Encrypt geëxporteerde instellingen* selecteert, worden deze versleuteld met uw jouw [masterwachtwoord](../Configuration/Preferences#masterwachtwoord). In dat geval moet het masterwachtwoord elke keer dat de instellingen worden geëxporteerd of geïmporteerd, worden ingevoerd.

## Open Humans

- Je kunt de community helpen door je gegevens te doneren aan onderzoeksprojecten! Details kun je nalezen op de [Open Humans pagina](../Configuration/OpenHumans.md).

- In Instellingen kun je definiëren wanneer gegevens moeten worden geüpload

  - alleen uploaden indien verbonden met WiFi
  - enkel tijdens opladen