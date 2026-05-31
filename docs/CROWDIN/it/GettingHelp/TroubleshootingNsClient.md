(Troubleshooting-NSClient-troubleshooting-nsclient)=
# Risoluzione dei problemi di NSClient

NSClient dipende da una comunicazione stabile con Nightscout. Una connessione instabile porta a errori di sincronizzazione e un elevato consumo di dati.

Se nessuno ti segue su Nightscout, puoi scegliere di mettere in pausa NSClient per risparmiare la batteria, oppure puoi configurare NSClient in modo che si connetta solo quando sei su Wi-Fi e/o durante la ricarica.

* Come rilevare una connessione instabile?

Vai alla scheda NSClient in AAPS e osserva il log. Il comportamento atteso è ricevere un PING ogni ~30 secondi e quasi nessun messaggio di riconnessione. Se vedi molte riconnessioni, c'è un problema.

Dalla versione 2.0 di AAPS, quando viene rilevato questo comportamento, NSClient viene messo in pausa per 15 minuti e viene visualizzato il messaggio "NSClient malfunzionamento" nella schermata principale.

* Riavvio

Il primo passo da provare è riavviare sia Nightscout che il telefono, per verificare se il problema è permanente.

Se il tuo Nightscout è ospitato su Heroku, puoi riavviarlo così: accedi a Heroku, clicca sul nome della tua app Nightscout, clicca sul menu 'Altro', poi 'Riavvia tutti i dynos'.

Per altri host, segui la documentazione del tuo provider.

* Problemi con il telefono

Android potrebbe mettere il telefono in modalità sleep. Verifica di avere un'eccezione per AAPS nelle opzioni di risparmio energetico del tuo telefono, per consentirgli di funzionare sempre in background.

Controlla nuovamente NSClient quando sei in una posizione con un segnale di rete forte.

Prova un altro telefono.

* Nightscout

Se il tuo sito è ospitato su Azure, molte persone hanno riscontrato che i problemi di connessione sono migliorati dopo il passaggio a Heroku.

Una soluzione alternativa ai problemi di connessione su Azure è impostare nelle impostazioni dell'applicazione il protocollo HTTP su 2.0 e i Websocket su ON.

* Nessuna lettura glicemica da Nightscout

Se AAPS si connette correttamente a Nightscout ma la glicemia viene visualizzata come N/A. Vai alla scheda NSCLIENT, premi il menu a 3 punti in alto a destra, clicca su Preferenze NSClient -> Sincronizzazione e attiva "Ricevi/reintegra dati CGM".

* Se si ottiene ancora un errore...

Controlla la dimensione del tuo database in MongoDB (o tramite il plugin della dimensione del database in Nightscout). Se stai usando il piano gratuito di MongoDB, 496 MB significa che è pieno e deve essere ripulito. [Segui queste istruzioni di Nightscout per controllare la dimensione del database e cancellare i dati](https://nightscout.github.io/troubleshoot/troublehoot/#database-full).

Prima di cancellare i dati dal database, e se non l'hai già fatto, considera di donare i tuoi dati AAPS al progetto Open Humans (per la ricerca). Le istruzioni si trovano nella [pagina di configurazione di OpenHumans](../SupportingAaps/OpenHumans.md).
