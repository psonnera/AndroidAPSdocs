# Daily Life - Pumps
## Cambio dei set di infusione: serbatoi di insulina e cannule

The procedure described below is for tubed pumps only and does not apply to patch pumps like Omnipod, Medtrum Nano, Accu-Chek Solo etc. La procedura descritta di seguito è applicabile solo ai microinfusori con tubo e non si applica ai microinfusori patch come Omnipod, Medtrum Nano, Accu-Chek Solo, ecc. Questa procedura viene talvolta chiamata "cambio del set", dove un cambio "completo" include il serbatoio di insulina e la cannula, e un cambio "parziale" si riferisce solo alla sostituzione della cannula.

Le sostituzioni fisiche della cartuccia/serbatoio non possono essere eseguite tramite **AAPS** e devono essere effettuate direttamente sul microinfusore. È necessario registrarle manualmente in **AAPS** una volta completate.

### Guida per la sostituzione del serbatoio e della cannula del microinfusore

1)  In **AAPS**, disconnettere il microinfusore: premere a lungo l'icona "Open Loop"/"Closed Loop" nella schermata principale di **AAPS** e selezionare "Disconnetti microinfusore - 1 ora". L'icona del microinfusore diventerà grigia, indicando che il microinfusore è disconnesso.

2)  Sostituire fisicamente il serbatoio di insulina: disconnettere fisicamente il microinfusore dal corpo e sostituire il serbatoio/la cartuccia e la cannula seguendo le istruzioni del produttore.

3)  Adescare/riempire il tubo e la cannula: questa operazione può essere eseguita direttamente sul microinfusore. Assicurarsi di eliminare eventuali bolle d'aria nel tubo.

4)  Collegare la nuova cannula al corpo. Una volta inserita la cannula e rimosso l'ago, la cannula collegata presenta un piccolo spazio d'aria che deve essere anch'esso adescato. Per comunicarlo in **AAPS** e adescare il sito: selezionare il pulsante PRIME/FILL nella scheda azioni di **AAPS** e spuntare "Cambio sito microinfusore" e/o "Cambio cartuccia insulina" secondo le necessità. Premere quindi la quantità predefinita di insulina per l'adescamento della cannula (di solito circa 0,3 U, ma verificare il valore corretto per la propria cannula) e selezionare "OK". Leggere il messaggio di riepilogo e confermare l'esecuzione dell'adescamento toccando "OK".

5)  Riconnettere il microinfusore in **AAPS**: premere il simbolo del microinfusore grigio disconnesso e selezionare "Riconnetti microinfusore" per riprendere il loop.

### Informazioni utili riguardanti le sostituzioni di insulina/cannula

●   La registrazione di un cambio del sito del microinfusore reimposta Autosens al 100%. Reimposta anche le spie di stato e le età della cannula/insulina corrispondenti nella schermata principale di **AAPS**.

●   È possibile impostare/regolare la quantità di adescamento predefinita in Preferenze > Panoramica > Quantità standard insulina per adescamento. Consultare il foglio illustrativo nella confezione della cannula per conoscere quante unità (a seconda della lunghezza dell'ago e del tubo) devono essere utilizzate per l'adescamento.

●   L'insulina somministrata tramite la funzione di adescamento non viene presa in considerazione da **AAPS** nel calcolo dell'insulina attiva (IOB), ed è indicata nel menu trattamenti di **AAPS** come "Prime".

●   Qualsiasi bolo erogato dal microinfusore durante la disconnessione non verrà preso in considerazione da **AAPS**. Se si eroga un bolo direttamente dal microinfusore mentre **AAPS** è disconnesso, una volta riconnesso è possibile comunicare questa insulina (senza erogarla) nella scheda "insulina" (vedere il link sottostante "per comunicare l'insulina somministrata senza effettuare un bolo" per maggiori dettagli).

### Problemi con la cannula, il sito di infusione, il tubo e/o il microinfusore

Se si è certi di non aver ricevuto insulina per un certo periodo, nonostante **AAPS** registri che è stata somministrata, e si sa esattamente quando è iniziato il problema (_es._ si rimuove la cannula e si vede che era piegata durante l'inserimento), è possibile correggere in **AAPS**, tenendo presente che l'insulina potrebbe in realtà essere stata somministrata ma potrebbe agire lentamente per qualche motivo.

```{admonition} Caution - Risk of Hypoglycemia
:class: danger
Eliminare le somministrazioni di insulina da **AAPS** con ESTREMA cautela, nel caso in cui l'insulina _sia_ stata effettivamente somministrata, e monitorare attentamente la glicemia nelle successive 24 ore.
```

Per rimuovere boli e SMB che si sa non essere stati somministrati, aprire la scheda Trattamenti ed eliminare in modo conservativo le informazioni sui boli registrati > carboidrati e bolo a partire dal momento in cui si è verificato l'incidente. In questo modo si correggerà il valore di "insulina attiva" (IOB) fondamentale per i calcoli di **AAPS**; tornando alla schermata principale si vedrà che l'IOB è ora diminuito. Tenere presente che non è possibile eliminare la basale che **AAPS** calcola come somministrata, che verrà quindi ancora presa in considerazione da **AAPS**.

In casi meno evidenti di problemi di somministrazione di insulina _es._ perdite, occlusioni o tunneling, in cui non si è certi di quando sia iniziato il problema o si ritiene che parte dell'insulina sia stata somministrata, è necessario prestare attenzione. È possibile rilevare questi problemi "annusando" l'insulina, vedendo un cerotto bagnato, riscontrando valori di glicemia elevati o ricevendo un allarme. Poiché non si sa mai quanta insulina è entrata nella pelle (che potrebbe iniziare ad agire dopo un po'), sarà difficile determinare la quantità corretta di insulina da sottrarre dall'attuale valore di "insulina attiva" (IOB). Una strategia consiste nel mettere in pausa il loop per 5 ore (o per la durata specifica dell'azione insulinica) dopo aver risolto il problema di somministrazione dell'insulina, e poi riprendere il loop. In questo modo si garantirà che l'IOB sia corretto quando si riavvia il loop.

## Disconnessione del microinfusore per doccia o attività

Se si rimuove il microinfusore per fare la doccia, il bagno, nuotare, praticare sport da contatto o altre attività, è necessario comunicarlo ad **AAPS** affinché non venga erogata insulina, per mantenere corretto l'IOB. Il microinfusore può essere disconnesso utilizzando l'icona di stato del loop nella schermata principale di **AAPS**.

Poiché non si riceve insulina mentre il microinfusore è disconnesso, è consigliabile riconnettersi ogni due ore per compensare la basale mancante. È possibile farlo collegandosi ed erogando i valori di basale mancanti (_es._ delle ultime due ore) prima di disconnettersi nuovamente. Questo dovrebbe aiutare a evitare una grave carenza di insulina che potrebbe portare a chetoacidosi diabetica (DKA). Se è scomodo riconnettersi durante l'attività (il sito della cannula è coperto da una muta, _ecc._), considerare un'iniezione con la penna. Questa iniezione manuale può essere registrata in **AAPS** e non deve necessariamente essere registrata al momento dell'iniezione (annotare l'orario dell'iniezione), poiché è possibile comunicare l'insulina e retrodatare l'orario effettivo di somministrazione quando si riconnette il microinfusore.

## Per comunicare l'insulina somministrata senza effettuare un bolo

Per comunicare ad **AAPS** l'insulina erogata dal microinfusore mentre **AAPS** era disconnesso, o da iniezioni con penna: selezionare la scheda "insulina", inserire la quantità in unità e selezionare "non somministrare bolo, registra solo". Selezionando questa opzione, apparirà una scheda "offset temporale". Se l'iniezione è stata somministrata di recente si può ignorarla, ma se il bolo è stato somministrato qualche tempo fa, è possibile aggiungere un segno meno davanti al tempo (_es._ - 30 min) per registrare l'orario effettivo del bolo. **AAPS** terrà quindi conto della durata dell'azione insulinica e calcolerà di conseguenza l'insulina residua ancora nel sistema.

Se si utilizza **AAPS** come caregiver, è possibile disconnettere (e riconnettere) il microinfusore da remoto molto facilmente tramite [comando SMS](../RemoteFeatures/SMSCommands.md) usando comandi come "pump disconnect 120" e "pump connect 120". La durata della disconnessione remota va da 1 a 120 minuti (nell'esempio sono 120 minuti). Questo è molto utile se lo smartphone **AAPS** è difficile da raggiungere, nascosto nella cintura del microinfusore di un bambino che corre verso la piscina, o tenuto stretto (o in uso) da un adolescente.

## Reconnecting the pump after activity

Dopo una lunga disconnessione (1-2 ore), è abbastanza comune che **AAPS** calcoli un IOB negativo. Quando si riconnette il microinfusore, a seconda delle preferenze/livello di glicemia attuale/cibo pianificato o attività successiva, è possibile:

a) Semplicemente riconnettere il microinfusore in **AAPS** (dal grigio al verde, per il loop chiuso) e lasciare che **AAPS** ricomincia a somministrare insulina

_oppure_

b) Se si desidera essere più aggressivi (ad esempio, si prevede un'iperglicemia), è possibile accedere al calcolatore e calcolare un bolo per zero carboidrati, per somministrare immediatamente l'insulina mancante calcolata come bolo.


La strategia preferita è altamente personale ed è meglio determinata tramite tentativi.    
