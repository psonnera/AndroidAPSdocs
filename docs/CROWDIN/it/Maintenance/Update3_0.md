# Controlli necessari dopo l'aggiornamento ad AAPS 3.0

* **La versione minima di Android è ora 9.0.**
* **I dati non vengono migrati al nuovo database.**

  Non lamentarti, il cambiamento è così enorme che semplicemente non è possibile. Pertanto dopo l'aggiornamento IOB, COB, trattamenti ecc. saranno azzerati. Devi creare un nuovo [cambio di profilo](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md) e iniziare con IOB e COB pari a zero.

  Pianifica attentamente l'aggiornamento!!! Il momento migliore è quando non c'è insulina attiva e carboidrati.

* Consulta le [Note di Rilascio](../Maintenance/ReleaseNotes.md) per i dettagli sulle funzionalità nuove e modificate.


## Controlla le automazioni

* Sono state introdotte nuove restrizioni. Controlla le tue automazioni, in particolare se le condizioni sono ancora valide.
* Se manca una delle condizioni, devi aggiungerla di nuovo.
* Le automazioni in rosso contengono azioni non valide; modificale e ripristinale a valori validi.

  Esempio: Prima era consentito un cambio di profilo al 140%, ma ora è limitato al 130%.

## Controlla le impostazioni di nsclient e imposta le complicazioni di sincronizzazione

* L'implementazione del plugin nsclient è cambiata completamente.
* Vai alla scheda nsclient e apri le impostazioni nel menu a destra. È ora disponibile una nuova preferenza "Sincronizzazione".
* Ora puoi fare una selezione dettagliata di quali elementi devono essere sincronizzati con il tuo sito Nightscout.

(Update3_0-nightscout-profile-cannot-be-pushed)=
## Il profilo Nightscout non può essere inviato
* Il profilo Nightscout è sparito, riposa in pace!
* Per copiare il tuo profilo Nightscout attuale in un profilo locale, vai alla pagina dei trattamenti (ora da aprire nel menu a destra).
* Cerca un cambio di profilo al 100% e premi clona.
* Viene aggiunto un nuovo profilo locale, valido dalla data corrente.
* Per aggiornare il profilo dal lato NS usa "Clona" (record!!, non profilo) e salva le modifiche. Dovresti vedere "Profilo valido dal:" impostato alla data corrente.

(Update3_0-reset-master-password)=
## Reimposta la password master
* Ora puoi reimpostare la tua password master nel caso in cui l'hai dimenticata.
* Devi aggiungere un file denominato `PasswordReset` nella directory `/AAPS/extra` nel filesystem del tuo telefono.
* Riavvia AAPS.
* La nuova password sarà il numero di serie del tuo microinfusore attivo.
* Per Dash: il numero di serie è sempre 4241.
* Per EROS è anche elencato nella scheda POD come "Numero di sequenza".

## Warning signal beneath BG

A partire da Android 3.0, potresti ricevere un segnale di avviso sotto il numero della glicemia nella schermata principale.

  ![Red BG warning](../images/bg_warn_red.png)

  ![Yellow BG warning](../images/bg_warn_yellow.png)

Per i dettagli vedi la [pagina schermate AAPS](#aaps-screens-bg-warning-sign).

(update30-failure-message-data-from-different-pump)=
## Failure message: Data from different pump

   ![Failure message: Data from different pump](../images/Screen_DifferentPump.png)

Per risolvere questo problema vai al [generatore di configurazione](#Config-Builder-pump). Cambia il microinfusore in virtuale e poi torna al microinfusore reale. Questo reimposterà lo stato del microinfusore.
