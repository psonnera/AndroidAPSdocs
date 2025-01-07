# Come usare il plugin Autotune (solo dev)

La documentazione sull'algoritmo di Autotune è disponibile nella [documentazione OpenAPS](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html).

Il plugin Autotune è un'implementazione dell'algoritmo di Autotune di OpenAPS all'interno di AAPS.

**Attualmente il Plugin Autotune è disponibile solo nel [ramo dev](../AdvancedOptions/DevBranch.md) e in modalità sviluppatore.**

![Plugin Autotune](../images/Autotune/Autotune_1.png)

## Interfaccia utente Autotune

![Schermata predefinita Autotune](../images/Autotune/Autotune_1b.png)

- È possibile selezionare nel menu a tendina di scelta Profilo, quello che si desidera aggiornare (come impostazione predefinita è selezionato il profilo attivo corrente)
  - Nota: Ogni volta che si seleziona un nuovo profilo, i risultati precedenti verranno rimossi e il parametro Tune Days verrà impostato sul valore predefinito
- Quindi Tune days è permette di definire il numero di giorni utilizzati nel calcolo per sintonizzare il tuo profilo. Il valore minimo è 1 giorno e il valore massimo 30 giorni. Questo numero non dovrebbe essere troppo basso per ottenere risultati corretti e regolari (oltre 7 giorni per ogni calcolo)
  - Nota: ogni volta che si cambia il parametro Tune Days, i risultati precedenti verranno rimossi
- Last Run è un link che recupera l'ultimo calcolo valido. Se non hai lanciato Autotune il giorno corrente, o se i risultati precedenti sono stati rimossi con una modifica del parametro di calcolo sopra riportata, allora puoi recuperare i parametri e i risultati dell'ultima esecuzione riuscita.
- Una nota segnala ad esempio, alcune informazioni sul profilo selezionato (se si hanno diversi valori IC o diversi valori ISF)
  - Nota: Il calcolo automatico funziona con un solo IC e un singolo valore ISF. Attualmente non esiste un algoritmo Autotune per sintonizzare un IC o un ISF circadiani. Se il tuo profilo di input ha diversi valori, puoi vedere nella sezione di avvisi il valore medio preso in considerazione per sintonizzare il tuo profilo.
- Il pulsante Controlla il profilo di Input consente una rapida verifica del profilo (Unità, DIA, IC, ISF, basale e target)
  - Nota: Autotune regola solo il tuo IC (valore singolo), ISF (valore singolo) e basale (con variazione circadiana). Le unità, la DIA e il target rimarranno invariati nel profilo di output.

- "Run Autotune" lancerà il calcolo di Autotune con il profilo selezionato e il numero di giorni di sintonizzazione
  - Nota: il calcolo automatico può richiedere molto tempo. Una volta lanciato, è possibile passare a un'altra schermata (come quella iniziale , ...) e tornare successivamente nel plugin Autotune per vedere i risultati

![Autotune Run start](../images/Autotune/Autotune_2b.png)

- Poi durante l'esecuzione i risultati intermedi verranno visualizzati nell'area sottostante

  - Nota: Durante l'esecuzione, le impostazioni sono bloccate, quindi non è più possibile modificare il profilo di input selezionato o il numero di giorni. Dovrai aspettare la fine del calcolo corrente se vuoi lanciare un'altra esecuzione con altri parametri.

  ![Autotune during run](../images/Autotune/Autotune_3b.png)

- Quando il calcolo di Autotune è finito, vedrai il risultato (profilo sintonizzato) e quattro pulsanti sotto.

![Risultati esecuzione Autotune](../images/Autotune/Autotune_4b.png)

- It's important to always compare input profile (column "Profile"), output profile (column "Tuned") and the percentage of variation for each value (Column "%").

- Per i valori della basale, avete anche il numero di "giorni mancanti". Ci sono giorni mancanti in cui Autotune non ha abbastanza dati classificati come "Basal" per regolare la velocità basale per questo periodo (ad esempio dopo ogni pasto quando si ha l'assorbimento di carboidrati). Questo numero dovrebbe essere il più basso possibile, specialmente quando la basale è importante (per esempio durante la notte o alla fine del pomeriggio)

- Il pulsante "Confronta profili" apre la visualizzazione del comparatore del profilo. Il profilo di input è in blu e il profilo di output (chiamato "Tuned") è in rosso.

  - Nota: nell'esempio sottostante il profilo di input ha una variazione circadiana per IC e ISF, ma il profilo calcolato in uscita ha un singolo valore. Se è importante per voi ottenere un profilo di output circadiano andate alla sezione [ IC circadiano o profilo ISF ](#circadian-ic-or-isf-profile) qui sotto.

  ![Comparatore profili Autotune](../images/Autotune/Autotune_5.png)

- Se ti fidi dei risultati (bassa percentuale di variazione tra il profilo di input e il profilo di output), puoi cliccare sul pulsante "Attiva il profilo" e poi cliccare su OK per convalidarlo.

  - Il profilo Activate Tuned creerà automaticamente un nuovo profilo "Tuned" nel plugin del profilo locale.
  - Se hai già un profilo chiamato "Tuned" nel plugin del tuo profilo locale, questo profilo verrà aggiornato con il profilo Autotune calcolato prima dell'attivazione

  ![Autotune Activate profile](../images/Autotune/Autotune_6.png)

- Se pensi che il profilo Tuned debba essere regolato (ad esempio se pensi che alcune variazioni siano troppo importanti), puoi cliccare sul pulsante "Copia sul profilo locale"

  - Un nuovo profilo con il prefisso "Tuned" e la data e l'ora di esecuzione saranno creati nel plugin del profilo locale

![Autotune Copia nel profilo locale](../images/Autotune/Autotune_7.png)

- È quindi possibile selezionare il profilo locale per modificare il profilo aggiornato (sarà selezionato come impostazione predefinita quando si apre il plugin del profilo locale)

  - the values in local profile will but rounded in the user interface to your pump capabilities

  ![Autotune aggiornamento profilo locale](../images/Autotune/Autotune_8.png)

- Se si desidera sostituire il profilo di input con il risultato Autotune, fare clic sul pulsante "Aggiorna profilo di input" e convalidare con OK

  - Nota: se fai clic su "Attiva il profilo" dopo "Aggiorna il profilo di input", attiverai il tuo profilo aggiornato e non il profilo predefinito "Tuned"?

  ![Autotune aggiornamento profilo di input](../images/Autotune/Autotune_9.png)

- Se è stato aggiornato il profilo di input, il pulsante "Aggiorna profilo di input" viene sostituito dal pulsante "Revert input profile" (vedere la schermata sottostante). Puoi vedere immediatamente in questo modo se il tuo attuale profilo di input nel plugin del profilo locale include già il risultato dell'ultima esecuzione o meno. Hai anche la possibilità di recuperare il tuo profilo di input senza risultati automatici con questo pulsante

  ![Autotune Aggiornamento profilo di input](../images/Autotune/Autotune_10.png)



## Impostazioni Autotune

(autotune-configurazione-plugin)=

### Autotune plugin settings

![Autotune default screen](../images/Autotune/Autotune_11.png)

- Cambio profilo automatica (default Off): vedi [Run Autotune con una regola di automazione ](#run-autotune-with-an-automation-rule) di seguito. Se si modifica questa impostazione in On, il profilo di input verrà automaticamente aggiornato dal profilo Tuned e verrà attivato.
  - **Fai attenzione, devi fidarti e verificare durante diversi giorni successivi, che dopo un aggiornamento e l'attivazione del profilo Tuned senza modifiche, il tuo loop migliori**

- Categorize UAM as basal (default On): Questa impostazione è per gli utenti che usano AndroidAPS senza alcun carbs inserito (Full UAM). Impedirà (quando disattivato) di classificare l'UAM come basale.
  - Nota: se viene rilevata almeno un'ora di assorbimento dei carboidrati durante un giorno, tutti i dati classificati come "UAM" saranno classificati come basali, indipendentemente da questa impostazione (On o Off)
- Numero di giorni di dati (predefinito 5): è possibile definire il valore predefinito con questa impostazione. Each time your select a new profile in Autotune plugin, Tune days parameter will be replaced by this default value
- Applica il risultato medio in IC/ISF circadiano (default Off): vedi [ IC circolare o profilo ISF ](#circadian-ic-or-isf-profile) di seguito.

### Other settings

- Autotune utilizza anche il rapporto di autosenso massimo e il rapporto di autosenso minimo per limitare la variazione. È possibile vedere e regolare questi valori in Config Builder & #062; Sensitivity detection plugin & #062; Impostazioni & #062; Impostazioni avanzate

  ![Schermata predefinita Autotune ](../images/Autotune/Autotune_12.png)



## Funzioni avanzate

(Ic-circadiano-o-profilo-Isf di Autotune) =

### IC Circadiano o profilo ISF

- Se hai un'importante variazione di IC e/o di ISF nel tuo profilo, e ti fidi completamente del tuo tempo e della tua variazione circadiana, allora puoi impostare "Applicare il risultato medio in IC/ISF circadiano"

  - Note that Autotune calculation will always be done with a single value, and circadian variation will not be tuned by Autotune. Questa impostazione applica solo la variazione media calcolata per IC e/o ISF sui valori circadiani

- Guarda nella schermata sotto Profilo aggiornato con Applica variazione media Off (a sinistra) e On (a destra)

  ![Schermata predefinita di Autotune](../images/Autotune/Autotune_13.png)



### Aggiorna uno specifico giorno della settimana

- Se cliccate sulla casella con l'occhio a destra del parametro "Rune days", vedrete la selezione del giorno. È possibile specificare quale giorno della settimana deve essere incluso nel calcolo di Autotune (nella schermata sottostante è possibile vedere un esempio di "giorni lavorativi" con sabato e domenica rimossi dal calcolo automatico)
  - Se il numero di giorni inclusi nel calcolo di Autotune è inferiore al numero di giorni di sintonizzazione, vedrai quanti giorni saranno inclusi a destra del selettore di Tune days (10 giorni nell'esempio sottostante)
  - Questa impostazione dà buoni risultati solo se il numero di giorni rimanenti non è troppo piccolo (ad esempio se si sintonizza un profilo specifico per i giorni di fine settimana con solo la domenica e il sabato selezionati, è necessario selezionare un minimo di 21 o 28 giorni di sintonizzazione per avere 6 o 8 giorni inclusi nel calcolo di Autotune)

![Autotune default screen](../images/Autotune/Autotune_14b.png)

- Durante il calcolo di Autotune, è possibile vedere l'avanzamento dei calcoli ("Risultato parziale giorno 3 / 10 sintonizzato" sull'esempio sotto)

  ![Autotune default screen](../images/Autotune/Autotune_15b.png)



(avvio-autotune-con-una-regola-automatica) =

## Avvio Autotune con una regola automatica

Il primo passo è definire il corretto evento per una regola di automazione con Autotune:

Nota: per ulteriori informazioni su come impostare una regola di automazione, vedere [ qui](../DailyLifeWithAaps/Automations.md).

- È necessario selezionare Ripristinare il tempo di attivazione: eseguire Autotune solo una volta al giorno e l'autotune è progettato per essere eseguito quotidianamente (ogni nuova esecuzione si sposta un giorno dopo e la modifica rapida del profilo dovrebbe essere piccola)

  ![Autotune default screen](../images/Autotune/Autotune_16.png)

- È meglio all'inizio eseguire Autotune durante il giorno per essere in grado di controllare i risultati. If you want to run Autotune during the night, you have to select in the trigger 4AM or later to include current day in next Autotune Calculation.

  ![Autotune default screen](../images/Autotune/Autotune_17.png)

- Then you can select "Run Autotune" Action in the list

  ![Autotune default screen](../images/Autotune/Autotune_18.png)

- You can then select Autotune Action to adjust parameters for your run. Default parameters are "Active Profile", default Tune days value defined in Autotune Plugin preferences, and All days are selected.

  ![Autotune default screen](../images/Autotune/Autotune_19b.png)

- After a few days, if you fully trust Autotune results and percentage of modification is low, you can modify [Autotune settings](#autotune-plugin-settings) "Automation Switch Profile" to enabled to automatically update and activate profile tuned after calculation.

Note: if you want to automatically tune profiles for specific days of the week (for example a profile for "Weekend days" and another one for "Working days"), then create one rule for each profile, select the same days in Trigger and in Autotune Action, Tune days must be high enough to be sure tuning will be done with at least 6 or 8 days, and don't forget to select time after 4AM in trigger...

- See below an example of rule to tune "my profile" on all "Working days" with 14 Tune days selected (so only 10 days included in autotune calculation).

![Autotune default screen](../images/Autotune/Autotune_20b.png)



## Tips and trick's

Autotune works with information existing in your database, so if you just installed AAPS on a new phone, you will have to wait several days before being able to launch Autotune with enough days to get relevant results.

Autotune is just an help, it's important to regularly check if you agree with calculated profile. If you have any doubt, change Autotune settings (for example the number of days) or copy results in local profile and adjust profile before using it.

Always use Autotune several days manually to check results before applying them. And it's only when you fully trust Autotune results, and when variation becomes tiny between previous profile and calculated profile than you start to use Automation (Never before)

- Autotune can work very well for some users and not for others, so **If you don't trust Autotune result, don't use it**

It's also important to analyse Autotune results to understand (or try to understand) why Autotune propose these modifications

- you can have a whole increase or decrease of the strength of your profile (for example increase of total basal associated to decrease of ISF and IC values). it could be associated to several following days with autosens correction above 100% (more agressivity required) or below 100% (you are more sensitive)
- Sometimes Autotune propose a different balance between basal rates and IC/ISF (for ex lower basal and more aggressive IC/ISF)

We advise to not use Autotune in the following cases:

- You don't enter all your carbs
  - If you don't enter carbs correction for an hypoglycemia, Autotune will see an unexpected increase of your BG value and will increase your basal rates the 4 hours earlier, it could be the opposite of what you need to avoid hypo, especially if it's in the middle of the night. That's why it's important to enter all carbs especially correction for hypo.
- You have a lot of period with UAM detected during the day.
  - Do you have entered all your carbs and correctly estimated your Carbs ?
  - All UAM periods (except if you enter no carbs during a day and categorized UAM as basal is disabled), all your UAM periods will be categorized as basal, this can increase a lot your basal (much more than necessary)

- Your carbs absorption is very slow: if most of your carbs absorption are calculated with min_5m_carbimpact parameter (you can see these periods with a little orange dot in the top of COB curve), the calculation of COB could be wrong and leads to wrong results.
  - When you practice sport, you are generally more sensitive and your BG doesn't rise a lot, so during or after an exercise, it's usual to see some periods with slow carbs. But if you have too often unexpected slow carb absorption, then you may need a profile adjustment (higher value of IC) or a min_5m_carbimpact a bit too high.
- You have a "very bad days", for example stuck several hours in hyperglycemia with a huge amount of insulin to be able to go down within the range, or after a sensor change you got long periods of wrong BG values. If during the pas weeks you only have one or 2 "bad days", you can disable manually these days in autotune calculation to exclude them from calculation, and again **check carefully if you can trust the results**
- If the percentage of modification is too important
  - You can try to increase the number of days to get smoother results