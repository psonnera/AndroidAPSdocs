# Accu-Chek Insight

**Questo software è parte di una soluzione fai-da-te per pancreas artificiale e non è un prodotto finito, ma richiede che sia TU a leggere, imparare e comprendere il sistema, incluso come utilizzarlo. Non è qualcosa che gestisce tutta la tua terapia del diabete al posto tuo, ma ti permette di migliorare il tuo diabete e la tua qualità di vita se sei disposto a dedicarvi il tempo necessario. Non affrettarti, ma concediti il tempo di imparare. Sei tu solo il responsabile di ciò che ne fai.**

---
***AVVISO:** Se in passato hai utilizzato Insight con **SightRemote**, aggiorna alla **versione più recente di AAPS** e **disinstalla SightRemote**.*
---


## Requisiti hardware e software

* Un microinfusore Roche Accu-Chek Insight (qualsiasi firmware, tutti funzionano)

Nota: AAPS scriverà i dati sempre nel **primo profilo di velocità basale del microinfusore**.
* Uno smartphone Android (praticamente qualsiasi versione Android funziona con Insight, ma controlla la pagina [Componenti](../Getting-Started/ComponentOverview) per sapere quale versione Android è necessaria per eseguire AAPS.)
* L'app AAPS installata sul telefono

## Configurazione

* Il microinfusore Insight deve essere connesso a un solo dispositivo alla volta. Se in precedenza hai usato il telecomando Insight (glucometro), devi rimuovere il glucometro dall'elenco dei dispositivi associati al microinfusore: Menu > Impostazioni > Comunicazione > Rimuovi dispositivo

   ![Screenshot of Remove Meter Insight](../images/Insight_RemoveMeter.png)

* In [Costruttore di configurazione > Microinfusore](../SettingUpAaps/ConfigBuilder.md), selezionare Accu-Chek Insight.

   ![Screenshot of Config Builder Insight](../images/Insight_ConfigBuilder_AAPS3_0.jpg)

* Toccare l'ingranaggio per aprire le impostazioni Insight.
* Nelle impostazioni, toccare il pulsante 'Associazione Insight' nella parte superiore dello schermo. Verrà visualizzato un elenco di tutti i dispositivi Bluetooth nelle vicinanze (in basso a sinistra).
* Sul microinfusore Insight, andare a Menu > Impostazioni > Comunicazione > Aggiungi dispositivo. Il microinfusore visualizzerà la schermata seguente (in basso a destra) con il numero di serie del microinfusore.

   ![Screenshot of Insight Pairing 1](../images/Insight_Pairing1.png)

* Tornando al telefono, toccare il numero di serie del microinfusore nell'elenco dei dispositivi Bluetooth. Poi toccare Associa per confermare.

   ![Screenshot of Insight Pairing 2](../images/Insight_Pairing2.png)

* Sia il microinfusore che il telefono visualizzeranno un codice. Verificare che i codici siano uguali su entrambi i dispositivi e confermare sia sul microinfusore che sul telefono.

   ![Screenshot of Insight Pairing 3](../images/Insight_Pairing3.png)

* Fatto! Complimenti per aver associato correttamente il microinfusore con AAPS.

   ![Screenshot of Insight Pairing 4](../images/Insight_Pairing4.png)

* Per verificare che tutto funzioni, tornare al Costruttore di configurazione in AAPS e toccare l'ingranaggio accanto al Microinfusore Insight per accedere alle impostazioni Insight, quindi toccare Associazione Insight e vedrai alcune informazioni sul microinfusore:

   ![Screenshot of Insight Pairing Information](../images/Insight_PairingInformation.png)

Nota: Non ci sarà una connessione permanente tra il microinfusore e il telefono. La connessione verrà stabilita solo quando necessario (ad es. per impostare una basale temporanea, erogare un bolo, leggere la cronologia del microinfusore...). Altrimenti la batteria del telefono e del microinfusore si scaricherebbe troppo rapidamente.

(Accu-Chek-Insight-Pump-settings-in-aaps)=
## Impostazioni in AAPS
**Nota: Ora è possibile (solo con AAPS v2.7.0 e versioni successive) usare 'Usa sempre valori basali assoluti' se si vuole usare Autotune con il microinfusore Insight, anche se 'la sincronizzazione è abilitata' con Nightscout.** (In AAPS vai a [Preferenze > NSClient > Impostazioni avanzate](#Preferences-advanced-settings-nsclient)).

   ![Screenshot of Insight Settings](../images/Insight_settings.png)

Nelle impostazioni Insight in AAPS è possibile abilitare le seguenti opzioni:
* "Registra cambio serbatoio": Registra automaticamente un cambio cartuccia insulina quando si esegue il programma "riempimento cannula" sul microinfusore.

* "Registra cambio tubo": Aggiunge una nota nel database AAPS quando si esegue il programma "riempimento tubo" sul microinfusore.

* "Registra cambio sito": Aggiunge una nota nel database AAPS quando si esegue il programma "riempimento cannula" sul microinfusore. **Nota: Un cambio sito reimposta anche Autosens.**

* "Registra cambio batteria": Registra un cambio batteria quando si inserisce una nuova batteria nel microinfusore.

* "Registra cambi modalità operativa": Inserisce una nota nel database AAPS ogni volta che si avvia, si ferma o si mette in pausa il microinfusore.

* "Registra avvisi": Registra una nota nel database AAPS ogni volta che il microinfusore emette un avviso (eccetto promemoria, bolo e annullamento TBR - questi non vengono registrati).

* "Abilita emulazione TBR": Il microinfusore Insight può erogare basali temporanee (TBR) solo fino al 250%. Per aggirare questa limitazione, l'emulazione TBR ordinerà al microinfusore di erogare un bolo esteso per l'insulina aggiuntiva se si richiede una TBR superiore al 250%.

  **Nota: Usare un solo bolo esteso alla volta, poiché più boli estesi contemporaneamente potrebbero causare errori.**

* "Disabilita vibrazioni durante erogazione bolo manuale": Disabilita le vibrazioni del microinfusore Insight durante l'erogazione di un bolo manuale (o esteso). Questa impostazione è disponibile solo con l'ultima versione del firmware Insight (3.x).

* "Disabilita vibrazioni durante erogazione bolo automatico": Disabilita le vibrazioni del microinfusore Insight durante l'erogazione di un bolo automatico (SMB o basale temporanea con emulazione TBR). Questa impostazione è disponibile solo con l'ultima versione del firmware Insight (3.x).

* "Durata recupero": Definisce per quanto tempo AAPS attenderà prima di riprovare dopo un tentativo di connessione fallito. È possibile scegliere da 0 a 20 secondi. In caso di problemi di connessione, scegliere un tempo di attesa più lungo. <br><br>Example for min. recovery duration = 5 and max. recovery duration = 20 <br><br>no connection -> wait <b>5</b> sec. <br>  retry -> no connection -> wait <b>6</b> sec. <br>  retry -> no connection -> wait <b>7</b> sec. <br>  retry -> no connection -> wait <b>8</b> sec. <br>... <br>  riprova -> nessuna connessione -> attendi <b>8</b> sec. <br>... <br>riprova -> nessuna connessione -> attendi <b>20</b> sec.

* "Ritardo disconnessione": Definisce per quanto tempo (in secondi) AAPS attenderà prima di disconnettersi dal microinfusore al termine di un'operazione. Il valore predefinito è 5 secondi.

For periods when pump was stopped AAPS will log a temp. di 0%.

In AAPS, la scheda Accu-Chek Insight mostra lo stato attuale del microinfusore e ha due pulsanti:
* "Aggiorna": Aggiorna lo stato del microinfusore
* "Abilita/Disabilita TBR tramite notifica": Un microinfusore Insight standard emette un allarme quando una TBR è terminata. Questo pulsante consente di abilitare o disabilitare questo allarme senza bisogno di software di configurazione.

   ![Screenshot of Insight Status](../images/Insight_Status2.png)

## Impostazioni nel microinfusore

Configurare gli allarmi nel microinfusore come segue:
* Menu > Impostazioni > Impostazioni dispositivo > Impostazioni modalità > Silenzioso > Segnale > Suono
* Menu > Impostazioni > Impostazioni dispositivo > Impostazioni modalità > Silenzioso > Volume > 0 (rimuovere tutte le barre)
* Menu > Modalità > Modalità segnale > Silenzioso

Questo disattiverà tutti gli allarmi del microinfusore, consentendo ad AAPS di decidere se un allarme è rilevante. Se AAPS non conferma un allarme, il volume aumenterà (prima un segnale acustico, poi una vibrazione).

(Accu-Chek-Insight-Pump-vibration)=
### Vibrazione

A seconda della versione del firmware del microinfusore, l'Insight vibrerà brevemente ogni volta che viene erogato un bolo (ad esempio, quando AAPS emette un SMB o l'emulazione TBR eroga un bolo esteso).

* Firmware 1.x: Nessuna vibrazione per design.
* Firmware 2.x: La vibrazione non può essere disabilitata.
* Firmware 3.x: AAPS eroga il bolo silenziosamente. (versione minima [2.6.1.4](#Releasenotes-version-2-6-1-4))

La versione del firmware si trova nel menu.

## Sostituzione della batteria

La durata della batteria per Insight in modalità loop varia da 10 a 14 giorni, con un massimo di 20 giorni. L'utente che riporta questo dato usa batterie al litio Energizer.

Il microinfusore Insight ha una piccola batteria interna per mantenere le funzioni essenziali come l'orologio durante la sostituzione della batteria rimovibile. Se la sostituzione della batteria richiede troppo tempo, questa batteria interna potrebbe esaurirsi, l'orologio si azzererà e verrà chiesto di inserire una nuova data e ora dopo aver inserito la nuova batteria. In questo caso, tutte le voci in AAPS precedenti al cambio batteria non verranno più incluse nei calcoli poiché l'ora corretta non può essere identificata correttamente.

(Accu-Chek-Insight-Pump-insight-specific-errors)=
## Errori specifici di Insight

### Bolo esteso

Usare un solo bolo esteso alla volta, poiché più boli estesi contemporaneamente potrebbero causare errori.

### Timeout

A volte può succedere che il microinfusore Insight non risponda durante la configurazione della connessione. In questo caso AAPS visualizzerà il seguente messaggio: "Timeout durante l'handshake - resetta Bluetooth".

![Insight Reset Bluetooth](../images/Insight_ResetBT.png)

In questo caso spegnere il Bluetooth sia sul microinfusore che sullo smartphone per circa 10 secondi e poi riaccenderlo.

## Fuso orario con Insight

Per informazioni sui viaggi attraverso i fusi orari vedere la sezione [Viaggi con cambi di fuso orario con i microinfusori](#timezone-traveling-insight).

