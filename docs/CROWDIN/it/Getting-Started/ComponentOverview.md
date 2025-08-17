# Panoramica Dei Componenti

**AAPS** non è solo un'applicazione (costruita da te), ma è uno dei diversi moduli del sistema a circuito chiuso. Prima di decidere i componenti, è una buona idea dare un'occhiata alla documentazione dei componenti.

![Panoramica dei componenti](../images/modules.png)

```{admonition} IMPORTANT SAFETY NOTICE
:class: important

La fondazione delle funzionalità di sicurezza **AAPS** discusse in questa documentazione è basata sulle caratteristiche di sicurezza del materiale utilizzato per costruire il sistema. Per chiudere un circuito di dosaggio automatizzato di insulina, è fondamentale che utilizzi solo un microinfusore di insulina e un sistema di monitoraggio continuo del glucosio che siano testati, pienamente funzionanti e approvati dalle istanze ufficiali del tuo paese. Le modifiche materiale o software a questi componenti possono causare un dosaggio inatteso di insulina, causando un rischio significativo per l'utente. Se trovate o ottenete dei microinfusori di insulina o dei ricevitori di sistemi di monitoraggio continuo del glucosio rotti, modificati o autoprodotti , **non utilizzateli** per creare un sistema **AAPS**.

Inoltre, è altrettanto importante utilizzare solo le forniture originali, come gli inseritori, cannule e contenitori per insulina approvati dal produttore per l’uso con la pompa o il sistema di monitoraggio continuo del glucosio. Usare forniture non testate o modificate può causare imprecisione del sistema di monitoraggio continuo del glucosio e errori di dosaggio di insulina. L'insulina è altamente pericolosa quando dosata incorettamente - non giocare con la vostra vita hackerando le forniture.

Ultimo ma non meno importante, non devi assumere inibitori SGLT-2 (Gliflozine) in quanto abbassano incalcolabilmente i livelli di zucchero nel sangue. La combinazione con un sistema che abbassa la basale per aumentare la glicemia è particolarmente pericolosa in quanto a causa delle Gliflozine questo aumento della glicemia potrebbe non accadere e può verificarsi uno stato pericoloso di mancanza di insulina. [Maggiori informazioni qui](#PreparingForAaps-no-sglt-2-inhibitors).
```

## Moduli Necessari

### Buon algoritmo individuale di dosaggio per la terapia del diabete

Anche se non è qualcosa da creare o da comprare, questo è il 'modulo' che probabilmente viene più spesso sottovalutato ma è essenziale. Quando lasci un algoritmo aiutare a gestire il diabete, devi conoscere le impostazioni giuste per non commettere gravi errori. Anche se ti mancano ancora altri moduli, puoi già verificare e adattare il tuo **profilo** in collaborazione con il tuo diabetologo.

Il **profilo** comprende:

- BR (tasso di basale): fornisce l'insulina di fondo;
- ISF (fattore di sensibilità insulinica): di quanto il livello di glucosio nel sangue sarà ridotto da 1 unità di insulina;
- CR (rapporto CHO): quanti grammi di CHO sono coperti da 1 unità di insulina;
- DIA (durata dell’azione insulinica).

La maggior parte degli utenti usano BR, ISF e CR, circadiani che adattano la sensibilità ormonale dell’insulina durante il giorno.

Maggiori informazioni sul tuo **profilo** [nella pagina dedicata](../SettingUpAaps/YourAapsProfile.md).

### Telefono

Vedere la pagina dedicata [Telefoni](../Getting-Started/Phones.md).

### Microinfusore di insulina

Vedi la pagina dedicata [Microinfusori Compatibili](../Getting-Started/CompatiblePumps.md).

**Vantaggi e svantaggi di alcuni modelli di micro**

Combo, Insight e i vecchi Medtronic sono micro solidi e utilizzabili per un circuito chiuso. Combo ha il vantaggio di molti modelli di set di infusione tra cui scegliere, in quanto ha un attacco Luer-Lock standard. La batteria è una mini-stilo che puoi acquistare in qualsiasi area di servizio, 24 ore su 24 e se ne hai davvero bisogno, è possibile rubare/prendere in prestito dal telecomando nella camera dell'hotel ;-).

I vantaggi di DanaR/RS e Dana-i confrontati a Combo come micro di scelta tuttavia sono:

- L'accoppiamento iniziale è più semplice con Dana-i/RS. Ma di solito lo fai solo una volta, quindi impatta solo se desideri provare una nuova funzione con micro diversi.
- Finora Combo funziona con l'analisi dello schermo. In generale funziona bene, ma è lento. Per un circuito chiuso, non importa tanto visto che tutto funziona in sfondo. Tuttavia richiede di essere spesso collegato, quindi la connessione BT potrebbe interrrompersi più facilmente, quando ti allontani dal telefono mentre fai un bolo & stai cucinando.
- Combo vibra alla fine delle basale temporanee, il DanaR vibra (o bippa) per i micro-boli. Di notte, è probabile che vorrai usare basale temporanee e non SMB.  Dana-i/RS è configurabile in modo da non bippare né vibrare.
- Reading the history on the Dana-i/RS in a few seconds with carbs makes it possible to switch phones easily while offline and continue looping as soon a soon as some CGM values are in.
- Tutte i micro compatibili con **AAPS** sono impermeabili alla consegna. Solo i micro Dana sono "impermeabili sotto garanzia" grazie al vano batterie sigillato e al sistema di riempimento del serbatoio.

### Sorgente Glicemia

Vedi la pagina dedicata [Sensori compatibili](../Getting-Started/CompatiblesCgms.md).

### File **AAPS**-.apk

Il componente principale del sistema. Per installare l'app, devi prima costruire il file apk. Le istruzioni sono [qui](../SettingUpAaps/BuildingAaps.md).

### Server di rendicontazione

Un server di rendicontazione permette di visualizzare i tuoi dati di glucosio, i trattamenti, e crea rapporti per delle analisi dettagliate. Ci sono attualmente due server di rendicontazione disponibili per l'uso con AAPS : [Nightscout](#SettingUpTheReportingServer-nightscout) e [Tidepool](#SettingUpTheReportingServer-tidepool). Entrambi forniscono modi per visualizzare i tuoi dati di diabete nel tempo, forniscono statistiche sul **tempo nell'intervallo** (TIR) e altri dati.

Il server di rendicontazione è indipendente dagli altri moduli. Se non vuoi usare un server di rendicontazione, devi sapere che non è obbligatorio per l'esecuzione di **AAPS** nel lungo termine. Ma è comunque necessario impostarne uno in quanto sarà richiesto per soddisfare [**l'Obiettivo 1**](#objectives-objective1).

Ulteriori informazioni su come configurare il tuo server di rendicontazione sono disponibili [qui](../SettingUpAaps/SettingUpTheReportingServer.md).

## Moduli Facoltativi

### Smartwatch

You can choose any smartwatch with Android WearOS 1.x up to 4.x. **Beware, WearOS 5.x is not compatible!**

Gli utenti stanno creando un elenco [di telefoni e orologi testati](#Phones-list-of-tested-phones). Ci sono diversi quadranti da usare con **AAPS**, che puoi trovare [qui](../WearOS/WearOsSmartwatch.md).

### xDrip+

Even if you don't need to have the xDrip+ App as **BG Source**, you can still use it for _i.e._ alarms or a different blood glucose display. Puoi avere tutti gli allarmi che vuoi, specificare il tempo in cui l'allarme deve essere attivo, se può ignorare la modalità silenziosa, ecc. Puoi trovare informazioni su xDrip+ [qui](../CompatibleCgms/xDrip.md). Siate consapevoli che la documentazione di questa applicazione non è sempre aggiornata, in quanto la sua evoluzione è abbastanza veloce.

## Cosa fare durante l'attesa dei moduli

A volte ci vuole un po' di tempo per ottenere tutti i moduli per chiudere il circuito. Ma nessuna preoccupazione, ci sono un sacco di cose che puoi fare mentre aspetti. È **necessario** controllare e, se necessario, adattare i tassi basali (BR), i rapporti insulina-CHO (IC), i fattori di sensibilità insulinica (ISF) ecc. Il circuito aperto può essere un buon modo per testare il sistema e familiarizzarsi con **AAPS**. Utilizzando questa modalità, **AAPS** fornisce raccomandazioni di trattamento che puoi eseguire manualmente.

Puoi continuare a leggere la documentazione qui, entrare in contatto con altri utenti AAPS online o offline, [leggere altri documenti](../UsefulLinks/BackgroundReading.md) o ciò che altri utenti scrivono (anche se devi fare attenzione, non tutto è corretto o buono da usare per te).

**Done?** If you have your **AAPS** components all together (congrats!) or at least enough to start in open loop mode, you should first read through the [Objective description](../SettingUpAaps/CompletingTheObjectives.md) before each new Objective and setup up your hardware.
