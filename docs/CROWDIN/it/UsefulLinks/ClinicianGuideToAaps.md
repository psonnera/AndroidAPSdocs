# Per i clinici – Introduzione generale e guida ad AAPS

Questa pagina è destinata ai clinici che hanno espresso interesse per la tecnologia open source del pancreas artificiale come AAPS, o ai pazienti che vogliono condividere tali informazioni con i propri medici.

Questa guida contiene alcune informazioni di alto livello sul loop chiuso fai-da-te e in particolare su come funziona AAPS. Per maggiori dettagli su tutti questi argomenti, consultare la [documentazione completa di AAPS online](../index.md). In caso di domande, chiedere al paziente per maggiori dettagli, o contattare la comunità. (Se non sei sui social media (ad es. [Twitter](https://twitter.com/kozakmilos) o Facebook), invia un'email a developers@AndroidAPS.org). [Qui puoi trovare anche alcuni degli ultimi studi e dati sui risultati](https://openaps.org/outcomes/).

## I passaggi per costruire un Loop Chiuso fai-da-te:

Per iniziare a usare AAPS, è necessario eseguire i seguenti passaggi:
* Trovare un [microinfusore compatibile](../Getting-Started/CompatiblePumps.md), un [dispositivo Android compatibile](../Getting-Started/Phones.md) e una [sorgente CGM compatibile](../Getting-Started/CompatiblesCgms.md).
* [Scaricare il codice sorgente di AAPS e compilare il software](../SettingUpAaps/BuildingAaps.md).
* [Configurare il software per comunicare con i dispositivi per il diabete e specificare le impostazioni e le preferenze di sicurezza](../SettingUpAaps/SetupWizard.md).

## Come funziona un Loop Chiuso fai-da-te

Senza un sistema a loop chiuso, una persona con diabete raccoglie i dati dal microinfusore e dal CGM, decide cosa fare e agisce.

Con l'erogazione automatica di insulina, il sistema fa la stessa cosa: raccoglie i dati dal microinfusore, dal CGM e da qualsiasi altro luogo in cui vengono registrate le informazioni (come Nightscout), utilizza queste informazioni per fare i calcoli e decidere quanta insulina in più o in meno è necessaria (sopra o sotto la velocità basale di base), e utilizza basali temporanee per apportare le correzioni necessarie a mantenere o riportare la glicemia nell'intervallo target.

Se il dispositivo che esegue AAPS si guasta o esce dall'intervallo del microinfusore, una volta terminata l'ultima basale temporanea, il microinfusore torna a funzionare come un microinfusore standard con le velocità basali preprogrammate.

## Come vengono raccolti i dati:

Con AAPS, un dispositivo Android esegue un'app speciale per fare i calcoli; il dispositivo comunica tramite Bluetooth con un microinfusore supportato. AAPS può comunicare con altri dispositivi e con il cloud tramite wifi o dati mobili per raccogliere informazioni aggiuntive e riferire al paziente, agli assistenti e ai familiari su cosa sta facendo e perché.

Il dispositivo Android deve:
* comunicare con il microinfusore e leggere la cronologia - quanta insulina è stata erogata
* comunicare con il CGM (direttamente o tramite il cloud) - per vedere i valori di glicemia attuali e passati

Quando il dispositivo ha raccolto questi dati, l'algoritmo viene eseguito e prende decisioni basate sulle impostazioni (ISF, rapporto carboidrati, DIA, target, ecc.). Se necessario, invia comandi al microinfusore per modificare la velocità di erogazione dell'insulina.

Raccoglierà anche informazioni sui boli, il consumo di carboidrati e le modifiche ai target temporanei dal microinfusore o da Nightscout per utilizzarle nel calcolo delle velocità di erogazione dell'insulina.

## Come sa cosa fare?

Il software open source è progettato per rendere facile al dispositivo il lavoro che le persone facevano (in modalità manuale) per calcolare come dovrebbe essere regolata l'erogazione di insulina. Per prima cosa raccoglie i dati da tutti i dispositivi di supporto e dal cloud, prepara i dati ed esegue i calcoli, fa previsioni dei livelli di glicemia previsti nelle prossime ore in diversi scenari e calcola le correzioni necessarie per mantenere o riportare la glicemia nell'intervallo target. Poi invia le correzioni necessarie al microinfusore. Quindi rilegge i dati e ricomincia.

Poiché il parametro di input più importante è il livello di glucosio nel sangue proveniente dal CGM, è importante avere dati CGM di alta qualità.

AAPS è progettato per tracciare in modo trasparente tutti i dati di input raccolti, la raccomandazione risultante e qualsiasi azione intrapresa. È quindi facile rispondere alla domanda in qualsiasi momento "perché sta facendo X?" esaminando i log.

## Esempi di processo decisionale dell'algoritmo AAPS:

AAPS utilizza lo stesso algoritmo di base e le stesse funzionalità di OpenAPS. L'algoritmo fa molteplici previsioni (basate sulle impostazioni e sulla situazione) che rappresentano diversi scenari di ciò che potrebbe accadere in futuro. In Nightscout, queste vengono visualizzate come "linee viola". AAPS usa colori diversi per separare queste [linee di previsione](#aaps-screens-prediction-lines). Nei log, descriverà quale di queste previsioni e quale intervallo di tempo sta guidando le azioni necessarie.

### Ecco alcuni esempi delle linee di previsione viola e come potrebbero differire:

![Purple prediction line examples](../images/Prediction_lines.jpg)

### Ecco alcuni esempi di diversi intervalli di tempo che influenzano le correzioni necessarie all'erogazione di insulina:

### Scenario 1 - Basale zero per sicurezza

In questo esempio, la glicemia sta aumentando a breve termine; tuttavia, si prevede che sarà bassa su un periodo più lungo. In effetti, si prevede che scenda al di sotto del target *e* della soglia di sicurezza. Per sicurezza, per prevenire il basso, AAPS emetterà una basale zero (basale temporanea allo 0%), finché la glicemia prevista (in qualsiasi intervallo di tempo) non sarà al di sopra della soglia.

![Dosing scenario 1](../images/Dosing_scenario_1.jpg)

### Scenario 2 - Basale zero per sicurezza

In questo esempio, si prevede che la glicemia scenda a breve termine, ma si prevede che alla fine sarà sopra il target. Tuttavia, poiché il basso a breve termine è effettivamente al di sotto della soglia di sicurezza, AAPS emetterà una basale zero finché non ci sarà più nessun punto della linea di previsione al di sotto della soglia.

![Dosing scenario 2](../images/Dosing_scenario_2.jpg)

### Scenario 3 - Serve più insulina

In questo esempio, una previsione a breve termine mostra una caduta al di sotto del target. Tuttavia, non si prevede che scenda al di sotto della soglia di sicurezza. La glicemia prevista finale è sopra il target. Pertanto, AAPS si asterrà dall'aggiungere insulina che contribuirebbe a un basso a breve termine (aggiungendo insulina che farebbe scendere la previsione al di sotto della soglia). Poi valuterà l'aggiunta di insulina per riportare il livello più basso della glicemia prevista finale al target, una volta che è sicuro farlo. *(A seconda delle impostazioni e della quantità e del timing dell'insulina necessaria, questa insulina può essere erogata tramite basali temporanee o SMB (super micro boli)).*

![Dosing scenario 3](../images/Dosing_scenario_3.jpg)

### Scenario 4 - Basale bassa per sicurezza

In questo esempio, AAPS vede che la glicemia sta salendo ben al di sopra del target. Tuttavia, a causa del timing dell'insulina, c'è già abbastanza insulina nel corpo per portare la glicemia nell'intervallo alla fine. In effetti, si prevede che la glicemia alla fine scenda al di sotto del target. Pertanto, AAPS non fornirà insulina extra per non contribuire a un basso a lungo termine. Anche se la glicemia è alta/in aumento, è probabile che qui venga impostata una bassa basale temporanea.

![Dosing scenario 4](../images/Dosing_scenario_4.jpg)

## Ottimizzazione delle impostazioni e apportare modifiche

Come clinico che potrebbe non avere esperienza con AAPS o con i loop chiusi fai-da-te, potresti trovare difficile aiutare il tuo paziente a ottimizzare le impostazioni o apportare modifiche per migliorare i suoi risultati. Abbiamo molteplici strumenti e [guide](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/optimize-your-settings.html) nella comunità che aiutano i pazienti a fare piccole modifiche testate per migliorare le loro impostazioni.

La cosa più importante che i pazienti devono fare è apportare un cambiamento alla volta e osservare l'impatto per 2-3 giorni prima di scegliere di cambiare o modificare un'altra impostazione (a meno che non sia ovviamente un cambiamento negativo che peggiora le cose, nel qual caso dovrebbero tornare immediatamente all'impostazione precedente). La tendenza umana è di girare tutte le manopole e cambiare tutto in una volta; ma se qualcuno lo fa, potrebbe ritrovarsi con ulteriori impostazioni sub-ottimali per il futuro e trovare difficile tornare a uno stato funzionante noto.

Uno degli strumenti più potenti per apportare modifiche alle impostazioni è uno strumento di calcolo automatico per le velocità basali, ISF e rapporto carboidrati. Questo si chiama "[Autotune](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html)". È progettato per essere eseguito in modo indipendente/manuale e consentire ai dati di guidare te o il tuo paziente nell'apportare modifiche incrementali alle impostazioni. È buona pratica nella comunità eseguire (o rivedere) i rapporti Autotune prima di tentare di apportare modifiche manuali alle impostazioni. Con AAPS, Autotune verrà eseguito come operazione "una tantum", anche se ci sono sforzi in corso per incorporarlo direttamente in AAPS. Poiché questi parametri sono un prerequisito sia per l'erogazione standard di insulina con microinfusore che per l'erogazione di insulina a loop chiuso, la discussione dei risultati di autotune e la regolazione di questi parametri sarebbe il collegamento naturale con il clinico.

Inoltre, il comportamento umano (appreso dalla modalità manuale del diabete) spesso influenza i risultati, anche con un loop chiuso fai-da-te. Ad esempio, se si prevede che la glicemia scenda e AAPS riduce l'insulina mentre scende, potrebbero essere necessari solo pochi carboidrati (ad es. 3-4 g di carboidrati) per riportare la glicemia da 70 mg/dl (3,9 mmol). Tuttavia, in molti casi, qualcuno potrebbe scegliere di trattare con molti più carboidrati (ad es. attenendosi alla regola del 15), il che causerà un picco più rapido sia dal glucosio extra che perché l'insulina era stata ridotta nel periodo che ha preceduto il basso.
## OpenAPS

**Questa guida è stata adottata dalla [guida del clinico a OpenAPS](https://openaps.readthedocs.io/en/latest/docs/Resources/clinician-guide-to-OpenAPS.html).** OpenAPS è un sistema sviluppato per essere eseguito su un piccolo computer portatile (generalmente denominato "rig"). AAPS utilizza molte delle tecniche implementate in OpenAPS e condivide gran parte della logica e degli algoritmi, motivo per cui questa guida è molto simile alla guida originale. Gran parte delle informazioni su OpenAPS può essere facilmente adattata ad AAPS, con la differenza principale che è la piattaforma hardware su cui viene eseguito ciascun software.


## Riepilogo

Questa è una panoramica di alto livello su come funziona AAPS. Per maggiori dettagli, chiedere al paziente, contattare la comunità o leggere la documentazione completa di AAPS disponibile online.

Letture aggiuntive consigliate:
* La [documentazione completa di AAPS](../index.md)
* Il [Progetto di riferimento OpenAPS](https://OpenAPS.org/reference-design/), che spiega come OpenAPS è progettato per la sicurezza: https://openaps.org/reference-design/
* La [documentazione completa di OpenAPS](https://openaps.readthedocs.io/en/latest/index.html)
  * Maggiori [dettagli sui calcoli OpenAPS](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/Understand-determine-basal.html#understanding-the-determine-basal-logic)

