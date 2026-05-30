# Microinfusori Medtronic

Il driver non funziona con nessun modello più recente, compresi tutti i modelli che terminano con G (530G, serie 600 [630G, 640G, 670G], serie 700 [770G, 780G], ecc.).

Le seguenti combinazioni di modello e firmware sono compatibili:

    - 512/712 (qualsiasi versione firmware)
    - 515/715 (qualsiasi versione firmware)
    - 522/722 (qualsiasi versione firmware)
    - 523/723 (firmware 2.4A o inferiore)
    - 554/754 versione EU (firmware 2.6A o inferiore)
    - 554/754 versione Canada (firmware 2.7A o inferiore)

È possibile scoprire come controllare il firmware sui microinfusori su [OpenAPS docs](https://openaps.readthedocs.io/en/latest/docs/Gear%20Up/pump.html#how-to-check-pump-firmware-check-for-absence-of-pc-connect) o [LoopDocs](https://loopkit.github.io/loopdocs/build/step3/#medtronic-pump-firmware).

## Requisiti hardware e software
- **Telefono:** Il driver Medtronic dovrebbe funzionare con qualsiasi telefono Android che supporta le connessioni Bluetooth. **IMPORTANTE: Le implementazioni Bluetooth dei produttori di telefoni possono variare, quindi il comportamento di ogni modello di telefono può variare.  Ad esempio, alcuni telefoni gestiranno diversamente l'abilitazione/disabilitazione del Bluetooth.  Ciò può influenzare l'esperienza utente quando AAPS deve riconnettersi al dispositivo di tipo Rileylink.**
- **Dispositivo compatibile RileyLink:** I telefoni Android non possono comunicare con i microinfusori Medtronic senza un dispositivo separato per gestire le comunicazioni. Questo dispositivo si collegherà al telefono via Bluetooth e al microinfusore tramite una connessione radio compatibile.  Il primo di questi dispositivi si chiamava Rileylink, ma ora sono disponibili diverse altre opzioni che possono offrire funzionalità aggiuntive.

    - Rileylink disponibile su [getrileylink.org](https://getrileylink.org/product/rileylink916)
    - Orangelink disponibile su [getrileylink.org](https://getrileylink.org/product/orangelink)
    - Emalink (più opzioni di modello) disponibile su [github.com](https://github.com/sks01/EmaLink)
    - Gnarl (richiede alcune operazioni DIY aggiuntive) dettagli disponibili su [github.com](https://github.com/ecc1/gnarl)

Un grafico comparativo per i vari dispositivi compatibili con Rileylink è disponibile su [getrileylink.org](https://getrileylink.org/rileylink-compatible-hardware-comparison-chart)

(MedtronicPump-configuration-of-the-pump)=
## Configuration of the pump
Le seguenti impostazioni devono essere configurate sul microinfusore affinché AAPS possa inviare comandi da remoto.  I passaggi necessari per apportare ogni modifica su un Medtronic 715 sono mostrati tra parentesi per ogni impostazione.  I passaggi esatti possono variare in base al tipo di microinfusore e/o alla versione del firmware.

- **Abilitare la modalità remota sul microinfusore** (Sul microinfusore premere Act e andare a Utilità -> Opzioni remote, selezionare On, e nella schermata successiva fare Aggiungi ID e aggiungere qualsiasi ID casuale come ad esempio 111111). Almeno un ID deve essere nell'elenco degli ID remoti affinché il microinfusore si aspetti comunicazioni remote.
- **Impostare la basale massima** (Sul microinfusore premere Act e andare a Basale e poi selezionare Velocità basale massima). Ad esempio, impostare questo valore a quattro volte la velocità basale standard massima consentirebbe una basale temporanea al 400%. Il valore massimo consentito dal microinfusore è 34,9 unità all'ora.
- **Impostare il bolo massimo** (Sul microinfusore premere Act e andare a Bolo e poi selezionare Bolo massimo). Questo è il bolo più grande che il microinfusore accetterà.  Il valore massimo consentito dal microinfusore è 25.
- **Impostare il profilo su Standard**. (Sul microinfusore premere Act e andare a Basale e poi Seleziona schemi) Il microinfusore avrà bisogno di un solo profilo poiché AAPS gestirà i diversi profili sul telefono.  Non sono richiesti altri schemi.
- **Impostare il tipo di basale temporanea** (Sul microinfusore premere Act e andare a Basale e poi Tipo basale temp).  Selezionare Assoluta (non Percentuale).

## Configurazione Medtronic di Telefono/AAPS
- **Non associare il dispositivo compatibile RileyLink tramite il menu Bluetooth del telefono.** L'associazione tramite il menu Bluetooth del telefono impedirà ad AAPS di vedere il dispositivo compatibile con Rileylink quando si seguono le istruzioni sottostanti.
- Disabilitare la rotazione automatica dello schermo sul telefono.  Su alcuni dispositivi la rotazione automatica dello schermo causa il riavvio delle sessioni Bluetooth, il che causerebbe problemi al microinfusore Medtronic.
- Ci sono due modi per configurare il microinfusore Medtronic in AAPS:
1. Utilizzando la procedura guidata di configurazione come parte di una nuova installazione
2. Selezionando l'icona dell'ingranaggio accanto alla selezione Medtronic nell'opzione di selezione del microinfusore nel Costruttore di configurazione

Quando si configura il microinfusore Medtronic con la procedura guidata di configurazione è possibile che non si riesca a completare la configurazione a causa di problemi Bluetooth (ad es. non è possibile connettersi con successo al microinfusore).  Se ciò dovesse accadere, si dovrebbe selezionare l'opzione microinfusore virtuale per completare la configurazione e consentire ulteriori procedure di risoluzione dei problemi utilizzando l'opzione 2.

![Medtronic Settings](../images/Medtronic01a.png)

Durante la configurazione di AAPS per lavorare con il microinfusore Medtronic è necessario impostare i seguenti elementi: (vedere l'immagine sopra)
- **Numero seriale microinfusore**: Visualizzato sul retro del microinfusore e inizia con SN. Inserire solo i 6 numeri mostrati senza caratteri alfabetici (ad es. 123456).
- **Tipo microinfusore**: Il modello del microinfusore in uso (ad es. 522).
- **Frequenza microinfusore**: Ci sono due opzioni in base a dove il microinfusore è stato originariamente distribuito.  Controllare le [FAQ](#MedtronicPump-faq) in caso di dubbio su quale opzione selezionare):
    - per USA e Canada, la frequenza utilizzata è 916 MHz
    - per tutto il mondo, la frequenza utilizzata è 868 MHz
- **Basale massima sul microinfusore (U/h)**: Deve corrispondere all'impostazione configurata sul microinfusore (vedere Configurazione del microinfusore sopra).  Anche questa impostazione deve essere selezionata con attenzione poiché determinerà quanto AAPS può erogare tramite la basale.  Questo imposterà efficacemente la velocità massima della basale temporanea.  Ad esempio, impostare questo valore a quattro volte la velocità basale standard massima consentirebbe una basale temporanea al 400%. Il valore massimo consentito dal microinfusore è 34,9 unità all'ora.
- **Bolo massimo sul microinfusore (U)** (in un'ora): Deve corrispondere all'impostazione configurata sul microinfusore (vedere Configurazione del microinfusore sopra).  Questa impostazione deve essere considerata attentamente poiché determina quanto grande può essere il bolo che AAPS può impostare.
- **Ritardo prima dell'inizio del bolo (s)**: Il numero di secondi dopo l'emissione di un bolo prima che il comando venga effettivamente inviato al microinfusore.  Questo periodo di tempo consente all'utente di annullare il bolo nel caso in cui un comando di bolo venga inviato per errore.  Non è possibile annullare un bolo già iniziato tramite AAPS.  L'unico modo per annullare un bolo già iniziato è sospendere manualmente il microinfusore e poi riprenderlo.
- **Codifica Medtronic**: Determina se viene eseguita la codifica Medtronic.  Si preferisce selezionare la codifica Hardware (cioè eseguita dal dispositivo compatibile Rileylink) in quanto ciò comporta l'invio di meno dati.  La selezione della codifica Software (cioè eseguita da AAPS) può essere utile in caso di frequenti disconnessioni. Questa impostazione verrà ignorata se si ha la versione firmware 0.x sui dispositivi Rileylink.
- **Tipo di batteria (Power View)**: Per determinare correttamente il livello di carica residua della batteria, selezionare il tipo di batteria AAA in uso. Quando si seleziona un valore diverso dalla visualizzazione semplice, AAPS mostrerà il livello percentuale della batteria calcolato e i volt rimanenti. Sono disponibili le seguenti opzioni:

    - Non selezionato (Visualizzazione semplice)
    - Alcalina (Visualizzazione estesa)
    - Litio (Visualizzazione estesa)
    - NiZn (Visualizzazione estesa)
    - NiMH (Visualizzazione estesa)

- **Debug bolo/trattamenti**: Selezionare On o Off in base alle esigenze.
- **Configurazione RileyLink**: Questa opzione consente di trovare e associare il dispositivo compatibile Rileylink.  Selezionando questa opzione verranno mostrati tutti i dispositivi compatibili con Rileylink nelle vicinanze e l'intensità del segnale.
- **Usa scansione**: Attiva la scansione Bluetooth prima della connessione con i dispositivi compatibili Rileylink.  Questo dovrebbe migliorare l'affidabilità della connessione al dispositivo.
- **Mostra il livello della batteria riportato da OrangeLink/EmaLink/DiaLink**: Questa funzione è supportata solo sui dispositivi link più recenti come EmaLink o OrangeLink. I valori verranno mostrati nella scheda Medtronic in AAPS.
- **Imposta basali temp neutre**: Per impostazione predefinita, i microinfusori Medtronic emettono un segnale acustico ogni ora quando è attiva una basale temporanea.  L'abilitazione di questa opzione può aiutare a ridurre il numero di segnali acustici interrompendo una basale temporanea al cambio dell'ora per sopprimere il segnale.

## Scheda MEDTRONIC (MDT)
![MDT Tab](../images/Medtronic02.png) Quando AAPS è configurato per utilizzare un microinfusore Medtronic, verrà mostrata una scheda MDT nell'elenco delle schede in cima allo schermo.  Questa scheda mostra le informazioni sullo stato corrente del microinfusore insieme ad alcune azioni specifiche di Medtronic.
- **Stato RileyLink**: Lo stato corrente della connessione tra il telefono e il dispositivo compatibile Rileylink.  Dovrebbe mostrare sempre Connesso. Qualsiasi altro stato potrebbe richiedere l'intervento dell'utente.
- **Batteria RileyLink**: Il livello attuale della batteria del dispositivo EmaLink o OrangeLink.  Dipende dalla selezione di "Mostra il livello della batteria riportato dal dispositivo OrangeLink/EmaLink/DiaLink" nel menu di configurazione del microinfusore Medtronic.
- **Stato microinfusore**: Lo stato corrente della connessione del microinfusore.  Poiché il microinfusore non sarà costantemente connesso, mostrerà principalmente l'icona di sospensione.  Ci sono altri possibili stati tra cui "In avvio" quando AAPS sta cercando di inviare un comando o altri possibili comandi al microinfusore come "Ottieni ora", "Imposta TBR", ecc.
- **Batteria**: Mostra lo stato della batteria in base al valore scelto per Tipo di batteria (Power View) nel menu di configurazione del microinfusore Medtronic.
- **Ultima connessione**: Da quanto tempo è avvenuta l'ultima connessione riuscita al microinfusore.
- **Ultimo bolo**: Da quanto tempo è stato erogato l'ultimo bolo riuscito.
- **Velocità basale base**: Questa è la velocità basale base che viene eseguita sul microinfusore in questa ora nel profilo attivo.
- **Basale temp**: Basale temp attualmente erogata che può essere 0 unità all'ora.
- **Serbatoio**: Quanta insulina è nel serbatoio (aggiornata almeno ogni ora).
- **Errori**: Stringa di errore se c'è un problema (mostra principalmente se c'è un errore nella configurazione).

In fondo allo schermo ci sono tre pulsanti:
- **Aggiorna**: Per aggiornare lo stato corrente del microinfusore. Dovrebbe essere usato solo se la connessione è stata persa per un periodo prolungato poiché richiederà un aggiornamento completo dei dati (recupero cronologia, ottieni/imposta ora, ottieni profilo, ottieni stato batteria, ecc.).
- **Cronologia microinfusore**: Mostra la cronologia del microinfusore (vedere [sotto](#MedtronicPump-pump-history))
- **Statistiche RL**: Mostra le statistiche RL (vedere [sotto](#MedtronicPump-rl-status-rileylink-status))

(MedtronicPump-pump-history)=
## Pump History
![Pump History Dialog](../images/Medtronic03.png)

La cronologia del microinfusore viene recuperata ogni 5 minuti e memorizzata localmente. Vengono memorizzate solo le ultime 24 ore di cronologia.  Ciò consente un modo conveniente per vedere il comportamento del microinfusore se necessario.  Vengono memorizzati solo gli elementi rilevanti per AAPS e non includerà una funzione di configurazione che non ha rilevanza.

(MedtronicPump-rl-status-rileylink-status)=
## Stato RL (Stato RileyLink)
![RileyLink Status - Settings](../images/Medtronic04.png) ![RileyLink Status - History](../images/Medtronic05.png)


La finestra di dialogo Stato RL ha due schede:
- **Impostazioni**: Mostra le impostazioni del dispositivo compatibile RileyLink: Indirizzo configurato, Dispositivo connesso, Stato connessione, Errore di connessione e versioni firmware RileyLink. Il tipo di dispositivo è sempre Microinfusore Medtronic, il Modello sarà il proprio modello, il Numero seriale è il numero seriale configurato, la Frequenza microinfusore mostra quale frequenza si usa, Ultima frequenza è l'ultima frequenza usata.
- **Cronologia**: Mostra la cronologia delle comunicazioni, le voci con RileyLink mostrano i cambiamenti di stato per RileyLink e Medtronic mostra quali comandi sono stati inviati al microinfusore.

## Azioni
Quando viene utilizzato il driver Medtronic, vengono aggiunte due azioni aggiuntive alla scheda Azioni:
- **Attiva e sintonizza**: Nel caso in cui AAPS non si sia connesso al microinfusore per un periodo prolungato (dovrebbe connettersi ogni 5 minuti), è possibile forzare una sintonizzazione. Questo tenterà di contattare il microinfusore cercando tutte le possibili frequenze radio utilizzate dal microinfusore. In caso di connessione riuscita, la frequenza riuscita verrà impostata come predefinita.
- **Reimposta configurazione RileyLink**: Se si reimposta il dispositivo compatibile RileyLink potrebbe essere necessario utilizzare questa azione in modo che il dispositivo possa essere riconfigurato (frequenza impostata, tipo di frequenza impostato, codifica configurata).


## Note importanti

### Necessaria attenzione speciale nella configurazione NS
AAPS utilizza il numero seriale per la sincronizzazione e il numero seriale è esposto a NS. Poiché la conoscenza del numero seriale di un vecchio microinfusore Medtronic può essere utilizzata per controllare il microinfusore da remoto, prestare particolare attenzione nel proteggere il sito NS per prevenire la divulgazione del numero seriale del microinfusore. Vedere https://nightscout.github.io/nightscout/security/

### Utenti OpenAPS
Gli utenti OpenAPS devono notare che AAPS con Medtronic utilizza un approccio completamente diverso da OpenAPS.  Usando AAPS, il metodo principale di interazione con il microinfusore avviene tramite il telefono.  Nei casi d'uso normali è probabile che l'unica volta che sia necessario usare il menu del microinfusore sia quando si cambiano i serbatoi.  Questo è molto diverso dall'utilizzo di OpenAPS dove almeno parte di un bolo viene solitamente erogata tramite i pulsanti di bolo rapido.  Nel caso in cui il microinfusore venga utilizzato per erogare manualmente un bolo, possono verificarsi problemi se AAPS tenta di erogarne uno contemporaneamente.  Ci sono controlli per cercare di prevenire problemi in tali casi, ma questo dovrebbe comunque essere evitato quando possibile.

### Logging
Nel caso in cui sia necessario risolvere i problemi del microinfusore Medtronic, selezionare l'icona del menu nell'angolo in alto a sinistra dello schermo, selezionare Manutenzione e Impostazioni di registrazione. Per la risoluzione dei problemi Medtronic, è necessario selezionare Microinfusore, PumpComm, PumpBTComm. For troubleshooting any Medtronic issues Pump, PumpComm, PumpBTComm should be checked.

### Medtronic CGM
Il CGM Medtronic NON è attualmente supportato.

### Manual use of pump
Evitare di effettuare boli manualmente o di impostare TBR sul microinfusore. Tutti questi comandi devono essere inviati tramite AAPS.  Nel caso vengano utilizzati comandi manuali, deve esserci un ritardo di almeno 3 minuti tra di essi per ridurre il rischio di problemi.

### Cambiamenti di fuso orario e ora legale (DST) o viaggi con microinfusore Medtronic e AAPS

AAPS rileverà automaticamente i cambiamenti di fuso orario e aggiornerà l'ora del microinfusore quando il telefono passa al nuovo orario.

Viaggiare verso est significa aggiungere ore all'ora corrente (ad es. da GMT+0 a GMT+2) e non causerà problemi poiché non ci saranno sovrapposizioni (ad es. non sarà possibile avere la stessa ora due volte).  Viaggiare verso ovest, tuttavia, può causare problemi poiché si torna effettivamente indietro nel tempo, il che può causare dati IOB errati.

I problemi riscontrati quando si viaggia verso ovest sono noti agli sviluppatori e il lavoro su una possibile soluzione è in corso.  Vedere https://github.com/andyrozman/RileyLinkAAPS/issues/145 per maggiori dettagli.  Per ora, si prega di essere consapevoli che questo problema potrebbe verificarsi e monitorare attentamente quando si cambiano i fusi orari.

### GNARL è un dispositivo completamente compatibile con Rileylink?

Il codice GNARL supporta completamente tutte le funzioni utilizzate dal driver Medtronic in AAPS, il che significa che è completamente compatibile.  È importante notare che ciò richiederà lavoro aggiuntivo in quanto sarà necessario procurarsi hardware compatibile e poi caricare il codice GNARL sul dispositivo.

**Nota dell'autore:** Si noti che il software GNARL è ancora sperimentale e poco testato, e non dovrebbe essere considerato sicuro da usare come un RileyLink.

(MedtronicPump-faq)=
## FAQ

(MedtronicPump-what-to-do-if-i-loose-connection-to-rileylink-and-or-pump)=
### Cosa fare se si perde la connessione a RileyLink e/o al microinfusore?
Ci sono diverse opzioni da provare per risolvere i problemi di connettività.
- Utilizzare il pulsante "Attiva e sintonizza" nella scheda ACT come descritto sopra.
- Disabilitare il Bluetooth sul telefono, attendere 10 secondi e poi riabilitarlo. Questo forzerà il dispositivo Rileylink a riconnettersi al telefono.
- Reimpostare il dispositivo Rileylink.  È quindi necessario utilizzare il pulsante "Reimposta configurazione Rileylink" nella scheda ACT.
- Altri utenti hanno trovato efficaci i seguenti passaggi per ripristinare la connettività quando altri metodi non hanno funzionato:
    1. Riavviare il telefono
    2. *Mentre* il telefono si riavvia, riavviare il dispositivo Rileylink
    3. Aprire AAPS e consentire il ripristino della connessione


### Come determinare quale frequenza utilizza il microinfusore
![Pump Model](../images/Medtronic06.png)

Sul retro del microinfusore si troverà una riga che riporta il numero del modello insieme a un codice speciale di 3 lettere. Le prime due lettere determinano il tipo di frequenza e l'ultima determina il colore. Ecco i possibili valori per la frequenza:
- NA - Nord America (nella selezione della frequenza è necessario selezionare "US & Canada (916 MHz)")
- CA - Canada (nella selezione della frequenza è necessario selezionare "US & Canada (916 MHz)")
- WW - Worldwide (nella selezione della frequenza è necessario selezionare "Worldwide (868 Mhz)")

