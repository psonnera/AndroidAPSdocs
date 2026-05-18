# Come usare il plugin Autotune

La documentazione sull'algoritmo Autotune è disponibile nella [documentazione OpenAPS](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html).

Il plugin Autotune è un'implementazione dell'algoritmo Autotune di OpenAPS all'interno di AAPS.

Il Plugin Autotune è disponibile nelle versioni di AAPS dalla [3.4](#version3400) ma è nascosto per impostazione predefinita.

## Mostrare il plugin Autotune

Crea un file vuoto denominato `enable_autotune` nella sottocartella `extra` della tua [directory AAPS](#preferences-maintenance-settings) sul telefono.

***NOTA: Assicurati di controllare nelle impostazioni di **AAPS** dove si trova la tua Directory AAPS e di aver messo il file in quella corretta; diversi utenti sono stati colti di sorpresa mettendo il file nella cartella sbagliata.***

![Enable Autotune](../images/Autotune/Autotune_0.png)

Autotune verrà quindi visualizzato nel Costruttore di configurazione dopo aver riavviato AAPS.

![Autotune plugin](../images/Autotune/Autotune_1.png)

***NOTA: Se non riesci a vedere l'opzione `Autotune` dovrai fare clic sulla freccia evidenziata (casella rossa) per espandere e mostrare tutte le impostazioni nella sezione `Generale`.***

## Interfaccia utente Autotune

![Autotune default screen](../images/Autotune/Autotune_1b.png)

- Puoi selezionare nel menu a discesa Profilo il profilo di input che vuoi ottimizzare (per impostazione predefinita è selezionato il profilo attivo corrente)
  - Nota: ogni volta che selezioni un nuovo profilo, i risultati precedenti verranno rimossi e il parametro Giorni di ottimizzazione sarà impostato al valore predefinito
- Poi Giorni di ottimizzazione serve per selezionare il numero di giorni usati nel calcolo per ottimizzare il profilo. Il valore minimo è 1 giorno e il valore massimo 30 giorni. Questo numero non dovrebbe essere troppo piccolo per ottenere risultati iterativi e uniformi corretti (più di 7 giorni per ogni calcolo)
  - Nota: ogni volta che cambi il parametro Giorni di ottimizzazione, i risultati precedenti verranno rimossi
- Ultima esecuzione è un link che recupera il tuo ultimo calcolo valido. Se non hai avviato Autotune il giorno corrente, o se i risultati precedenti sono stati rimossi con una modifica del parametro di calcolo sopra, allora puoi recuperare i parametri e i risultati dell'ultima esecuzione riuscita.
- L'avviso mostra ad esempio alcune informazioni sul profilo selezionato (se hai diversi valori IC o diversi valori ISF)
  - Nota: il calcolo Autotune funziona con un solo valore IC e un solo valore ISF. Attualmente non esiste un algoritmo Autotune per ottimizzare un IC circadiano o un ISF circadiano. Se il tuo profilo di input ha diversi valori, puoi vedere nella sezione avvisi il valore medio preso in considerazione per ottimizzare il profilo.
- Il pulsante Controlla Profilo di Input apre il Visualizzatore di Profilo per consentirti una rapida verifica del tuo profilo (Unità, DIA, IC, ISF, basale e target)
  - Nota: Autotune ottimizzerà solo il tuo IC (singolo valore), ISF (singolo valore) e basale (con variazione circadiana). Unità, DIA e target rimarranno invariati nel profilo di output.

- "Esegui Autotune" avvierà il calcolo Autotune con il profilo selezionato e il numero di Giorni di ottimizzazione
  - Nota: il calcolo Autotune può richiedere molto tempo. Una volta avviato, puoi passare a un'altra vista (home, ...) e tornare più tardi nel plugin Autotune per vedere i risultati

  ![Autotune Run start](../images/Autotune/Autotune_2b.png)

- Durante l'esecuzione vedrai i risultati intermedi di seguito

  - Nota: durante l'esecuzione, le impostazioni sono bloccate, quindi non puoi più cambiare il profilo di input selezionato o il numero di giorni. Dovrai aspettare la fine del calcolo corrente se vuoi avviare un'altra esecuzione con altri parametri.

  ![Autotune during run](../images/Autotune/Autotune_3b.png)

- Quando il calcolo Autotune è terminato, vedrai il risultato (Profilo Ottimizzato) e quattro pulsanti in basso.

  ![Autotune Result](../images/Autotune/Autotune_4b.png)

- È importante confrontare sempre il profilo di input (colonna "Profilo"), il profilo di output (colonna "Ottimizzato") e la percentuale di variazione per ogni valore (Colonna "%").
  
- Per le velocità basali, hai anche il numero di "giorni mancanti". Hai giorni mancanti quando Autotune non ha abbastanza dati categorizzati come "Basale" per ottimizzare la velocità basale per quel periodo (ad esempio dopo ogni pasto quando hai assorbimento di carboidrati). Questo numero dovrebbe essere il più basso possibile, specialmente quando la basale è importante (ad esempio durante la notte o alla fine del pomeriggio)
  
- Il pulsante "Confronta profili" apre la vista del comparatore di profili. Il profilo di input è in blu e il profilo di output (denominato "Ottimizzato") è in rosso.

  - Nota: nell'esempio seguente il profilo di input ha variazione circadiana per IC e ISF, ma il profilo calcolato di output ha un singolo valore. Se è importante per te ottenere un profilo di output circadiano vedere [Profilo IC o ISF Circadiano](#autotune-circadian-ic-or-isf-profile) di seguito.

  ![Autotune Compare profiles](../images/Autotune/Autotune_5.png)

- Se ti fidi dei risultati (bassa percentuale di variazione tra profilo di input e profilo di output), puoi fare clic sul pulsante "Attiva profilo" e poi fare clic su OK per convalidare.

  - L'attivazione del Profilo Ottimizzato creerà automaticamente un nuovo profilo "Ottimizzato" nel plugin del Profilo locale.
  - Se hai già un profilo denominato "Ottimizzato" nel plugin del profilo locale, allora questo profilo verrà aggiornato con il profilo Autotune calcolato prima dell'attivazione

  ![Autotune Activate profile](../images/Autotune/Autotune_6.png)

- Se pensi che il Profilo Ottimizzato debba essere aggiustato (ad esempio se pensi che alcune variazioni siano troppo importanti), puoi fare clic sul pulsante "Copia nel profilo locale"
  
  - Verrà creato un nuovo profilo con il prefisso "Ottimizzato" e la data e l'ora dell'esecuzione nel plugin del profilo locale

  ![Autotune Copy to local profile](../images/Autotune/Autotune_7.png)

- Puoi quindi selezionare il profilo locale per modificare il Profilo Ottimizzato (verrà selezionato per impostazione predefinita quando apri il plugin Profilo locale)

  - I valori nel profilo locale verranno arrotondati nell'interfaccia utente alle capacità del microinfusore

  ![Autotune local profile update](../images/Autotune/Autotune_8.png)

- Se vuoi sostituire il tuo profilo di input con il risultato Autotune, fai clic sul pulsante "Aggiorna profilo di input" e convalida il Popup con OK

  - Nota: se fai clic su "Attiva profilo" dopo "Aggiorna profilo di input", attiveresti il profilo aggiornato e non il profilo "Ottimizzato" predefinito?

  ![Autotune Update input profile](../images/Autotune/Autotune_9.png)

- Se hai aggiornato il profilo di input, il pulsante "Aggiorna profilo di input" viene sostituito dal pulsante "Ripristina profilo di input" (vedere screenshot di seguito). In questo modo puoi vedere immediatamente se il tuo profilo di input corrente nel plugin Profilo locale include già il risultato dell'ultima esecuzione o no. Hai anche la possibilità di recuperare il tuo profilo di input senza il risultato autotune con questo pulsante

  ![Autotune Update input profile](../images/Autotune/Autotune_10.png)



## Impostazioni Autotune

(autotune-plugin-settings)=

### Impostazioni del plugin Autotune

  ![Autotune default screen](../images/Autotune/Autotune_11.png)

```{admonition} Solo DEV
:class: info
La funzionalità Cambio Profilo Automatico è disponibile solo in modalità Dev/Engineering.
```

- Cambio Profilo Automatico (predefinito Off): vedere [Esegui Autotune con una regola di automazione](#autotune-run-autotune-with-an-automation-rule) di seguito. Se cambi questa impostazione su On, il profilo di input verrà automaticamente aggiornato dal Profilo Ottimizzato e verrà attivato.
  - **Attenzione, devi fidarti e verificare per diversi giorni successivi, che dopo un aggiornamento e l'attivazione del Profilo Ottimizzato senza modifica, migliori il tuo loop**

- Categorizza UAM come basale (predefinito On): Questa impostazione è per gli utenti che usano AndroidAPS senza carboidrati inseriti (UAM completo). Impedirà (quando Off) di categorizzare UAM come basale.
  - Nota: se hai almeno un'ora di assorbimento di carboidrati rilevata durante un giorno, tutti i dati categorizzati come "UAM" verranno categorizzati come basale, qualunque sia questa impostazione (On o Off)
- Numero di giorni di dati (predefinito 5): Puoi definire il valore predefinito con questa impostazione. Ogni volta che selezioni un nuovo profilo nel plugin Autotune, il parametro Giorni di ottimizzazione verrà sostituito da questo valore predefinito
- Applica risultato medio in IC/ISF circadiano (predefinito Off): vedere [Profilo IC o ISF Circadiano](#autotune-circadian-ic-or-isf-profile) di seguito.

### Altre impostazioni

- Autotune usa anche il rapporto max autosens e il rapporto min autosens per limitare la variazione. Puoi vedere e regolare questi valori in Costruttore di configurazione > Plugin rilevamento sensibilità > Impostazioni > Impostazioni avanzate

  ![Autotune default screen](../images/Autotune/Autotune_12.png)



## Funzionalità avanzata

(autotune-circadian-ic-or-isf-profile)=

### Profilo IC o ISF Circadiano

- Se hai variazioni importanti di IC e/o del tuo ISF nel profilo, e ti fidi completamente del tempo circadiano e della variazione, puoi impostare "Applica risultato medio in IC/ISF circadiano"

  - Nota che il calcolo Autotune verrà sempre eseguito con un singolo valore, e la variazione circadiana non verrà ottimizzata da Autotune. Questa impostazione applica solo la variazione media calcolata per IC e/o ISF sui tuoi valori circadiani

- Vedere nello screenshot seguente il Profilo Ottimizzato con Applica variazione media Off (a sinistra) e On (a destra)

  ![Autotune default screen](../images/Autotune/Autotune_13.png)

  

### Ottimizzare giorni specifici della settimana

- Se fai clic sulla casella di controllo con l'occhio a destra del parametro "Giorni di ottimizzazione", vedrai la selezione del giorno. Puoi specificare quali giorni della settimana dovrebbero essere inclusi nel calcolo Autotune (nello screenshot seguente puoi vedere un esempio per "giorni lavorativi" con Sabato e Domenica rimossi dal calcolo autotune)
  - Se il numero di giorni inclusi nel calcolo Autotune è inferiore al numero di Giorni di ottimizzazione, vedrai quanti giorni verranno inclusi a destra del selettore Giorni di ottimizzazione (10 giorni nell'esempio seguente)
  - Questa impostazione dà buoni risultati solo se il numero di giorni rimanenti non è troppo piccolo (ad esempio se ottimizzi un profilo specifico per i giorni del weekend con solo Domenica e Sabato selezionati, dovresti selezionare un minimo di 21 o 28 Giorni di ottimizzazione per avere 6 o 8 giorni inclusi nel calcolo Autotune)

  ![Autotune default screen](../images/Autotune/Autotune_14b.png)

- Durante il calcolo Autotune, puoi vedere il progresso dei calcoli ("Risultato parziale giorno 3 / 10 ottimizzato" nell'esempio seguente)

  ![Autotune default screen](../images/Autotune/Autotune_15b.png)



(autotune-run-autotune-with-an-automation-rule)=

## Esegui Autotune con una regola di automazione

```{admonition} Solo DEV
:class: info
La funzionalità Cambio Profilo Automatico è disponibile solo in modalità Dev/Engineering.
```

Il primo passo è definire il trigger corretto per una regola di automazione con Autotune:

Nota: per ulteriori informazioni su come impostare una regola di automazione, vedi [qui](../DailyLifeWithAaps/Automations.md).

- Dovresti selezionare il trigger di tempo ricorrente: esegui Autotune solo una volta al giorno, e autotune è progettato per essere eseguito quotidianamente (ogni nuova esecuzione sposti un giorno dopo e rapidamente la modifica del profilo dovrebbe essere minima)

  ![Autotune default screen](../images/Autotune/Autotune_16.png)

- È meglio all'inizio eseguire Autotune durante il giorno per poter controllare i risultati. Se vuoi eseguire Autotune durante la notte, devi selezionare nel trigger le 4:00 o dopo per includere il giorno corrente nel prossimo Calcolo Autotune.

  ![Autotune default screen](../images/Autotune/Autotune_17.png)

- Puoi quindi selezionare l'Azione "Esegui Autotune" nell'elenco

  ![Autotune default screen](../images/Autotune/Autotune_18.png)

- Puoi poi selezionare l'Azione Autotune per regolare i parametri per l'esecuzione. I parametri predefiniti sono "Profilo Attivo", il valore predefinito Giorni di ottimizzazione definito nelle preferenze del Plugin Autotune e tutti i giorni sono selezionati.

  ![Autotune default screen](../images/Autotune/Autotune_19b.png)

- Dopo alcuni giorni, se ti fidi completamente dei risultati Autotune e la percentuale di modifica è bassa, puoi modificare le [impostazioni Autotune](#autotune-plugin-settings) "Cambio Profilo Automatico" su abilitato per aggiornare e attivare automaticamente il profilo ottimizzato dopo il calcolo.

Nota: se vuoi ottimizzare automaticamente i profili per giorni specifici della settimana (ad esempio un profilo per "Giorni del weekend" e un altro per "Giorni lavorativi"), allora crea una regola per ogni profilo, seleziona gli stessi giorni nel Trigger e nell'Azione Autotune, i Giorni di ottimizzazione devono essere abbastanza alti per essere sicuri che l'ottimizzazione venga effettuata con almeno 6 o 8 giorni, e non dimenticare di selezionare l'ora dopo le 4:00 nel trigger...

- Vedere di seguito un esempio di regola per ottimizzare "il mio profilo" in tutti i "Giorni lavorativi" con 14 Giorni di ottimizzazione selezionati (quindi solo 10 giorni inclusi nel calcolo autotune).

  ![Autotune default screen](../images/Autotune/Autotune_20b.png)



## Consigli e trucchi

Autotune funziona con le informazioni presenti nel database, quindi se hai appena installato AAPS su un nuovo telefono, dovrai aspettare diversi giorni prima di poter avviare Autotune con abbastanza giorni per ottenere risultati rilevanti.

Autotune è solo un aiuto, è importante controllare regolarmente se sei d'accordo con il profilo calcolato. In caso di dubbi, cambia le impostazioni Autotune (ad esempio il numero di giorni) o copia i risultati nel profilo locale e aggiusta il profilo prima di usarlo.

Usa sempre Autotune per diversi giorni manualmente per controllare i risultati prima di applicarli. Ed è solo quando ti fidi completamente dei risultati Autotune, e quando la variazione diventa minima tra il profilo precedente e il profilo calcolato che inizi a usare Automation (Mai prima)

- Autotune può funzionare molto bene per alcuni utenti e non per altri, quindi **Se non ti fidi del risultato Autotune, non usarlo**

È anche importante analizzare i risultati Autotune per capire (o cercare di capire) perché Autotune propone queste modifiche

- puoi avere un aumento o una diminuzione complessiva della forza del tuo profilo (ad esempio aumento della basale totale associato a diminuzione dei valori ISF e IC). Potrebbe essere associato a diversi giorni consecutivi con correzione autosens superiore al 100% (richiesta maggiore aggressività) o inferiore al 100% (sei più sensibile)
- A volte Autotune propone un diverso equilibrio tra velocità basali e IC/ISF (ad es. basale inferiore e IC/ISF più aggressivo)

Consigliamo di non usare Autotune nei seguenti casi:

- Non inserisci tutti i tuoi carboidrati
  - Se non inserisci la correzione con carboidrati per l'ipoglicemia, Autotune vedrà un aumento inaspettato del valore BG e aumenterà le velocità basali 4 ore prima, potrebbe essere l'opposto di ciò che hai bisogno per evitare l'ipo, specialmente se è nel mezzo della notte. Ecco perché è importante inserire tutti i carboidrati, specialmente la correzione per l'ipo.
- Hai molti periodi con UAM rilevati durante il giorno.
  - Hai inserito tutti i tuoi carboidrati e correttamente stimato i tuoi Carboidrati?
  - Tutti i periodi UAM (tranne se non inserisci carboidrati durante un giorno e categorizzare UAM come basale è disabilitato), tutti i tuoi periodi UAM verranno categorizzati come basale, il che può aumentare molto la basale (molto più del necessario)

- L'assorbimento dei carboidrati è molto lento: se la maggior parte dell'assorbimento dei carboidrati viene calcolato con il parametro min_5m_carbimpact (puoi vedere questi periodi con un piccolo punto arancione in cima alla curva COB), il calcolo del COB potrebbe essere errato e portare a risultati errati.
  - Quando fai sport, generalmente sei più sensibile e la BG non sale molto, quindi durante o dopo un esercizio è normale vedere alcuni periodi con assorbimento lento dei carboidrati. Ma se hai troppo spesso assorbimento lento inaspettato dei carboidrati, potresti aver bisogno di un aggiustamento del profilo (valore più alto di IC) o di un min_5m_carbimpact un po' troppo alto.
- Hai "giorni molto cattivi", ad esempio bloccato per diverse ore in iperglicemia con una grande quantità di insulina per riuscire a tornare nell'intervallo, o dopo un cambio del sensore hai lunghi periodi di valori BG errati. Se nelle ultime settimane hai solo uno o 2 "giorni cattivi", puoi disabilitare manualmente questi giorni nel calcolo autotune per escluderli dal calcolo, e di nuovo **controlla attentamente se puoi fidarti dei risultati**
- Se la percentuale di modifica è troppo importante
  - Puoi provare ad aumentare il numero di giorni per ottenere risultati più uniformi
