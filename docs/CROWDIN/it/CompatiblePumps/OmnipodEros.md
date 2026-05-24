# Documentazione del driver AAPS per il microinfusore Omnipod

Queste istruzioni riguardano la configurazione del microinfusore Omnipod Eros (**NON Omnipod Dash**). Il driver per Omnipod è disponibile all'interno di AAPS (AAPS) a partire dalla versione 2.8.

**Questo software fa parte di una tecnologia di pancreas artificiale fai-da-te e non è un prodotto, ma richiede che TU legga, impari e comprenda il sistema, compreso il suo utilizzo. Tu solo sei responsabile dell'uso che ne farai.**

```{contents}
:backlinks: entry
:depth: 2
```

## Requisiti hardware e software

- **Dispositivo di comunicazione con il Pod**

> Elemento che consente la comunicazione tra il telefono con AAPS e i Pod della serie Eros.
> 
> > - ![OrangeLink](../images/omnipod/OrangeLink.png)  [Sito di OrangeLink](https://getrileylink.org/product/orangelink)
> > - ![RileyLink](../images/omnipod/RileyLink.png) [RileyLink 433MHz](https://getrileylink.org/product/rileylink433)
> > - ![EmaLink](../images/omnipod/EmaLink.png)  [Sito di Emalink](https://github.com/sks01/EmaLink) - [Info di contatto](mailto:getemalink@gmail.com)
> > - ![DiaLink](../images/omnipod/DiaLink.png)  DiaLink - [Info di contatto](mailto:Boshetyn@ukr.net)
> > - ![LoopLink](../images/omnipod/LoopLink.png)  [Sito di LoopLink](https://www.getlooplink.org/) - [Info di contatto](https://jameswedding.substack.com/) - Non testato

- ![Telefono_Android](../images/omnipod/Android_phone.png)  **Telefono cellulare**

> Elemento che fa funzionare AAPS e invia comandi al dispositivo di comunicazione con il Pod.
> 
> > - [Telefono Android con il driver per Omnipod](#Phones-list-of-tested-phones) compatibile, con la versione di AAPS 2.8 o superiore e i relativi componenti configurati.

- ![Pod_Omnipod](../images/omnipod/Omnipod_Pod.png)  **Dispositivo per la somministrazione di insulina**

> Elemento che interpreta i comandi ricevuti dal dispositivo di comunicazione con il Pod, provenienti dal telefono con AAPS.
> 
> > - Un nuovo pod Omnipod (serie Eros - **NON DASH**)

Queste istruzioni presuppongono che tu stia avviando una nuova sessione pod; se così non fosse, aspetta di iniziare questo processo al prossimo cambio pod.

## Prima di iniziare

**LA SICUREZZA PRIMA DI TUTTO** - non tentare di svolgere questa procedura in un contesto in cui non sia possibile rimediare a un errore (sono indispensabili altri pod, insulina, RileyLink carico e altri telefoni).

**Il PDM Omnipod non funzionerà più dopo l'attivazione del pod da parte del driver Omnipod di AAPS**. Finora utilizzavi il PDM Omnipod per inviare comandi al tuo pod Omnipod Eros. Un pod Omnipod Eros consente la comunicazione con un solo dispositivo. Il dispositivo che attiva con successo il pod è l'unico con cui può comunicare da quel momento in poi. Questo significa che una volta attivato un pod Omnipod Eros con il RileyLink tramite il driver Omnipod di AAPS, **non sarà più possibile utilizzare il PDM con quel pod**. Il driver Omnipod di AAPS con il RileyLink è ora di fatto il tuo PDM. *Questo NON significa che devi buttare via il tuo PDM, bensì è consigliabile tenerlo come backup, e per le emergenze nel caso in cui AAPS non funzioni correttamente.*

**Puoi configurare più RileyLink, ma solo il RileyLink selezionato può comunicare con un pod.** Il driver AAPS Omnipod permette di aggiungere più RileyLink nella configurazione RileyLink, ma solo un RileyLink alla volta può essere selezionato per l'invio e la ricezione di comunicazioni.

**Il pod non si arresta quando il RileyLink è irraggiungibile.** Quando il RileyLink è fuori portata o il segnale è bloccato dalla comunicazione con il pod attivo, il pod continuerà a erogare insulina basale. Quando si attiva un pod, il profilo basale definito in AAPS viene impostato nel nuovo pod. Se perdi la connessione con il pod, il pod tornerà a questo profilo basale. Non potrai inviare nuovi comandi finché il RileyLink non tornerà raggiungibile e ristabilirà la connessione.

**I profili con basali che iniziano o finiscono a metà di un'ora NON sono supportati da AAPS.** Se sei un nuovo utente di AAPS e stai impostando il tuo profilo basale per la prima volta, tieni presente che le frequenze basali che iniziano alla metà di un'ora non sono supportate e dovrai adattareil tuo profilo basale in modo che parta a inizio ora. Ad esempio, se hai una velocità basale di 1,1 unità che inizia alle 09:30 e ha una durata di 2 ore terminando alle 11:30, non è supportata.  Dovrai aggiornare la velocità basale di 1,1 unità su un intervallo di tempo che va dalle 9:00 alle 11:00 o dalle 10:00 alle 12:00.  Anche se gli incrementi di 30 minuti del profilo della velocità basale sono supportati dallo stesso hardware dell'Omnipod, AAPS non è attualmente in grado di tenerne conto con i suoi algoritmi.

## Attivazione del driver Omnipod in AAPS

Puoi abilitare il driver Omnipod in AAPS in **due modi**:

### Opzione 1: la configurazione guidata

Dopo l'installazione di una nuova versione di AAPS, la **configurazione guidata** si avvia automaticamente.  Questo avviene anche durante gli aggiornamenti.  Se hai già esportato le tue impostazioni da un'installazione precedente, puoi uscire dalla configurazione guidata e importare le tue vecchie impostazioni.  Per le nuove installazioni, procedere come indicato di seguito.

Procedi con la **configurazione guidata di AAPS (2)**, che si trova nel **menu a tre puntini (1)** in alto a destra e prosegui attraverso i menu della configurazione guidata fino alla schermata **Micro**. Poi seleziona la voce **Omnipod (3)**.

> ![Attiva_Driver_Omnipod_1](../images/omnipod/Enable_Omnipod_Driver_1.png)  ![Attiva_Driver_Omnipod_2](../images/omnipod/Enable_Omnipod_Driver_2.png)

Nella stessa schermata, sotto la selezione del microinfusore, sono presenti le **impostazioni del driver Omnipod**, sotto la voce **Configurazione RileyLink** aggiungi il dispositivo RileyLink premendo il testo **Non impostato**.

Nella schermata di **selezione del RileyLink** premi il pulsante **Scansione** per eseguire la scansione di tutti i dispositivi Bluetooth disponibili e seleziona il tuo RileyLink dall'elenco. Una volta selezionato correttamente, verrai riportato alla schermata di selezione del driver del micro, con le impostazioni del driver Omnipod che mostreranno il RileyLink selezionato con il relativo indirizzo MAC.

Premi il pulsante **Avanti** per procedere con il resto della **configurazione guidata**. Può volerci anche un minuto prima che il RileyLink selezionato si connetta e il pulsante **Avanti** diventi attivo.

I passaggi dettagliati per la configurazione del dispositivo di comunicazione con il pod sono elencati di seguito nella [Sezione Configurazione RileyLink](#OmnipodEros-rileylink-setup).

**OPPURE**

### Opzione 2: Il Generatore di configurazione

Tramite il **menu a tendina** nell'angolo in alto a sinistra, in **Generatore di configurazione (1)** ➜**Micro**➜**Omnipod** selezionando il **pulsante radio (2)** intitolato **Omnipod**. Selezionando la **casella di controllo (4)** accanto all'**icona impostazioni (3)** verrà visualizzato il menu Omnipod come scheda nell'interfaccia AAPS intitolata **POD**. In questa documentazione ci si riferirà ad essa come la scheda **Omnipod (POD)**.

> **NOTA:** Un modo più rapido per accedere alle **impostazioni Omnipod** è disponibile di seguito nella [sezione Impostazioni Omnipod](#OmnipodEros-omnipod-settings) di questo documento.
> 
> ![Attiva_Driver_Omnipod_3](../images/omnipod/Enable_Omnipod_Driver_3.png) ![Attiva_Driver_Omnipod_4](../images/omnipod/Enable_Omnipod_Driver_4.png)

### Verifica della selezione del driver Omnipod

*Nota: Se si è usciti dalla Configurazione guidata prima di selezionare il RileyLink, il driver Omnipod è abilitato ma sarà comunque necessario selezionare il RileyLink.  È possibile che la scheda Omnipod (POD) appaia come mostrato di seguito*

Per verificare di aver abilitato il driver Omnipod in AAPS **scorri verso sinistra** dalla scheda **Panoramica**, dove ora sarà visibile una scheda **Omnipod** o **POD**.

![Attiva_Driver_Omnipod_5](../images/omnipod/Enable_Omnipod_Driver_5.png)

## Configurazione Omnipod

Scorri a sinistra verso la scheda **Omnipod (POD)** dove potrai gestire tutte le funzioni del pod e del RileyLink (alcune di queste funzioni non sono abilitate o visibili senza una sessione pod attiva):

> ![aggiorna_stato_pod](../images/omnipod/ICONS/omnipod_overview_refresh_pod_status.png) Aggiorna connettività e stato del pod
> 
> ![gestione_pod](../images/omnipod/ICONS/omnipod_overview_pod_management.png) Gestione pod (Attiva, Disattiva, Emetti segnale acustico di test, Statistiche RileyLink e Cronologia pod)

(OmnipodEros-rileylink-setup)=

### Configurazione RileyLink

Se hai già abbinato correttamente il RileyLink nella Configurazione guidata o nei passaggi precedenti, procedi alla [Sezione Attivazione pod](#OmnipodEros-activating-a-pod) di seguito.

*Nota: Un buon indicatore visivo che il RileyLink non è connesso è che i pulsanti Insulina e Calcolatrice nella scheda HOME saranno assenti. Questo accade anche nei primi 30 secondi circa dopo l'avvio di AAPS, mentre stabilisce attivamente la connessione al RileyLink.*

1. Assicurarsi che il RileyLink sia completamente carico e acceso.

2. Dopo aver selezionato il driver Omnipod, identificare e selezionare il RileyLink da **Generatore di configurazione (1)** ➜**Micro**➜**Omnipod**➜**Icona ingranaggio (Impostazioni) (2)** ➜**Configurazione RileyLink (3)** premendo il testo **Non impostato** o **Indirizzo MAC (se presente)**.

   > Assicurarsi che la batteria del RileyLink sia carica e che sia [posizionato nelle vicinanze](#OmnipodEros-optimal-omnipod-and-rileylink-positioning) (~30 cm o meno) del telefono affinché AAPS possa identificarlo tramite il suo indirizzo MAC. Una volta selezionato, si può procedere ad attivare la prima sessione pod. Usare il pulsante Indietro del telefono per tornare all'interfaccia principale di AAPS.
   > 
   > ![Configurazione_RileyLink_1](../images/omnipod/RileyLink_Setup_1.png) ![Configurazione_RileyLink_2](../images/omnipod/RileyLink_Setup_2.png)

3. Nella schermata di **selezione RileyLink** premere il pulsante **Scansione (4)** per avviare una scansione Bluetooth. **Selezionare il proprio RileyLink (5)** dall'elenco dei dispositivi Bluetooth disponibili.

   > ![Configurazione_RileyLink_3](../images/omnipod/RileyLink_Setup_3.png) ![Configurazione_RileyLink_4](../images/omnipod/RileyLink_Setup_4.png)

4. Dopo la selezione riuscita, si torna alla pagina Impostazioni Omnipod che mostra l'**indirizzo MAC del RileyLink attualmente selezionato (6).**

   > ![Configurazione_RileyLink_5](../images/omnipod/RileyLink_Setup_5.png)

5. Verificare che nella scheda **Omnipod (POD)** lo **Stato RileyLink (1)** risulti **Connesso.** Il campo **Stato pod (2)** dovrebbe mostrare **Nessun pod attivo**; in caso contrario, riprovare il passaggio precedente o uscire da AAPS per verificare se questo aggiorna la connessione.

   > ![Configurazione_RileyLink_6](../images/omnipod/RileyLink_Setup_6.png)

(OmnipodEros-activating-a-pod)=

### Attivazione di un pod

Prima di poter attivare un pod, assicurarsi di aver configurato e connesso correttamente il RileyLink nelle impostazioni Omnipod.

*PROMEMORIA: La comunicazione con il pod avviene a distanze limitate durante l'abbinamento per l'attivazione del pod, per misure di sicurezza. Prima dell'abbinamento il segnale radio del pod è più debole, ma dopo l'abbinamento funzionerà alla piena potenza del segnale. Durante queste procedure, assicurarsi che il pod sia* [nelle vicinanze](#OmnipodEros-optimal-omnipod-and-rileylink-positioning) (~30 cm o meno) ma non sopra o accanto al RileyLink.*

01. Guasti del pod

    > ![Attiva_Pod_1](../images/omnipod/Activate_Pod_1.png) ![Attiva_Pod_2](../images/omnipod/Activate_Pod_2.png)

02. Viene visualizzata la schermata **Riempi il pod**. Riempire un nuovo pod con almeno 80 unità di insulina e attendere due segnali acustici che indicano che il pod è pronto per essere preparato. Nel calcolare la quantità totale di insulina necessaria per 3 giorni, tenere presente che la preparazione del pod richiede da 12 a 15 unità.

    > ![Attiva_Pod_3](../images/omnipod/Activate_Pod_3.png)
    > 
    > Assicurarsi che il nuovo pod e il RileyLink siano nelle vicinanze l'uno dell'altro (~30 cm o meno) e cliccare il pulsante **Avanti**.

03. Nella schermata **Inizializza pod**, il pod inizierà la preparazione (si sentirà un clic seguito da una serie di ticchettii mentre il pod si prepara). Se il RileyLink è fuori portata dal pod che si sta attivando, si riceverà un messaggio di errore **Nessuna risposta dal pod**. In questo caso, [avvicinare il RileyLink](#OmnipodEros-optimal-omnipod-and-rileylink-positioning) (~30 cm o meno) al pod senza però posizionarlo sopra o accanto ad esso, e cliccare il pulsante **Riprova (1)**.

    > ![Attiva_Pod_4](../images/omnipod/Activate_Pod_4.png) ![Attiva_Pod_5](../images/omnipod/Activate_Pod_5.png)

04. Dopo una preparazione riuscita verrà mostrato un segno di spunta verde e il pulsante **Avanti** diventerà attivo. Cliccare il pulsante **Avanti** per completare l'inizializzazione della preparazione del pod e visualizzare la schermata **Applica pod**.

    > ![Attiva_Pod_6](../images/omnipod/Activate_Pod_6.png)

05. Preparare quindi il sito di infusione del nuovo pod. Rimuovere il cappuccio in plastica dall'ago del pod e il foglio di carta bianco dall'adesivo, e applicare il pod al sito solitamente scelto sul proprio corpo. Al termine, cliccare il pulsante **Avanti**.

    > ![Attiva_Pod_7](../images/omnipod/Activate_Pod_7.png)

06. Apparirà ora la finestra di dialogo **Applica pod**. **Cliccare il pulsante OK SOLO se si è pronti ad inserire la cannula**.

    > ![Attiva_Pod_8](../images/omnipod/Activate_Pod_8.png)

07. Dopo aver premuto **OK**, potrebbe volerci del tempo prima che l'Omnipod risponda e inserisca la cannula (massimo 1-2 minuti), quindi pazientare.

    > Se il RileyLink è fuori portata dal pod che si sta attivando, si riceverà un messaggio di errore **Nessuna risposta dal pod**. In questo caso, avvicinare il RileyLink (~30 cm o meno) al pod senza posizionarlo sopra o accanto ad esso, e cliccare il pulsante **Riprova**.
    > 
    > Se il RileyLink è fuori dalla portata Bluetooth o non ha una connessione attiva con il telefono, si riceverà un messaggio di errore **Nessuna risposta da RileyLink**. In questo caso, avvicinare il RileyLink al telefono e cliccare il pulsante **Riprova**.
    > 
    > *NOTA: Prima dell'inserimento della cannula, è buona pratica pizzicare la pelle vicino al punto di inserimento della cannula. Questo garantisce un'inserzione fluida dell'ago e ridurrà le probabilità di sviluppare occlusioni.*
    > 
    > ![Attiva_Pod_9](../images/omnipod/Activate_Pod_9.png)
    > 
    > ![Attiva_Pod_10](../images/omnipod/Activate_Pod_10.png) ![Attiva_Pod_11](../images/omnipod/Activate_Pod_11.png)

08. Appare un segno di spunta verde e il pulsante **Avanti** diventa attivo dopo il corretto inserimento della cannula. Cliccare il pulsante **Avanti**.

    > ![Attiva_Pod_12](../images/omnipod/Activate_Pod_12.png)

09. Viene visualizzata la schermata **Pod attivato**. Cliccare il pulsante verde **Fine**. Congratulazioni! Hai avviato una nuova sessione pod attiva.

    > ![Attiva_Pod_13](../images/omnipod/Activate_Pod_13.png)

10. La schermata del menu **Gestione pod** ora dovrebbe mostrare il pulsante **Attiva pod (1)** *disabilitato* e il pulsante **Disattiva pod (2)** *abilitato*. Questo perché ora è attivo un pod e non è possibile attivarne un altro senza prima disattivare il pod attualmente attivo.

    Cliccare il pulsante Indietro del telefono per tornare alla schermata della scheda **Omnipod (POD)** che ora mostrerà le informazioni sul pod per la sessione pod attiva, inclusa la velocità basale corrente, il livello del serbatoio del pod, l'insulina erogata, gli errori e gli avvisi del pod.

    Per ulteriori dettagli sulle informazioni visualizzate, consultare la sezione [Scheda Omnipod (POD)](#OmnipodEros-omnipod-pod-tab) di questo documento.

    ![Attiva_Pod_14](../images/omnipod/Activate_Pod_14.png) ![Attiva_Pod_15](../images/omnipod/Activate_Pod_15.png)

### Disattivazione di un pod

In condizioni normali, la vita di un pod dura tre giorni (72 ore) più ulteriori 8 ore dopo l'avviso di scadenza del pod, per un totale di 80 ore di utilizzo del pod.

Per disattivare un pod (per scadenza o per un guasto del pod):

1. L'intera cronologia è disponibile solo per il pod attualmente attivo; dopo il cambio del pod, questa cronologia verrà cancellata e verranno registrati e mostrati solo gli eventi del pod appena attivato.

   > ![Disattiva_Pod_1](../images/omnipod/Deactivate_Pod_1.png) ![Disattiva_Pod_2](../images/omnipod/Deactivate_Pod_2.png)

2. Nella schermata **Disattiva pod**, assicurarsi innanzitutto che il RileyLink sia nelle vicinanze del pod ma non sopra o accanto ad esso, poi cliccare il pulsante **Avanti** per iniziare il processo di disattivazione del pod.

   > ![Disattiva_Pod_3](../images/omnipod/Deactivate_Pod_3.png)

3. Apparirà la schermata **Disattivazione pod in corso** e si riceverà un segnale acustico di conferma dal pod che la disattivazione è avvenuta con successo.

   > ![Disattiva_Pod_4](../images/omnipod/Deactivate_Pod_4.png)
   > 
   > **SE la disattivazione non riesce** e non si riceve un segnale acustico di conferma, si potrebbe ricevere il messaggio **Nessuna risposta da RileyLink** o **Nessuna risposta dal pod**. Cliccare il pulsante **Riprova (1)** per tentare di nuovo la disattivazione. Se la disattivazione continua a non riuscire, cliccare il pulsante **Scarta pod (2)** per scartare il pod. È ora possibile rimuovere il pod poiché la sessione attiva è stata disattivata. Se il pod emette un allarme acustico, potrebbe essere necessario silenziarlo manualmente (usando uno spillo o una graffetta) poiché il pulsante **Scarta pod (2)** non lo silenzia.
   > 
   > > ![Disattiva_Pod_5](../images/omnipod/Deactivate_Pod_5.png)  ![Disattiva_Pod_6](../images/omnipod/Deactivate_Pod_6.png)

4. Alla disattivazione riuscita apparirà un segno di spunta verde. Cliccare il pulsante **Avanti** per visualizzare la schermata di pod disattivato. È ora possibile rimuovere il pod poiché la sessione attiva è stata disattivata.

   > ![Disattiva_Pod_7](../images/omnipod/Deactivate_Pod_7.png)

5. Cliccare il pulsante verde per tornare alla schermata **Gestione pod**.

   > ![Disattiva_Pod_8](../images/omnipod/Deactivate_Pod_8.png)

6. Si torna al menu **Gestione pod**; premere il pulsante Indietro del telefono per tornare alla scheda **Omnipod (POD)**. Verificare che il campo **Stato RileyLink:** riporti **Connesso** e il campo **Stato pod:** visualizzi il messaggio **Nessun pod attivo**.

   > ![Disattiva_Pod_9](../images/omnipod/Deactivate_Pod_9.png)  ![Disattiva_Pod_10](../images/omnipod/Deactivate_Pod_10.png)

### Sospensione e ripresa dell'erogazione di insulina

Il processo seguente mostra come sospendere e riprendere l'erogazione dal microinfusore di insulina.

*NOTA - se non si vede un pulsante SOSPENDI*, non è stato abilitato per la visualizzazione nella scheda Omnipod (POD). Abilitare l'impostazione **Mostra pulsante Sospendi erogazione nella scheda Omnipod** nelle [Impostazioni Omnipod](#OmnipodEros-omnipod-settings) sotto **Altro**.

#### Sospensione dell'erogazione di insulina

Usare questo comando per mettere il pod attivo in stato di sospensione. In questo stato di sospensione, il pod non erogherà più insulina. Questo comando imita la funzione di sospensione che il PDM Omnipod originale invia a un pod attivo.

1. Andare alla scheda **Omnipod (POD)** e cliccare sul pulsante **SOSPENDI (1)**. Il comando di sospensione viene inviato dal RileyLink al pod attivo e il pulsante **SOSPENDI (3)** diventerà grigio. Lo **Stato pod (2)** visualizzerà **SOSPENDI EROGAZIONE**.

   > ![Sospensione_Erogazione_Insulina_1](../images/omnipod/Suspend_Insulin_Delivery_1.png) ![Sospensione_Erogazione_Insulina_2](../images/omnipod/Suspend_Insulin_Delivery_2.png)

2. Quando il comando di sospensione è confermato con successo dal RileyLink, viene visualizzata una finestra di dialogo di conferma con il messaggio **Tutta l'erogazione di insulina è stata sospesa**. Cliccare **OK** per confermare e procedere.

   > ![Sospensione_Erogazione_Insulina_3](../images/omnipod/Suspend_Insulin_Delivery_3.png)

3. Il pod attivo ha ora sospeso tutta l'erogazione di insulina. La scheda **Omnipod (POD)** aggiornerà lo **Stato pod (1)** a **Sospeso**. Il pulsante **SOSPENDI** cambierà in un nuovo pulsante **Riprendi erogazione (2)**.

   > ![Sospensione_Erogazione_Insulina_4](../images/omnipod/Suspend_Insulin_Delivery_4.png)

#### Ripresa dell'erogazione di insulina

Usare questo comando per istruire il pod attivo, attualmente sospeso, a riprendere l'erogazione di insulina. Dopo che il comando è stato elaborato con successo, l'insulina riprenderà l'erogazione normale usando la velocità basale corrente basata sull'orario corrente dal profilo basale attivo. Il pod accetterà di nuovo i comandi per bolo, TBR e SMB.

1. Andare alla scheda **Omnipod (POD)** e assicurarsi che il campo **Stato pod (1)** visualizzi **Sospeso**, poi premere il pulsante **Riprendi erogazione (2)** per avviare il processo di istruzione del pod corrente a riprendere la normale erogazione di insulina. Un messaggio **RIPRENDI EROGAZIONE** verrà visualizzato nel campo **Stato pod (3)**, a indicare che il RileyLink sta inviando attivamente il comando al pod sospeso.

   > ![Riprendi_Erogazione_Insulina_1](../images/omnipod/Resume_Insulin_Delivery_1.png) ![Riprendi_Erogazione_Insulina_2](../images/omnipod/Resume_Insulin_Delivery_2.png)

2. Quando il comando di ripresa dell'erogazione è confermato con successo dal RileyLink, viene visualizzata una finestra di dialogo di conferma con il messaggio **L'erogazione di insulina è stata ripresa**. Cliccare **OK** per confermare e procedere.

   > ![Riprendi_Erogazione_Insulina_3](../images/omnipod/Resume_Insulin_Delivery_3.png)

3. La scheda **Omnipod (POD)** aggiornerà il campo **Stato pod (1)** per visualizzare **IN ESECUZIONE,** e il pulsante **Riprendi erogazione** ora visualizzerà il pulsante **SOSPENDI (2)**.

   > ![Riprendi_Erogazione_Insulina_4](../images/omnipod/Resume_Insulin_Delivery_4.png)

### Conferma degli avvisi del pod

*NOTA - se non si vede un pulsante CONF. AVVISI, è perché viene visualizzato condizionalmente nella scheda Omnipod (POD) SOLO quando è stato attivato l'avviso di scadenza del pod o di serbatoio esaurito.*

Il processo seguente mostra come riconoscere e ignorare i segnali acustici del pod che si verificano quando il pod attivo raggiunge il limite di tempo di avviso prima della scadenza del pod a 72 ore (3 giorni). Questo limite di tempo di avviso è definito nelle impostazioni degli avvisi Omnipod in **Ore prima della chiusura**. La durata massima di un pod è 80 ore (3 giorni 8 ore), tuttavia Insulet raccomanda di non superare il limite delle 72 ore (3 giorni).

*NOTA - Se è stata abilitata l'impostazione "Conferma automaticamente gli avvisi pod" negli avvisi Omnipod, questo avviso verrà gestito automaticamente dopo la prima occorrenza e NON sarà necessario ignorare manualmente l'avviso.*

1. Quando viene raggiunto il limite di tempo di avviso definito in **Ore prima della chiusura**, il pod emette segnali acustici di avviso per informare l'utente che si sta avvicinando alla scadenza e che presto sarà necessario il cambio pod. È possibile verificarlo nella scheda **Omnipod (POD)**: il campo **Scadenza pod: (1)** mostrerà il momento esatto in cui il pod scadrà (72 ore dopo l'attivazione) e il testo diventerà **rosso** dopo che tale orario è trascorso; nel campo **Avvisi pod attivi (2)** viene visualizzato il messaggio di stato **Il pod scadrà presto**. Questo evento attiva il pulsante **CONF. AVVISI (3)**. Una **notifica di sistema (4)** informa inoltre dell'imminente scadenza del pod.

   > ![Conferma_Allarmi_1](../images/omnipod/Acknowledge_Alerts_1.png) ![Conferma_Allarmi_2](../images/omnipod/Acknowledge_Alerts_2.png)

2. Andare alla scheda **Omnipod (POD)** e premere il pulsante **GEST. POD (1)** per accedere al menu **Gestione pod**, poi premere il pulsante **Statistiche RileyLink (2)** per visualizzare le impostazioni del **RileyLink (3)** e del **Dispositivo (4)** pod attivo.

   > ![Conferma_Allarmi_3](../images/omnipod/Acknowledge_Alerts_3.png)

3. Alla **disattivazione riuscita** degli avvisi, il pod attivo emetterà **2 segnali acustici** e verrà visualizzata una finestra di dialogo di conferma con il messaggio **Gli avvisi attivi sono stati confermati**. Cliccare il pulsante **OK** per confermare e chiudere la finestra di dialogo.

   > ![Conferma_Allarmi_4](../images/omnipod/Acknowledge_Alerts_4.png)
   > 
   > Se il RileyLink è fuori portata dal pod mentre il comando di conferma avvisi è in elaborazione, verrà visualizzato un messaggio di avviso con 2 opzioni. **Silenzia (1)** silenzia questo avviso corrente. **OK (2)** conferma questo avviso e consente all'utente di provare di nuovo a confermare gli avvisi.
   > 
   > ![Conferma_Allarmi_5](../images/omnipod/Acknowledge_Alerts_5.png)

4. Andare alla scheda **Omnipod (POD)**; nel campo **Avvisi pod attivi**, il messaggio di avviso non viene più visualizzato e il pod attivo non emetterà più i segnali acustici di avviso di scadenza.

(OmnipodEros-view-pod-history)=

### Visualizzare la cronologia pod

Questa sezione mostra come visualizzare la cronologia del pod attivo e filtrare per diverse categorie di azioni. Lo strumento cronologia pod consente di visualizzare le azioni e i risultati applicati al pod attualmente attivo durante la sua vita di tre giorni (72-80 ore).

Questa funzionalità è utile per verificare boli, TBR, modifiche basali che sono stati somministrati ma di cui non si è sicuri se siano stati completati. Le categorie rimanenti sono utili in generale per la risoluzione dei problemi.

*NOTA:* I comandi **Incerti** appariranno nella cronologia del pod, tuttavia per loro natura non è possibile garantirne l’accuratezza.

1. Visualizzare la cronologia pod

   > ![Storico_Pod_1](../images/omnipod/Pod_History_1.png) ![Storico_Pod_2](../images/omnipod/Pod_History_2.png)

2. Nella schermata **Cronologia pod**, la categoria predefinita **Tutte (1)** mostra la **Data e ora (2)** di tutte le **Azioni (3)** e **Risultati (4)** del pod in ordine cronologico inverso. Usare il **pulsante Indietro del telefono 2 volte** per tornare alla scheda **Omnipod (POD)**.

   > ![Storico_Pod_3](../images/omnipod/Pod_History_3.png) ![Storico_Pod_4](../images/omnipod/Pod_History_4.png)

### Visualizzare impostazioni e cronologia RileyLink

Questa sezione mostra come visualizzare le impostazioni del pod attivo e del RileyLink insieme alla cronologia delle comunicazioni di ciascuno. Questa funzionalità, una volta aperta, è divisa in due sezioni: **Impostazioni** e **Cronologia**.

L'utilizzo principale di questa funzionalità è quando il dispositivo di comunicazione con il pod è fuori dalla portata Bluetooth del telefono per un certo periodo di tempo e lo **stato RileyLink** riporta **RileyLink irraggiungibile**. Il pulsante **AGGIORNA** nella scheda principale **Omnipod (POD)** tenterà manualmente di ristabilire la comunicazione Bluetooth con il RileyLink attualmente configurato.

Nel caso in cui il pulsante **AGGIORNA** non ripristini la connessione al dispositivo di comunicazione con il pod, seguire i passaggi aggiuntivi di seguito per una riconnessione manuale.

#### Ristabilire manualmente la comunicazione Bluetooth del dispositivo di comunicazione con il pod

1. Accedere al menu **Selezione RileyLink** selezionando il **menu a 3 punti (1)** nell'angolo in alto a destra della scheda **Omnipod (POD)** e selezionando **Preferenze Omnipod (2)** dal menu a discesa. Nel menu **Impostazioni Omnipod** sotto **Configurazione RileyLink (3)** premere il testo **Non impostato** (se non è selezionato alcun dispositivo) o **Indirizzo MAC** (se è presente un dispositivo) per aprire il menu **Selezione RileyLink**.

   > ![Reset_RileyLink_Bluetooth_1](../images/omnipod/RileyLink_Bluetooth_Reset_1.png) ![Reset_RileyLink_Bluetooth_2](../images/omnipod/RileyLink_Bluetooth_Reset_2.png)

2. Nella schermata **Impostazioni RileyLink (1)**, nella sezione **RileyLink (2)**, è possibile confermare lo stato della connessione Bluetooth nei campi **Stato connessione ed errore: (3)**. A *Bluetooth Error* and *RileyLink unreachable* status should be shown. Avviare la riconnessione Bluetooth manuale premendo il pulsante **aggiorna (4)** in basso a destra.

   > ![Reset_RileyLink_Bluetooth_3](../images/omnipod/RileyLink_Bluetooth_Reset_3.png)
   > 
   > Se il dispositivo di comunicazione con il pod non risponde o è fuori portata dal telefono mentre il comando di aggiornamento Bluetooth è in elaborazione, verrà visualizzato un messaggio di avviso con 2 opzioni.

   - **Silenzia (1)** silenzia questo avviso corrente.
   - **OK (2)** conferma questo avviso e consente di provare a ristabilire di nuovo la connessione Bluetooth.

   > ![Reset_RileyLink_Bluetooth_4](../images/omnipod/RileyLink_Bluetooth_Reset_4.png)

3. Se la **connessione Bluetooth** non viene ristabilita, provare a spegnere e riaccendere manualmente la funzione Bluetooth del telefono.

4. Dopo una riconnessione Bluetooth RileyLink riuscita, il campo **Stato connessione: (1)** dovrebbe riportare **RileyLink pronto**. Congratulazioni, il dispositivo di comunicazione con il pod configurato è stato riconnesso ad AAPS!

   > ![Reset_RileyLink_Bluetooth_5](../images/omnipod/RileyLink_Bluetooth_Reset_5.png)

#### Impostazioni del dispositivo di comunicazione con il pod e del pod attivo

Questa schermata fornisce informazioni, stato e configurazione delle impostazioni sia per il dispositivo di comunicazione con il pod attualmente configurato che per il pod Omnipod Eros attualmente attivo.

1. Impostazioni_Omnipod_3

   > ![Impostazioni_Statistiche_RileyLink_1](../images/omnipod/RileyLink_Statistics_Settings_1.png) ![Impostazioni_Statistiche_RileyLink_2](../images/omnipod/RileyLink_Statistics_Settings_2.png)
   > 
   > ![Impostazioni_Statistiche_RileyLink_3](../images/omnipod/RileyLink_Statistics_Settings_3.png)

##### Campi RileyLink (3)

> - **Indirizzo:** Indirizzo MAC del dispositivo di comunicazione con il pod selezionato, definito nelle Impostazioni Omnipod.
> - **Nome:** Nome di identificazione Bluetooth del dispositivo di comunicazione con il pod selezionato, definito nelle impostazioni Bluetooth del telefono.
> - **Livello batteria:** Visualizza il livello di batteria corrente del dispositivo di comunicazione con il pod connesso.
> - **Dispositivo connesso:** Modello del pod Omnipod che comunica attualmente con il dispositivo di comunicazione con il pod.
> - **Stato connessione:** Lo stato corrente della connessione Bluetooth tra il dispositivo di comunicazione con il pod e il telefono che esegue AAPS.
> - **Errore connessione:** Se si verifica un errore con la connessione Bluetooth, i dettagli verranno visualizzati qui.
> - **Versione firmware:** Versione firmware corrente installata sul dispositivo di comunicazione con il pod attivamente connesso.

##### Campi dispositivo (4) - Con un pod attivo

> - **Tipo dispositivo:** Il tipo di dispositivo che comunica con il dispositivo di comunicazione con il pod (microinfusore pod Omnipod).
> - **Modello dispositivo:** Il modello del dispositivo attivo connesso al dispositivo di comunicazione con il pod (il modello corrente del pod Omnipod, che è Eros).
> - **Numero di serie microinfusore:** Numero di serie del pod attualmente attivato.
> - **Frequenza microinfusore:** Frequenza radio di comunicazione che il dispositivo di comunicazione con il pod ha sintonizzato per la comunicazione con il pod.
> - **Ultima frequenza usata:** Ultima frequenza radio nota usata dal pod per comunicare con il dispositivo di comunicazione con il pod.
> - **Ultimo contatto dispositivo:** Data e ora dell'ultimo contatto del pod con il dispositivo di comunicazione con il pod.
> - **Pulsante Aggiorna** aggiorna manualmente le impostazioni in questa pagina.

(omnipod-eros-rileylink-and-active-pod-history)=
#### Cronologia RileyLink e pod attivo

This screen provides information in reverse chronological order of each state or action that either the RileyLink or currently connected pod is in or has taken. The entire history is only available for the currently active pod, after a pod change this history will be erased and only events from the newly activated pod will be recorded and shown.

1. Andare alla scheda **Omnipod (POD)**, cliccare sul pulsante **GEST. POD (1)**, nella schermata **Gestione pod** cliccare sul pulsante **Disattiva pod (2)**.

   > ![Storico_Statistiche_RileyLink_1](../images/omnipod/RileyLink_Statistics_History_1.png) ![Storico_Statistiche_RileyLink_2](../images/omnipod/RileyLink_Statistics_History_2.png)
   > 
   > ![Storico_Statistiche_RileyLink_3](../images/omnipod/RileyLink_Statistics_History_3.png)

##### Campi

> - **Data e ora:** In ordine cronologico inverso, il timestamp di ogni evento.
> - **Dispositivo:** Il dispositivo a cui si riferisce l'azione o lo stato corrente.
> - **Stato o azione:** Lo stato corrente o l'azione eseguita dal dispositivo.

(OmnipodEros-omnipod-pod-tab)=

## Scheda Omnipod (POD)

Di seguito è riportata una spiegazione del layout e del significato delle icone e dei campi di stato nella scheda **Omnipod (POD)** nell'interfaccia principale di AAPS.

*NOTA: Se un messaggio nei campi di stato della scheda Omnipod (POD) riporta (incerto), sarà necessario premere il pulsante Aggiorna per cancellarlo e aggiornare lo stato del pod.*

> ![Scheda_Omnipod](../images/omnipod/Omnipod_Tab.png)

### Campi

- **Stato RileyLink:** Visualizza lo stato di connessione corrente del RileyLink

- *RileyLink irraggiungibile* - il dispositivo di comunicazione con il pod non è nella portata Bluetooth del telefono, è spento o ha un guasto che impedisce la comunicazione Bluetooth.
- *RileyLink pronto* - il dispositivo di comunicazione con il pod è acceso e sta inizializzando attivamente la connessione Bluetooth.
- *Connesso* - il dispositivo di comunicazione con il pod è acceso, connesso e in grado di comunicare attivamente via Bluetooth.

- **Indirizzo pod:** Visualizza l'indirizzo corrente a cui si fa riferimento al pod attivo.

- **Scadenza pod:** Visualizza la data e l'ora in cui scadrà il pod attivo.

- **TID:** Visualizza il numero di serie del pod.

- **Versione firmware:** Visualizza la versione firmware del pod attivo.

- **Ora sul pod:** Visualizza l'ora corrente sul pod attivo.

- **Stato pod:** Visualizza lo stato del pod attivo.

- **Ultima connessione:** Visualizza l'ultima volta in cui è stata stabilita la comunicazione con il pod attivo.

- **Ultimo bolo:** Visualizza il dosaggio dell'ultimo bolo inviato al pod attivo e quanto tempo fa è stato erogato (tra parentesi).

- *Pochi secondi fa* - meno di 20 secondi fa.
- *Meno di un minuto fa* - più di 20 secondi ma meno di 60 secondi fa.
- *1 minuto fa* - più di 60 secondi ma meno di 120 secondi (2 min).
- *XX minuti fa* - più di 2 minuti fa, come definito dal valore di XX.

- **Ultimo bolo:** Visualizza il dosaggio dell'ultimo bolo inviato al pod attivo e quanto tempo fa è stato erogato (tra parentesi).

- **Velocità basale base:** Visualizza la velocità basale programmata per l'orario corrente dal profilo della velocità basale.

- **Ora sul pod:** Visualizza l'ora corrente sul pod attivo.

- Unità / ora @ ora di emissione TBR (minuti eseguiti / minuti totali di esecuzione TBR).
- *Esempio:* 0.00U/h @18:25 ( 90/120 minutes)

- **Serbatoio:** Visualizza oltre 50+U rimanenti quando nel serbatoio sono presenti più di 50 unità. Al di sotto di questo valore, le unità esatte vengono visualizzate in testo giallo.

- **Totale erogato:** Visualizza il numero totale di unità di insulina erogate dal serbatoio. *Nota: si tratta di un'approssimazione poiché la preparazione e il riempimento del pod non sono un processo esatto.*

- **Errori:** Visualizza l'ultimo errore riscontrato. Consultare la [cronologia pod](#OmnipodEros-view-pod-history), la [cronologia RileyLink](#omnipod-eros-rileylink-and-active-pod-history) e i file di log per gli errori passati e informazioni più dettagliate.

- **Avvisi pod attivi:** Riservato agli avvisi attualmente in esecuzione sul pod attivo. Normalmente utilizzato quando la scadenza del pod è superiore a 72 ore e i segnali acustici del pod sono in esecuzione.

### Icone

- **AGGIORNA:**

  > ![aggiorna_stato_pod](../images/omnipod/ICONS/omnipod_overview_refresh_pod_status.png)
  > 
  > Invia un comando di aggiornamento al pod attivo per aggiornare la comunicazione.
  > 
  > Usare per aggiornare lo stato del pod e ignorare i campi di stato che contengono il testo (incerto).
  > 
  > Consultare la [sezione Risoluzione dei problemi](#OmnipodEros-troubleshooting) di seguito per ulteriori informazioni.

- **POD MGMT:**

  > ![gestione_pod](../images/omnipod/ICONS/omnipod_overview_pod_management.png)
  > 
  > Naviga nel menu Gestione pod.

- **RIPRENDI EROGAZIONE:**

  > ![conferma_allarmi](../images/omnipod/ICONS/omnipod_overview_ack_alerts.png)
  > 
  > Quando premuto, disabilita i segnali acustici di scadenza del pod e le notifiche.
  > 
  > Il pulsante viene visualizzato solo quando il tempo del pod ha superato il tempo di avviso di scadenza. Alla conferma riuscita, questa icona non apparirà più.

- **IMPOSTA ORA:**

  > ![imposta_ora](../images/omnipod/ICONS/omnipod_overview_set_time.png)
  > 
  > Quando premuto, aggiorna l'ora sul pod con l'ora corrente del telefono.

- **SOSPENDI:**

  > ![sospensione](../images/omnipod/ICONS/omnipod_overview_suspend.png)
  > 
  > Sospende il pod attivo.

- **RESUME DELIVERY:**

  > ![riprendi](../images/omnipod/ICONS/omnipod_overview_resume.png)
  > 
  > > Riprende il pod attivo attualmente sospeso.

### Menu Gestione pod

Di seguito è riportata una spiegazione del layout e del significato delle icone nel menu **Gestione pod** accessibile dalla scheda **Omnipod (POD)**.

> ![Scheda_Omnipod_Gestione_Pod](../images/omnipod/Omnipod_Tab_Pod_Management.png)

- **Attiva pod**

  > ![attiva_pod](../images/omnipod/ICONS/omnipod_overview_pod_management_activate_pod.png)
  > 
  > Prepara e attiva un nuovo pod.

- **Disattiva pod**

  > ![disattiva_pod](../images/omnipod/ICONS/omnipod_overview_pod_management_deactivate_pod.png)
  > 
  > Disattiva il pod attualmente attivo.
  > 
  > Un pod parzialmente abbinato ignora questo comando.
  > 
  > Usare questo comando per disattivare un pod che emette allarmi (errore 49).
  > 
  > Se il pulsante è disabilitato (grigio) usare il pulsante Scarta pod.

- **Play test beep**

  > ![esegui_BIP_di_prova](../images/omnipod/ICONS/omnipod_overview_pod_management_play_test_beep.png)
  > 
  > Emette un singolo segnale acustico di prova sul pod quando premuto.

- **Discard pod**

  > ![scarta_pod](../images/omnipod/ICONS/omnipod_overview_pod_management_discard_pod.png)
  > 
  > Disattiva e scarta lo stato del pod di un pod che non risponde quando premuto.
  > 
  > Il pulsante viene visualizzato solo quando si verificano casi molto specifici in cui la disattivazione corretta non è più possibile:
  > 
  > > - Un **pod non è completamente abbinato** e quindi ignora i comandi di disattivazione.
  > > - Un **pod è bloccato** durante il processo di abbinamento tra un passaggio e l'altro.
  > > - Un **pod semplicemente non si abbina affatto.**

- **Cronologia pod**

  > ![storico_pod](../images/omnipod/ICONS/omnipod_overview_pod_management_pod_history.png)
  > 
  > Visualizza la cronologia delle attività del pod attivo.

- **Statistiche RileyLink:**

  > ![statistiche_rileylink](../images/omnipod/ICONS/omnipod_overview_pod_management_rileylink_stats.png)
  > 
  > Naviga alla schermata Statistiche RileyLink che mostra le impostazioni correnti e la cronologia delle connessioni RileyLink.
  > 
  > > - **Impostazioni** - visualizza le informazioni sulle impostazioni del RileyLink e del pod attivo.
  > > - **Cronologia** - visualizza la cronologia delle comunicazioni del RileyLink e del pod.

- **Reimposta configurazione RileyLink**

  > ![reset_configurazione_rileylink](../images/omnipod/ICONS/omnipod_overview_pod_management_reset_rileylink_config.png)
  > 
  > Quando si preme questo pulsante, viene reimpostata la configurazione del dispositivo di comunicazione con il pod attualmente connesso.
  > 
  > > - Quando la comunicazione viene avviata, vengono inviati e impostati dati specifici nel RileyLink > - Vengono impostati i registri di memoria > - Vengono impostati i protocolli di comunicazione > - Viene impostata la frequenza radio sintonizzata 
  > > - Consultare le [note aggiuntive](#OmnipodEros-reset-rileylink-config-notes) alla fine di questa tabella.

- **Leggi log pulse:**

  > ![pulse_log](../images/omnipod/ICONS/omnipod_overview_pod_management_pulse_log.png)
  > 
  > > Invia il log pulse del pod attivo negli appunti.

(OmnipodEros-reset-rileylink-config-notes)=

#### *Note sulla reimpostazione della configurazione RileyLink*

- Il principale utilizzo di questa funzionalità è quando il dispositivo di comunicazione con il pod attualmente attivo non risponde e la comunicazione è bloccata.
- Se il dispositivo di comunicazione con il pod viene spento e poi riacceso, è necessario premere il pulsante **Reimposta configurazione RileyLink** per impostare questi parametri di comunicazione nella configurazione del dispositivo.
- Se NON viene fatto, AAPS dovrà essere riavviato dopo il riavvio del dispositivo di comunicazione con il pod.
- Questo pulsante **NON** deve essere premuto quando si passa da un dispositivo di comunicazione con il pod a un altro.

(OmnipodEros-omnipod-settings)=

## Impostazioni Omnipod

Le impostazioni del driver Omnipod sono configurabili dal **menu a tendina** in alto a sinistra in **Generatore di configurazione**➜**Micro**➜**Omnipod**➜**Ingranaggio impostazioni (2)** selezionando il **pulsante radio (1)** intitolato **Omnipod**. Selezionando la **casella di controllo (3)** accanto all'**Ingranaggio impostazioni (2)** verrà visualizzato il menu Omnipod come scheda nell'interfaccia AAPS intitolata **OMNIPOD** o **POD**. In questa documentazione ci si riferirà ad essa come la scheda **Omnipod (POD)**.

![Impostazioni_Omnipod_1](../images/omnipod/Omnipod_Settings_1.png)

**NOTA:** Un modo più rapido per accedere alle **impostazioni Omnipod** è tramite il **menu a 3 punti (1)** nell'angolo in alto a destra della scheda **Omnipod (POD)** e selezionando **Preferenze Omnipod (2)** dal menu a discesa.

![Conferma_Allarmi_2](../images/omnipod/Omnipod_Settings_2.png)

I gruppi di impostazioni sono elencati di seguito; è possibile abilitarli o disabilitarli tramite un interruttore a levetta per la maggior parte delle voci descritte di seguito:

![Conferma_Allarmi_2](../images/omnipod/Omnipod_Settings_3.png)

*NOTA: Un asterisco (\*) indica che l'impostazione predefinita è abilitata.*

### RileyLink

Consente la scansione di un dispositivo di comunicazione con il pod. Il driver Omnipod non può selezionare più di un dispositivo di comunicazione con il pod alla volta.

- **Mostra livello batteria riportato da OrangeLink/EmaLink/DiaLink:** Riporta il livello di batteria effettivo del OrangeLink/EmaLink/Dialink. È **fortemente consigliato** che tutti gli utenti di OrangeLink/EmaLink/DiaLink abilitino questa impostazione.

- NON funziona con il RileyLink originale.
- Potrebbe non funzionare con le alternative al RileyLink.
- Abilitato - Riporta il livello di batteria corrente per i dispositivi di comunicazione con il pod supportati.
- Disabilitato - Riporta un valore n/d.

- **Abilita registrazione cambio batteria nelle Azioni:** Nel menu Azioni, il pulsante di cambio batteria è abilitato SE si è abilitata questa impostazione E quella di segnalazione della batteria sopra.  Alcuni dispositivi di comunicazione con il pod ora dispongono della possibilità di utilizzare batterie ordinarie sostituibili.  Questa opzione consente di registrare la sostituzione e reimpostare i timer di vita della batteria.

### Segnali acustici di conferma

Fornisce segnali acustici di conferma dal pod per bolo, basale, SMB e modifiche/erogazioni TBR.

- **\*Segnali acustici bolo abilitati:** Abilita o disabilita i segnali acustici di conferma quando viene erogato un bolo.
- **\*Segnali acustici basale abilitati:** Abilita o disabilita i segnali acustici di conferma quando viene impostata una nuova velocità basale, quella attiva viene annullata o quella corrente viene modificata.
- **\*Segnali acustici SMB abilitati:** Abilita o disabilita i segnali acustici di conferma quando viene erogato un SMB.
- **Segnali acustici TBR abilitati:** Abilita o disabilita i segnali acustici di conferma quando viene impostato o annullato un TBR.

### Notifiche

Fornisce avvisi AAPS e notifiche Nightscout per la scadenza del pod, lo spegnimento e il serbatoio esaurito in base alle unità soglia definite.

*Nota: una notifica AAPS verrà SEMPRE inviata per qualsiasi avviso dopo la comunicazione iniziale con il pod da quando l'avviso è stato attivato. Ignorare la notifica NON ignorerà l'avviso A MENO CHE non sia abilitata la conferma automatica degli avvisi pod. Per ignorare MANUALMENTE l'avviso è necessario visitare la scheda Omnipod (POD) e premere il pulsante CONF. AVVISI.*

- **\*Promemoria scadenza abilitato:** Abilita o disabilita il promemoria di scadenza del pod impostato per attivarsi quando viene raggiunto il numero di ore prima dello spegnimento definito.
- **Ore prima dello spegnimento:** Definisce il numero di ore prima dello spegnimento del pod attivo, che attiverà l'avviso di promemoria scadenza.
- **\*Avviso serbatoio esaurito abilitato:** Abilita o disabilita un avviso quando viene raggiunto il limite di unità residue del serbatoio del pod come definito nel campo Numero di unità.
- **Numero di unità:** Il numero di unità al quale attivare l'avviso di serbatoio esaurito del pod.
- **Conferma automaticamente gli avvisi pod:** Quando abilitata, verrà comunque inviata una notifica, ma immediatamente dopo il primo contatto di comunicazione con il pod da quando l'avviso è stato emesso, verrà automaticamente confermato e l'avviso verrà ignorato.

### Avvisi

Fornisce notifiche AAPS e avvisi sonori del telefono quando è incerto se gli eventi TBR, SMB o bolo siano stati completati con successo.

*NOTA: Queste sono solo notifiche, non vengono emessi segnali acustici.*

- **Suono per notifiche TBR incerte abilitato:** Abilita o disabilita questa impostazione per attivare un avviso sonoro e una notifica visiva quando AAPS non è sicuro se un TBR sia stato impostato con successo.
- **\*Suono per notifiche SMB incerte abilitato:** Abilita o disabilita questa impostazione per attivare un avviso sonoro e una notifica visiva quando AAPS non è sicuro se un SMB sia stato erogato con successo.
- **\*Suono per notifiche bolo incerte abilitato:** Abilita o disabilita questa impostazione per attivare un avviso sonoro e una notifica visiva quando AAPS non è sicuro se un bolo sia stato erogato con successo.

### Altro

Fornisce impostazioni avanzate per assistere nel debugging.

- **Mostra pulsante Sospendi erogazione nella scheda Omnipod:** Nascondi o visualizza il pulsante di sospensione dell'erogazione nella scheda **Omnipod (POD)**.
- **Mostra pulsante Log pulse nel menu Gestione pod:** Nascondi o visualizza il pulsante del log pulse nel menu **Gestione pod**.
- **Mostra pulsante Statistiche RileyLink nel menu Gestione pod:** Nascondi o visualizza il pulsante Statistiche RileyLink nel menu **Gestione pod**.
- **\*Rilevamento DST/fuso orario abilitato:** consente di rilevare automaticamente le modifiche del fuso orario se il telefono viene utilizzato in un'area in cui è in vigore l'ora legale.

### Switching or Removing an Active Pod Communication Device (RileyLink)

Con molti modelli alternativi al RileyLink originale disponibili (come OrangeLink o EmaLink) o la necessità di avere versioni multiple/di backup dello stesso dispositivo di comunicazione con il pod (RileyLink), diventa necessario cambiare o rimuovere il dispositivo di comunicazione con il pod (RileyLink) selezionato dalla configurazione delle impostazioni Omnipod.

I passi seguenti mostrano come **Rimuovere** un dispositivo di comunicazione con il pod (RileyLink) esistente e come **Aggiungerne** uno nuovo.  Eseguire sia i passaggi **Rimuovi** che **Aggiungi** permette di cambiare il dispositivo.

1. Navigare nella scheda **Omnipod (POD)** e cliccare sul pulsante **GEST. POD (1)**, poi cliccare su **Attiva pod (2)**.

   > ![Impostazioni_Omnipod_2](../images/omnipod/Omnipod_Settings_2.png) ![Configurazione_RileyLink_2](../images/omnipod/RileyLink_Setup_2.png)

### Cambio o rimozione di un dispositivo di comunicazione con il pod attivo (RileyLink)

Questo processo mostra come aggiungere un nuovo dispositivo di comunicazione con il pod alle impostazioni del driver Omnipod.

1. In **Configurazione RileyLink** premere il testo **Indirizzo MAC (1)** per aprire il menu **Selezione RileyLink**.

   > ![Configurazione_RileyLink_Rimuovi_1](../images/omnipod/RileyLink_Setup_Remove_1.png)

2. Nel menu **Selezione RileyLink** premere il pulsante **Rimuovi (2)** per rimuovere **il RileyLink attualmente selezionato (3)**.

   > ![Configurazione_RileyLink_Rimuovi_2](../images/omnipod/RileyLink_Setup_Remove_2.png)

3. Alla richiesta di conferma premere **Sì (4)** per confermare la rimozione del dispositivo.

   > ![Configurazione_RileyLink_Rimuovi_3](../images/omnipod/RileyLink_Setup_Remove_3.png)

4. Si torna al menu **Impostazioni Omnipod** dove in **Configurazione RileyLink** il dispositivo risulterà ora **Non impostato (5)**.  Congratulazioni, il dispositivo di comunicazione con il pod selezionato è stato rimosso con successo.

   > ![Configurazione_RileyLink_Rimuovi_4](../images/omnipod/RileyLink_Setup_Remove_4.png)

### Rimozione del dispositivo di comunicazione con il pod attualmente selezionato (RileyLink)

Questo processo mostra come rimuovere il dispositivo di comunicazione con il pod attualmente selezionato (RileyLink) dalle impostazioni del driver Omnipod.

1. In **Configurazione RileyLink** premere il testo **Non impostato (1)** per aprire il menu **Selezione RileyLink**.

   > ![Configurazione_RileyLink_Aggiungi_1](../images/omnipod/RileyLink_Setup_Add_1.png)

2. Premere il pulsante **Scansione (2)** per iniziare la scansione di tutti i dispositivi Bluetooth disponibili.

   > ![Configurazione_RileyLink_Aggiungi_2](../images/omnipod/RileyLink_Setup_Add_2.png)

3. Selezionare **il proprio RileyLink (3)** dall'elenco dei dispositivi disponibili e si tornerà al menu **Impostazioni Omnipod** che mostra l'**Indirizzo MAC (4)** del dispositivo appena selezionato.  Congratulazioni, il dispositivo di comunicazione con il pod è stato selezionato con successo.

   > ![Configurazione_RileyLink_Aggiungi_3](../images/omnipod/RileyLink_Setup_Add_3.png) ![Configurazione_RileyLink_Aggiungi_4](../images/omnipod/RileyLink_Setup_Add_4.png)

## Scheda Azioni (ACT)

Questa scheda è ben documentata nella documentazione principale di AAPS, ma ci sono alcuni elementi specifici per come il pod Omnipod differisce dai microinfusori con tubo, specialmente dopo i processi di applicazione di un nuovo pod.

1. Andare alla scheda **Azioni (ACT)** nell'interfaccia principale di AAPS.
2. Nella sezione **Careportal (1)**, i seguenti 3 campi avranno la loro **età reimpostata** a 0 giorni e 0 ore **dopo ogni cambio pod**: **Insulina** e **Cannula**. Questo avviene per la costruzione e il funzionamento del microinfusore Omnipod. La **batteria del microinfusore** e il **serbatoio dell'insulina** sono contenuti all'interno di ogni pod. Poiché il pod inserisce la cannula direttamente nella pelle nel sito di applicazione del pod, non viene usato un tubo tradizionale nei microinfusori Omnipod. *Pertanto dopo un cambio pod, l'età di ciascuno di questi valori verrà reimpostata automaticamente a zero.* **L'età della batteria del microinfusore** non viene riportata poiché la batteria nel pod durerà sempre più della vita del pod (massimo 80 ore).

> ![Tab_Azioni](../images/omnipod/Actions_Tab.png)

### Livelli

**Livello insulina**

La segnalazione della quantità di insulina nel pod Omnipod Eros non è precisa.  Questo perché non si sa esattamente quanta insulina è stata inserita nel pod, ma solo che quando vengono emessi 2 segnali acustici durante il riempimento del pod sono state iniettate più di 85 unità. Un pod può contenere un massimo di 200 unità. Anche la preparazione introduce varianza poiché non è un processo esatto.  Con entrambi questi fattori, il driver Omnipod è stato scritto per fornire la migliore approssimazione dell'insulina rimanente nel serbatoio.

> - **Oltre 50 unità** - Riporta un valore di 50+U quando nel serbatoio sono presenti più di 50 unità.
> - **Sotto 50 unità** - Riporta un valore calcolato approssimativo dell'insulina rimanente nel serbatoio.
> - **SMS** - Restituisce il valore o 50+U per le risposte SMS.
> - **Nightscout** - Carica il valore 50 quando ci sono più di 50 unità su Nightscout (versione 14.07 e precedenti).  Le versioni più recenti riporteranno un valore di 50+ quando ci sono più di 50 unità.

**Livello batteria**

La segnalazione del livello di batteria è un'impostazione che può essere abilitata per restituire il livello di batteria corrente dei dispositivi di comunicazione con il pod, come OrangeLink, EmaLink o DiaLink.  L'hardware RileyLink non è in grado di segnalare il livello di batteria.  Il livello di batteria viene segnalato dopo ogni comunicazione con il pod, quindi durante la carica potrebbe non essere osservato un aumento lineare.  Un aggiornamento manuale aggiornerà il livello di batteria corrente.  Quando un dispositivo di comunicazione con il pod supportato viene disconnesso, verrà riportato un valore dello 0%.

> - **L'hardware RileyLink NON è in grado di segnalare il livello di batteria**
> - **L'impostazione "Mostra livello batteria riportato da OrangeLink/EmaLink/DiaLink" DEVE essere abilitata nelle impostazioni Omnipod per segnalare i valori del livello di batteria**
> - **La segnalazione del livello di batteria funziona SOLO per i dispositivi OrangeLink, EmaLink e DiaLink**
> - **La segnalazione del livello di batteria POTREBBE funzionare per altri dispositivi (escluso RileyLink)**
> - **SMS** - Restituisce il livello di batteria corrente come risposta quando esiste un livello effettivo; un valore n/d non verrà restituito.
> - **Nightscout** - Il livello di batteria viene segnalato quando esiste un livello effettivo; un valore n/d non verrà segnalato.

(OmnipodEros-troubleshooting)=

## Risoluzione dei problemi

### Pod Failures

I pod si guastano occasionalmente a causa di vari problemi, inclusi problemi hardware del pod stesso. Si sconsiglia di segnalarlo a Insulet poiché AAPS non è un caso d'uso approvato. Un elenco dei codici di guasto si trova [qui](https://github.com/openaps/openomni/wiki/Fault-event-codes) per aiutare a determinare la causa.

### Prevenzione dei guasti pod con errore 49

Questo guasto è correlato a uno stato errato del pod per un comando o un errore durante un comando di erogazione di insulina. Si raccomanda agli utenti di passare al client Nightscout in modalità *solo caricamento (Disabilita sincronizzazione)* in **Generatore di configurazione**➜**Generale**➜**NSClient**➜**ingranaggio**➜**Impostazioni avanzate** per prevenire possibili guasti.

### Pump Unreachable Alerts

Si raccomanda di configurare gli avvisi di microinfusore irraggiungibile a **120 minuti** andando nel menu a tre punti in alto a destra, selezionando **Preferenze**➜**Avvisi locali**➜**Soglia microinfusore irraggiungibile [min]** e impostando questo valore a **120**.

(OmnipodEros-import-settings-from-previous-aaps)=
### Importa impostazioni da versioni precedenti di AAPS

Si prega di notare che l'importazione delle impostazioni può importare uno stato pod obsoleto. Di conseguenza, si potrebbe perdere un pod attivo. Si raccomanda pertanto vivamente di **non importare le impostazioni mentre è in corso una sessione pod attiva**.

1. Disattivare la sessione pod. Verificare di non avere una sessione pod attiva.
2. Esportare le impostazioni e conservarne una copia in un posto sicuro.
3. Disinstallare la versione precedente di AAPS e riavviare il telefono.
4. Installare la nuova versione di AAPS e verificare di non avere una sessione pod attiva.
5. Importare le impostazioni e attivare il nuovo pod.

### Avvisi del driver Omnipod

Si prega di notare che il driver Omnipod presenta una varietà di avvisi univoci nella **scheda Panoramica**, la maggior parte dei quali sono informativi e possono essere ignorati, mentre alcuni forniscono all'utente un'azione da intraprendere per risolvere la causa dell'avviso attivato. Di seguito è riportato un riepilogo dei principali avvisi che si potrebbero incontrare:

#### Nessun pod attivo

Nessuna sessione pod attiva rilevata. Questo avviso può essere temporaneamente ignorato premendo **POSTICIPA**, ma continuerà ad attivarsi finché non viene attivato un nuovo pod. Una volta attivato, questo avviso viene automaticamente silenziato.

#### Pod sospeso

Avviso informativo che il pod è stato sospeso.

#### Impostazione del profilo basale non riuscita. L'erogazione potrebbe essere sospesa! Aggiornare manualmente lo stato del pod dalla scheda Omnipod e riprendere l'erogazione se necessario..

Avviso informativo che l'impostazione del profilo basale del pod non è riuscita; sarà necessario premere *Aggiorna* nella scheda Omnipod.

#### Impossibile verificare se il bolo SMB ha avuto successo. Se si è certi che il bolo non sia riuscito, è necessario eliminare manualmente la voce SMB dai Trattamenti.

Avviso che il successo del bolo SMB non ha potuto essere verificato; sarà necessario verificare il campo *Ultimo bolo* nella scheda Omnipod per vedere se il bolo SMB ha avuto successo e, in caso contrario, rimuovere la voce dalla scheda Trattamenti.

#### Incerto se "bolo/TBR/SMB task" completato, verificare manualmente se è andato a buon fine.

A causa del modo in cui il RileyLink e l'Omnipod comunicano, possono verificarsi situazioni in cui è *incerto* se un comando è stato elaborato con successo. Era necessario informare l'utente di questa incertezza.

Di seguito sono riportati alcuni esempi di quando può verificarsi una notifica di incertezza.

- **Boli** - I boli incerti non possono essere verificati automaticamente. La notifica rimarrà fino al prossimo bolo, ma un aggiornamento manuale del pod cancellerà il messaggio. *Per impostazione predefinita, i segnali acustici di avviso sono abilitati per questo tipo di notifica poiché l'utente dovrà verificarli manualmente.*
- **TBR, stati pod, cambi profilo, cambi orario** - un aggiornamento manuale del pod cancellerà il messaggio. Per impostazione predefinita, i segnali acustici di avviso sono disabilitati per questo tipo di notifica.
- **Deviazione oraria pod -** Quando l'ora sul pod e l'ora del telefono si discostano troppo, diventa difficile per il loop AAPS funzionare e fare previsioni e raccomandazioni di dosaggio accurate. Se la deviazione oraria tra il pod e il telefono è superiore a 5 minuti, AAPS segnalerà che il pod è in stato Sospeso con un messaggio GESTISCI CAMBIO ORA. Nella parte inferiore della scheda Omnipod (POD) apparirà un'icona **Imposta ora** aggiuntiva. Cliccando su Imposta ora si sincronizzerà l'ora del pod con quella del telefono e poi si potrà cliccare il pulsante RIPRENDI EROGAZIONE per continuare le normali operazioni del pod.

## Migliori pratiche

(OmnipodEros-optimal-omnipod-and-rileylink-positioning)=

### Posizionamento ottimale di Omnipod e RileyLink

L'antenna usata nel RileyLink per comunicare con un pod Omnipod è un'antenna a spirale elicoidale a 433 MHz. Per via delle sue proprietà costruttive, irradia un segnale omnidirezionale come una ciambella tridimensionale con l'asse z che rappresenta l'antenna verticale. Ciò significa che ci sono posizioni ottimali per il RileyLink, specialmente durante le procedure di attivazione e disattivazione del pod.

![Rappresentazione_Toro](../images/omnipod/Toroid_w_CS.png)

> *(Fig 1. Rappresentazione grafica dell'antenna a spirale elicoidale in uno schema omnidirezionale*)

Per motivi di sicurezza, l'*attivazione* del pod deve essere eseguita a una distanza *più ravvicinata (~30 cm o meno)* rispetto ad altre operazioni come somministrare un bolo, impostare un TBR o semplicemente aggiornare lo stato del pod. Per la natura della trasmissione del segnale dall'antenna RileyLink, NON si raccomanda di posizionare il pod direttamente sopra o accanto al RileyLink.

L'immagine sottostante mostra il modo ottimale di posizionare il RileyLink durante le procedure di attivazione e disattivazione del pod. Il pod potrebbe attivarsi in altre posizioni, ma si avrà il maggior successo usando la posizione nell'immagine sottostante.

*Nota: Se dopo aver posizionato ottimalmente il pod e il RileyLink la comunicazione non riesce, ciò potrebbe essere dovuto a una batteria scarica che riduce il raggio di trasmissione dell'antenna RileyLink. Per evitare questo problema, assicurarsi che il RileyLink sia adeguatamente carico o collegato direttamente a un cavo di ricarica durante questo processo.*

![Pod_Omnipod_e_Posizione_RileyLink](../images/omnipod/Omnipod_pod_and_RileyLink_Position.png)

## Dove ottenere aiuto per il driver Omnipod

Tutto il lavoro di sviluppo per il driver Omnipod è svolto dalla comunità su base volontaria; si chiede di essere considerati e di utilizzare le seguenti linee guida quando si richiede assistenza:

- **Livello 0:** Leggere la sezione pertinente di questa documentazione per assicurarsi di capire come dovrebbe funzionare la funzionalità con cui si sta riscontrando difficoltà.
- **Livello 1:** Se si riscontrano ancora problemi che non si riesce a risolvere usando questo documento, andare al canale *#androidaps* su **Discord** usando [questo link di invito](https://discord.gg/4fQUWHZ4Mw).
- **Livello 2:** Cercare i problemi esistenti per vedere se il problema è già stato segnalato; in caso contrario, creare un nuovo [problema](https://github.com/nightscout/AndroidAPS/issues) e allegare i propri [file di log](../GettingHelp/AccessingLogFiles.md).
- **Siate pazienti - la maggior parte dei membri della nostra comunità è composta da volontari di buona volontà, e la risoluzione dei problemi richiede spesso tempo e pazienza sia dagli utenti che dagli sviluppatori.**
