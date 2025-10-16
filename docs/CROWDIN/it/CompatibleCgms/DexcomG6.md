# Dexcom G6 e ONE

WARNING --- [BYODA](https://docs.google.com/forms/d/e/1FAIpQLScD76G0Y-BlL4tZljaFkjlwuqhT83QlFM5v6ZEfO7gCU98iJQ/viewform?fbzx=2196386787609383750)--- There are reported issues **AAPS** receiving no BG data when using either BYODA & DiaKEM as its data source. Users are recommended to use [X-Drip+](https://androidaps.readthedocs.io/en/latest/CompatibleCgms/xDrip.html) as **AAPS'** BG data source until this issue has been resolved.

## Prima le basi

-   Segui i consigli generali di igiene del sensore e le impostazioni corrispondente [qui](../CompatibleCgms/GeneralCGMRecommendation.md).

## Suggerimenti generali per il circuito chiuso con G6 e ONE

- I trasmettitori recenti sono chiamati Firefly. I sensori non possono essere riavviati senza rimuovere il trasmettitore, il quale non può essere resettato, e non generano dati grezzi.

- Se stai riavviando i sensori, assicurati di essere pronto a calibrare e tieni d'occhio le variazioni di glicemia.

- È probabile che l'inserimento anticipato dei sensori G6/ONE crei variazioni nei risultati, data la calibrazione di fabbrica di questi sensori. Se usi questa strategia, dovrai probabilmente calibrare il sensore per ottenere risultati migliori.

Leggi di più nell'[articolo](https://www.diabettech.com/artificial-pancreas/diy-looping-and-cgm/) pubblicato da Tim Street su [www.diabettech.com](https://www.diabettech.com).

## Se usi un G6 o ONE con xDrip+

- Se stai usando un trasmettitore recente (Firefly), il riavvio preventivo è **ignorato**.
- Se stai usando un trasmettitore modificato, **non hai bisogno** di impostare i riavvii preventivi.
-   Se stai usando un vecchio trasmettitore ricondizionato, la cosa più sicura da fare è di **disabilitare** il [riavvio preventivo](https://navid200.github.io/xDrip/docs/Preemptive-Restart.html). Però, in questo caso dovrai usare il G6 in [ modalità nativa](https://navid200.github.io/xDrip/docs/Native-Algorithm.html) (che è sconsigliato in quanto disabilita la calibrazione di fabbrica e non filtra le letture rumorose), oppure il sensore si fermerà dopo 10 giorni.
-   I trasmettitori Dexcom G6 e ONE possono essere collegati contemporaneamente al ricevitore Dexcom (o in alternativa al micro t:slim) e a un’app sul telefono.
-   Quando utilizzi xDrip+ collegato al sensore, disinstalla prima l'app Dexcom. **Non è possibile collegare le app xDrip+ e Dexcom al trasmettitore contemporaneamente!**
-   Se hai bisogno di Clarity e vuoi approfittare degli allarmi xDrip+ usa [BYODA](#DexcomG6-if-using-g6-with-build-your-own-dexcom-app) (solo G6) con trasmissione locale (broadcast) verso xDrip+.
-   È anche possibile utilizzare xDrip+ come app di compagno dell'app ufficiale Dexcom, ma si potrebbero verificare ritardi nelle letture di glicemia.
-   Se non lo hai già installato, scarica [xDrip+](https://github.com/NightscoutFoundation/xDrip) e segui le istruzioni sulla pagina [Impostazioni xDrip+](../CompatibleCgms/xDrip.md).
-   Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

- Regola le impostazioni in xDrip+ secondo la pagina [impostazioni xDrip](../CompatibleCgms/xDrip.md)

(DexcomG6-if-using-g6-with-build-your-own-dexcom-app)=
## Se usi un G6 con Build Your Own Dexcom App

-   [Costruisci la tua app Dexcom](https://docs.google.com/forms/d/e/1FAIpQLScD76G0Y-BlL4tZljaFkjlwuqhT83QlFM5v6ZEfO7gCU98iJQ/viewform?fbzx=2196386787609383750) (BYODA) supporta la trasmissione locale su AAPS e/o xDrip+ (non per i sensori G5/ONE/G7!)

![Opzioni broadcast BYODA](../images/BYODA.png)

-   Questa app ti permette di utilizzare il tuo Dexcom G6 con qualsiasi smartphone Android.
-   Disinstalla l'app Dexcom originale o l'app Dexcom patchata se hai usato una di quelle precedentemente (**non fermare** il sensore attualmente in esecuzione)
-   Installa l'apk scaricato
-   Inserisci il codice del sensore e il numero di serie del trasmettitore nell'app patchata.
-   Nelle impostazioni del telefono vai alle app > Dexcom G6 > autorizzazioni > autorizzazioni aggiuntive e premi 'Accedi a l'app Dexcom'.
-   Dopo poco tempo, l'app BYODA dovrebbe collegarsi al trasmettitore.

### Impostazioni per AAPS

-   Seleziona BYODA in [Configuratore Strutturale, Origine BG](#Config-Builder-bg-source).

-   Se non ricevi alcun valore, seleziona qualsiasi altra origine BG, poi ri-seleziona 'BYODA' per stabilire la connessione tra AAPS e BYODA.

### Impostazioni per xDrip+

-   Seleziona '640G/Eversense' come sorgente dati.
-   Dovrai (forse) eseguire Il comando 'Inizializza sensore' in xDrip+ per ricevere i valori. Questo non influenzerà il tuo sensore, che è controllato da BYODA.


(DexcomG6-troubleshooting-g6)=
## Risoluzione dei problemi G6 e ONE

### Risoluzione problemi specifici di Dexcom G6/ONE

-   Scorri verso il basso per la **risoluzione dei problemi** [qui](https://navid200.github.io/xDrip/docs/Dexcom_page.html).

### Risoluzione generale dei problemi

Il consigli generali per i sensori si trovano [qui](#general-cgm-troubleshooting).

### Nuovo trasmettitore con un sensore già avviato

Se ti capita di dovere cambiare il trasmettitore con un sensore già avviato, puoi provare a rimuovere il trasmettitore senza danneggiare il guscio del sensore. Vedi il video [qui](https://navid200.github.io/xDrip/docs/Remove-transmitter.html). Se scegli [questa soluzione](https://youtu.be/tx-kTsrkNUM) devi stare attento a evitare [di danneggiare i contatti del sensore](https://navid200.github.io/xDrip/docs/Petroleum-jelly-in-Dexcom-G6-Sensor.html) con la striscia.
