# Smoothing dei dati glicemici

Se i dati di glicemia (**glicemia**) sono salteggianti/rumorosi, **AAPS** può dosare l’insulina in modo non corretto con conseguenti iper o ipo. Se si osservano errori nei dati del sensore, è imperativo disattivare il circuito chiuso fino a quando il problema non verrà risolto. A seconda del tuo sensore, tali problemi potrebbero essere dovuti alla configurazione CGM in **AAPS** (come spiegato più avanti); o un problema del sito di inserimento del sensore (che potrebbe richiederne la sostituzione).

## Smooting dei dati in AAPS

A partire dalla versione **AAPS** 3.2, **AAPS** offre la possibilità di fare lo smoothing dei dati all'interno di **AAPS** piuttosto che nell'app CGM. Ci sono tre opzioni disponibili in [Configuratore Strutturale > Smoothing](../SettingUpAaps/ConfigBuilder.md).

![Smoothing](../images/ConfBuild_Smoothing.png)

### Smoothing esponenziale

In generale, questa è l'opzione consigliata da cui iniziare, poiché è la più aggressiva nel risolvere il rumore e riscrive il valore più recente. Tuttavia, consulta la tabella di seguito per altre raccomandazioni specifiche.

### Smoothing medio

Questa opzione funziona in modo simile allo smoothing che è stato precedentemente implementato su alcune piattaforme CGM. È più reattivo ai recenti cambiamenti del valore di glicemia e quindi più soggetto a risposte errate ai dati CGM rumorosi.

### No smoothing

Usa questa opzione solo se i tuoi dati CGM vengono correttamente filtrati dalla tua app prima di essere trasmessi ad **AAPS**.

(smoothing-xdrip-dexcom-g6)=

## Suggerimenti per usare lo smoothing

|               | Exponential |  Average  |    None     |
| ------------- |:-----------:|:---------:|:-----------:|
| G5/G6/ONE     |  If noisy   |           | Recommended |
| G7/ONE+/Stelo |  If noisy   | If stable |             |

I sensori Libre sono rumorosi e possono richiedere lo smoothing. Quando si utilizza la connessione diretta xDrip+ o il sorgente dati dell'app patchata (ricevendo da un'altra app, incluso Juggluco), [lo smoothing viene già effettuato all'interno dell'app](#libre2-value-smoothing-raw-values).

| Sensor / Data source | Juggluco | xDrip+ direct | xDrip+ bridge | xDrip+ patched app |
| -------------------- |:--------:|:-------------:|:-------------:|:------------------:|
| Libre 1/14 days/Pro  |   N.A.   |     N.A.      |    Average    |        N.A.        |
| Libre 2/2+ (EU)      | Average  |     None      |    Average    |        None        |
| Libre 2/2+/3/3+      | Average  |     N.A.      |     N.A.      |        None        |
