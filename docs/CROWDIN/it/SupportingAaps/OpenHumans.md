# Open Humans Uploader

## Dona i tuoi dati alla scienza

Puoi aiutare la comunità donando i tuoi dati a progetti di ricerca! Questo aiuta gli scienziati a restituire qualcosa, sviluppare nuove idee scientifiche e ampliare la mentalità aperta dei sistemi open source a circuito chiuso. **AAPS** è pronto a sincronizzare i tuoi dati con [Open Humans](https://www.openhumans.org), una piattaforma che ti permette di caricare, collegare e archiviare i tuoi dati personali – come genetica, attività e dati sulla salute.

Mantieni il pieno controllo su cosa succede ai tuoi dati e su quali progetti vuoi supportare dandogli accesso. A seconda del progetto a cui ti sei unito, i dati vengono valutati e utilizzati in modi e misura diversi.

I seguenti dati verranno caricati sul tuo account Open Humans:

- Valori di glicemia
- Eventi Careportal (eccetto le note)
- Extended boluses
- Cambi profilo
- Dosi giornaliere totali
- Basali temporanee
- Target temporanei
- Preferenze
- Versione dell'applicazione
- Modello del dispositivo
- Dimensioni dello schermo

Informazioni segrete o private come l'URL di Nightscout o il segreto API non verranno caricate.

## Configurazione

1. Crea il tuo account su [Open Humans](https://www.openhumans.org) se non l'hai ancora fatto. Puoi riutilizzare i tuoi account Google o Facebook esistenti se lo desideri.
2. Abilita il plugin "Open Humans" in [Costruttore di configurazione > Sincronizzazione](../SettingUpAaps/ConfigBuilder.md).
3. Apri le sue impostazioni usando il pulsante a forma di ingranaggio. Puoi limitare il caricamento ai momenti in cui il telefono usa il Wi-Fi e/o è in carica.
4. Apri il Plugin Open Humans (tramite la scheda OH o il menu hamburger) e clicca su 'LOGIN'.

![Open Humans Config Builder](../images/OHUploader1.png)

5. Leggi attentamente le informazioni fornite sull'Open Humans Uploader e i termini di utilizzo.
6. Conferma spuntando la casella e clicca su 'LOGIN'.
7. Si aprirà il sito web di Open Humans. Accedi con le tue credenziali.
8. Decidi se vuoi nascondere la tua iscrizione all'AAPS Uploader nel tuo profilo pubblico di Open Humans.
9. Clicca sul pulsante 'Autorizza progetto'.

![Open Humans Terms of Use + Login](../images/OHUploader2.png)

10. Tornando in AAPS vedrai un messaggio che conferma il login effettuato con successo.
11. Mantieni il plugin Open Humans Uploader e il telefono accesi per completare la configurazione.
12. Dopo aver cliccato su chiudi vedrai il tuo ID membro. Dimensioni della coda > 0 indica che ci sono ancora dati da caricare.
13. Clicca su 'LOGOUT' se vuoi interrompere il caricamento dei dati su Open Humans.
14. Una notifica Android ti informerà del caricamento in corso.

![Open Humans finish setup](../images/OHUploader3.png)

15. Puoi gestire i tuoi dati accedendo al [sito web di Open Humans](https://www.openhumans.org).

![Open Humans manage data](../images/OHWeb.png)

## Opportunità di condivisione

### [Il progetto 'OPEN'](https://www.open-diabetes.eu/)

Il progetto 'OPEN' riunisce un consorzio internazionale e intersettoriale di pazienti innovatori, clinici, scienziati sociali, informatici e organizzazioni di difesa dei pazienti, al fine di investigare vari aspetti dei Sistemi di Pancreas Artificiale fai-da-te (DIY APS) utilizzati da un numero crescente di persone con diabete. Per maggiori dettagli visita il loro [sito web](https://www.open-diabetes.eu/).

Nel settembre 2020 il progetto 'OPEN' ha lanciato un [sondaggio](https://survey.open-diabetes.eu/) che include l'opzione di donare i dati caricati su Open Humans. Un [tutorial](https://open-diabetes.eu/en/open-survey/survey-tutorials/) su come donare i tuoi dati al progetto 'OPEN' è disponibile sul loro sito e all'interno del sondaggio stesso.

### [OpenAPS Data Commons](https://www.openhumans.org/activity/openaps-data-commons/)

OpenAPS Data Commons è stato creato per fornire un modo semplice di condividere i set di dati dalla comunità DIYAPS per la ricerca. I dati vengono condivisi sia con ricercatori tradizionali che creeranno studi di ricerca tradizionali, sia con gruppi o individui della comunità che vogliono esaminare i dati come parte dei propri progetti di ricerca. OpenAPS Data Commons utilizza la piattaforma 'Open Humans' per consentire alle persone di caricare e condividere facilmente i propri dati dai DIYAPS inclusi AAPS, Loop e OpenAPS.

Puoi far confluire i tuoi dati in Open Humans in uno di tre modi:

1. usa l'opzione AAPS uploader per portare i tuoi dati in Open Humans
2. usa il Trasferimento Dati Nightscout per portare i tuoi dati in Open Humans
3. carica manualmente i file di dati in Open Humans.

Una volta creato un account e avviato il flusso di dati in Open Humans, assicurati di unirti anche a OpenAPS Data Commons per donare i tuoi dati alla ricerca, se lo desideri.

## Termini di utilizzo

Questo è uno strumento open source che copierà i tuoi dati su [Open Humans](https://www.openhumans.org). Non ci riserviamo alcun diritto di condividere i tuoi dati con terze parti senza la tua esplicita autorizzazione. I dati che il progetto e l'app ricevono sono identificati tramite un ID utente casuale e verranno trasmessi in modo sicuro a un account Open Humans solo con la tua autorizzazione di tale processo. Puoi interrompere il caricamento ed eliminare i dati caricati in qualsiasi momento tramite [www.openhumans.org](https://www.openhumans.org). Tieni presente che alcuni progetti che ricevono dati potrebbero non supportare questa funzionalità.

Vedi anche [Termini di utilizzo di Open Humans](https://www.openhumans.org/terms/).

## Privacy dei dati

Open Humans si occupa di proteggere la tua privacy assegnandoti un ID numerico per ogni progetto. Questo consente ai progetti di riconoscerti ma non di identificarti. L'ID applicazione caricato da AAPS è simile e aiuta solo ad amministrare i dati. Maggiori informazioni sono disponibili qui:

- [Politica sull'uso dei dati di Open Humans](https://www.openhumans.org/data-use/)
- [GDPR di Open Humans](https://www.openhumans.org/gdpr/)
