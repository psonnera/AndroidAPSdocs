# Suggerimenti per l'uso base di Accu-Chek Combo

## Come garantire il corretto funzionamento

* Portare sempre **lo smartphone con sé**, lasciarlo vicino al letto di notte. Poiché il microinfusore potrebbe trovarsi dietro o sotto il corpo durante il sonno, una posizione più alta (su uno scaffale o una tavola) funziona meglio.
* Assicurarsi sempre che la batteria del microinfusore sia il più carica possibile. Vedere la sezione batteria per suggerimenti sulla batteria.
* Quando possibile, operare il microinfusore solo tramite l'app AAPS. Per facilitare ciò, attivare il blocco tasti sul microinfusore in **IMPOSTAZIONI MICROINFUSORE / BLOCCO TASTI / ON**. Solo quando si cambia la batteria o la cartuccia è necessario utilizzare i tasti del microinfusore.

![Keylock](../images/combo/combo-tips-keylock.png)

## Microinfusore non raggiungibile. Cosa fare?

### Attivare l'allarme microinfusore non raggiungibile
* In AAPS, andare a **Impostazioni / Allarmi locali** e attivare **allarme quando il microinfusore non è raggiungibile** e impostare **limite microinfusore non raggiungibile [min]** a **31** minuti.
* Questo darà abbastanza tempo per non attivare l'allarme quando si lascia la stanza mentre il telefono è rimasto sulla scrivania, ma informa se il microinfusore non può essere raggiunto per un tempo superiore alla durata di una basale temporanea.

### Ripristina la raggiungibilità del microinfusore

* Quando AAPS segnala un allarme **microinfusore non raggiungibile**, prima rilasciare il blocco tasti e **premere qualsiasi tasto sul microinfusore** (ad es. il pulsante "giù"). Non appena il display del microinfusore si è spento, premere **Aggiorna** nella **scheda Combo** in AAPS. Il più delle volte la comunicazione riprende a funzionare.
* Se ciò non aiuta, riavviare lo smartphone. Dopo il riavvio, AAPS verrà riattivato e verrà stabilita una nuova connessione con il microinfusore. Se si utilizza il vecchio driver, ruffy verrà riattivato.

* I test con diversi smartphone hanno mostrato che alcuni smartphone attivano l'errore "microinfusore non raggiungibile" più spesso di altri. Vedere [AAPS Telefoni](#Phones-list-of-tested-phones) per smartphone testati con successo.

### Cause e conseguenze di frequenti errori di comunicazione
* Sui telefoni con **poca memoria** (o con impostazioni di **risparmio energetico aggressivo**), AAPS viene spesso chiuso. È possibile riconoscerlo dal fatto che i pulsanti Bolo e Calcolatore nella schermata principale non vengono mostrati all'apertura di AAPS perché il sistema si sta inizializzando. Ciò può attivare "allarmi microinfusore non raggiungibile" all'avvio. Nel campo **Ultima connessione** della scheda Combo, è possibile verificare quando AAPS ha comunicato l'ultima volta con il microinfusore.

![Pump unreachable](../images/combo/combo-tips-pump-unreachable.png)

![No connection to pump (as shown in the old driver's tab)](../images/combo/combo-tips-no-connection-to-pump.png)

![No connection to pump (as shown in the new driver's tab)](../images/combo/combov2-tips-no-connection-to-pump.png)

* Questo errore può scaricare la batteria del microinfusore più velocemente perché il profilo basale viene letto dal microinfusore quando l'app viene riavviata.
* Aumenta anche la probabilità di causare l'errore che fa rifiutare al microinfusore tutte le connessioni in entrata finché non viene premuto un pulsante sul microinfusore.

## L'annullamento della basale temporanea fallisce
* Occasionalmente, AAPS non riesce ad annullare automaticamente un avviso **BASALE TEMP ANNULLATA**. In questo caso è necessario premere **AGGIORNA** nella **scheda Combo** di AAPS oppure l'allarme sul microinfusore dovrà essere confermato.

## Considerazioni sulla batteria del micro

### Cambio della batteria
* Dopo un allarme di **batteria scarica**, la batteria dovrebbe essere cambiata il prima possibile per avere sempre abbastanza energia per una comunicazione Bluetooth affidabile con lo smartphone, anche se il telefono si trova a una distanza maggiore dal microinfusore.
* Anche dopo un allarme di **batteria scarica**, la batteria potrebbe essere utilizzata per un tempo significativo. Tuttavia, si raccomanda di avere sempre una batteria fresca con sé dopo che è suonato un allarme di "batteria scarica".
* Prima di cambiare la batteria, premere sul simbolo **Loop** nella schermata principale e selezionare **Sospendi loop per 1h**.
* Attendere che il micro comunichi quindi il logo del micro e del bluetooth sullo schermo siano spariti.

![Bluetooth enabled](../images/combo/combo-tips-compo.png)

* Rilasciare il blocco tasti sul microinfusore, mettere il microinfusore in modalità stop, confermare un'eventuale basale temporanea annullata e cambiare la batteria rapidamente.
* Quando si utilizza il vecchio driver, se l'orologio sul microinfusore non ha sopravvissuto al cambio batteria, reimpostare data e ora sul microinfusore esattamente alla data/ora del telefono su cui è in esecuzione AAPS. (Il nuovo driver aggiorna automaticamente data e ora del microinfusore.)
* Poi rimettere il microinfusore in modalità di esecuzione e selezionare **Riprendi** premendo sull'icona **Loop sospeso** nella schermata principale.
* AAPS reimposterà una basale temporanea necessaria con l'arrivo del prossimo valore di glicemia.

(Accu-Chek-Combo-Tips-for-Basic-usage-battery-type-and-causes-of-short-battery-life)=
### Tipo di batteria e cause di breve durata della batteria
* Poiché la comunicazione Bluetooth intensiva consuma molta energia, utilizzare solo **batterie di alta qualità** come Energizer Ultimate Lithium, le "power one" del "grande" kit di servizio Accu-Chek, o se si opta per una batteria ricaricabile, utilizzare batterie Eneloop.

![Energizer](../images/combo/combo-tips-energizer.jpg) ![OnePower](../images/combo/combo-tips-power-one.png)

Gli intervalli per la durata tipica dei diversi tipi di batteria sono i seguenti:
* **Energizer Ultimate Lithium**: da 4 a 7 settimane
* **Power One Alkaline** (Varta) dal kit di servizio: da 2 a 4 settimane
* **Batterie ricaricabili Eneloop** (BK-3MCCE): da 1 a 3 settimane

Se la durata della batteria è significativamente inferiore agli intervalli indicati sopra, verificare le seguenti possibili cause:
* Esistono alcune varianti del cappuccio a vite della batteria del microinfusore Combo che cortocircuitano parzialmente le batterie e le scaricano rapidamente. I cappucci senza questo problema possono essere riconosciuti dai contatti metallici dorati.
* Se l'orologio del microinfusore non "sopravvive" a un rapido cambio di batteria, è probabile che il condensatore che mantiene in funzione l'orologio durante una breve interruzione dell'alimentazione sia rotto. In questo caso, potrebbe essere utile una sostituzione del microinfusore da parte di Roche, che non è un problema durante il periodo di garanzia.
* L'hardware e il software dello smartphone (sistema operativo Android e stack Bluetooth) influiscono anche sulla durata della batteria del microinfusore, anche se i fattori esatti non sono ancora completamente noti. Se se ne ha la possibilità, provare un altro smartphone e confrontare le durate della batteria.

## Bolo esteso, bolo multionda
L'algoritmo OpenAPS non supporta un bolo esteso parallelo o un bolo multionda. Ma un trattamento simile può essere ottenuto con le seguenti alternative:
* Utilizzare i **Carboidrati estesi** quando si inseriscono carboidrati o si usa il Calcolatore inserendo i carboidrati dell'intero pasto e la durata prevista per l'assorbimento dei carboidrati nel sangue. Il sistema calcolerà quindi piccole quantità di carboidrati distribuite uniformemente per l'intera durata, il che farà sì che l'algoritmo fornisca un dosaggio insulinico equivalente controllando continuamente l'aumento/diminuzione complessivo del livello di glicemia. Per un approccio simile al bolo multionda, è anche possibile combinare un bolo immediato più piccolo con i carboidrati estesi.
* Prima di mangiare, nella **scheda Azioni** in AAPS impostare un obiettivo temporaneo **Presto pasto** con target glicemico 80 per diverse ore. La durata dovrebbe essere basata sull'intervallo che si sceglierebbe per un bolo esteso. Questo manterrà il target più basso del solito e quindi aumenterà la quantità di insulina erogata.
* Poi utilizzare il **CALCOLATORE** per inserire i carboidrati totali del pasto, ma non applicare direttamente i valori suggeriti dal calcolatore del bolo. Se si deve erogare un bolo simile al multionda, correggere il dosaggio di insulina verso il basso. A seconda del pasto, l'algoritmo ora deve erogare SMB aggiuntivi o basali temporanee più elevate per contrastare l'aumento della glicemia. Qui, il limite di sicurezza della basale (Max UI/h, IOB basale massimo) dovrebbe essere sperimentato molto attentamente e, se necessario, temporaneamente modificato.

* Se si è tentati di utilizzare semplicemente il bolo esteso o multionda direttamente sul microinfusore, AAPS penalizzerà disabilitando il loop chiuso per le successive sei ore per garantire che non venga calcolato un dosaggio di insulina eccessivo.

![Disabled loop after multiwave bolus](../images/combo/combo-tips-multiwave-bolus.png)

## Allarmi durante l'erogazione del bolo
* Se AAPS rileva che un bolo identico è stato erogato con successo nello stesso minuto, l'erogazione del bolo verrà impedita con lo stesso numero di unità di insulina. Se si desidera davvero fare lo stesso bolo due volte in rapida successione, attendere altri due minuti e poi erogare di nuovo il bolo. Se il primo bolo è stato interrotto o non è stato erogato per altri motivi, è possibile inviare di nuovo il bolo immediatamente da AAPS 2.0.
* L'allarme è un meccanismo di sicurezza che legge la cronologia dei boli del microinfusore prima di inviare un nuovo bolo per calcolare correttamente l'insulina attiva (IOB), anche quando un bolo viene erogato direttamente dal microinfusore. Qui le voci indistinguibili devono essere evitate.

![Double bolus](../images/combo/combo-tips-doppelbolus.png)

* Questo meccanismo è anche responsabile di una seconda causa dell'errore: se durante l'utilizzo del calcolatore del bolo viene erogato un altro bolo tramite il microinfusore e quindi la cronologia dei boli cambia, la base del calcolo del bolo è errata e il bolo viene annullato.

![Canceled bolus](../images/combo/combo-tips-history-changed.png)