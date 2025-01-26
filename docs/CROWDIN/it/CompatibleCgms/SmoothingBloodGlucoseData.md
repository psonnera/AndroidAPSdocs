- - -
orphan: true
- - -

# Smoothing dei dati glicemici

Se i dati di glicemia (**BG**) sono salteggianti/rumorosi, **AAPS** può dosare l’insulina in modo non corretto con conseguenti iper o ipo. Se si osservano errori nei dati del sensore, è imperativo disattivare il circuito chiuso fino a quando il problema non verrà risolto. A seconda del tuo sensore, tali problemi potrebbero essere dovuti alla configurazione CGM in **AAPS** (come spiegato più avanti); o un problema del sito di inserimento del sensore (che potrebbe richiederne la sostituzione).

Alcuni sistemi CGM hanno algoritmi interni per rilevare il livello di rumore nelle letture, e **AAPS** può utilizzare queste informazioni per evitare di fare SMB se i dati di glicemia sono troppo inaffidabili. Tuttavia, alcuni CGM non trasmettono questi dati e per queste sorgenti di glicemia 'Abilita sempre SMB' e 'Abilita SMB con COB' sono disabilitati per motivi di sicurezza.

## Smooting dei dati in AAPS

A partire dalla versione **AAPS** 3.2, **AAPS** offre la possibilità di fare lo smoothing dei dati all'interno di **AAPS** piuttosto che nell'app CGM. Ci sono tre opzioni disponibili in [Configuratore Strutturale > Smoothing](../SettingUpAaps/ConfigBuilder.md).

![Smoothing](../images/ConfBuild_Smoothing.png)

### Smoothing esponenziale

Questa è l'opzione consigliata per cominciare, in quanto è più aggressiva nel risolvere il rumore, e riscrive il valore più recente.

### Smoothing medio

Questa opzione funziona in modo simile allo smoothing che è stato precedentemente implementato su alcune piattaforme CGM. È più reattivo ai recenti cambiamenti del valore di glicemia e quindi più soggetto a risposte errate ai dati CGM rumorosi.

### No smoothing

Usa questa opzione solo se i tuoi dati CGM vengono correttamente filtrati dalla tua app prima di essere trasmessi ad **AAPS**.

## Suggerimenti per usare lo smoothing

|                       | Esponenziale |   Medio    |   Nessuno   |
| --------------------- |:------------:|:----------:|:-----------:|
| G5 e G6               | Se rumoroso  |            | Consigliato |
| G7                    | Se rumoroso  | Se stabile |             |
| Libre 1 o Juggluco    | Consigliato  |            |             |
| Libre 2 e 3 da xDrip+ |              |            | Consigliato |

### Sensori Dexcom

#### Costruisci La Tua App Dexcom (BYODA)
Quando usi [BYODA](#DexcomG6-if-using-g6-with-build-your-own-dexcom-app), i dati di glicemia sono fluidi e coerenti. Inoltre, puoi approfittare dell'algoritmo Dexcom back-smoothing. Non ci sono restrizioni nell'utilizzo di SMB, perché i dati di livello di rumore sono condivisi con AAPS.

(smoothing-xdrip-dexcom-g6)=
#### xDrip+ con Dexcom G6 o Dexcom ONE
I dati di livello di rumore e le letture regolari di glicemia sono solo condivisi con AAPS se usi la modalità nativa di [xDrip+](https://navid200.github.io/xDrip/docs/Native-Algorithm). Utilizzando la modalità nativa, non ci sono restrizioni nell'uso di SMB.

#### Dexcom G6 o Dexcom ONE con modalità Companion xDrip+
I dati di livello di rumore non sono condivisi con AAPS utilizzando questo metodo. Pertanto, 'Abilita SMB sempre' e 'Abilita SMB con CHO' sono disabilitati.

### Sensori Freestyle Libre

#### xDrip+ con FreeStyle Libre1
Il FreeStyle Libre 1 non trasmette alcuna informazione sul livello di rumore rilevato nelle letture, e quindi 'Abilita SMB sempre' e 'Abilita SMB con CHO' sono disabilitati quando si usa questo CGM. Inoltre, molte persone hanno segnalato che il FreeStyle Libre 1 produce spesso dati rumorosi.
