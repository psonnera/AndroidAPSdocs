- - -
orphan: true
- - -

# Smoothing dei dati glicemici

Se i dati di glicemia (**BG**) sono salteggianti/rumorosi, **AAPS** può dosare l’insulina in modo non corretto con conseguenti iper o ipo. Se si osservano errori nei dati del sensore, è imperativo disattivare il circuito chiuso fino a quando il problema non verrà risolto. A seconda del tuo sensore, tali problemi potrebbero essere dovuti alla configurazione CGM in **AAPS** (come spiegato più avanti); o un problema del sito di inserimento del sensore (che potrebbe richiederne la sostituzione).

## Smooting dei dati in AAPS

A partire dalla versione **AAPS** 3.2, **AAPS** offre la possibilità di fare lo smoothing dei dati all'interno di **AAPS** piuttosto che nell'app CGM. Ci sono tre opzioni disponibili in [Configuratore Strutturale > Smoothing](../SettingUpAaps/ConfigBuilder.md).

![Smoothing](../images/ConfBuild_Smoothing.png)

### Smoothing esponenziale

In general, this is the recommended option to start with, as it is most aggressive in resolving noise and rewrites the most recent value. However, see the table below for other specific recommendations.

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

Libre sensors are noisy and can require smoothing. When using xDrip+ direct connection, or the patched app data source (receiving from another app, Juggluco included), smoothing is already done inside the app.

| Sensor / Data source | Juggluco | xDrip+ direct | xDrip+ bridge | xDrip+ patched app |
| -------------------- |:--------:|:-------------:|:-------------:|:------------------:|
| Libre 1/14 days/Pro  |   N.A.   |     N.A.      |    Average    |        N.A.        |
| Libre 2/2+ (EU)      | Average  |     None      |    Average    |        None        |
| Libre 2/2+/3/3+      | Average  |     N.A.      |     N.A.      |        None        |
