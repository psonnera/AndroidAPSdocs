# Glossario

 __AAPS__ = AndroidAPS è il nome dell'app Android.

__AAPSClient__ (o __NSClient__) = funzionalità di controllo remoto che può essere usata dai caregiver tramite un telefono di sorveglianza per seguire __AAPS__ di un utente connettendosi al sito __Nightscout__ dell'utente. Ulteriori informazioni → Wiki - 'NS Client'. Il programma di apprendimento Obiettivi all'interno di __AAPS__ fornisce una guida passo passo. Ulteriori informazioni → Wiki - 'obiettivi'.

__APS__ = Sistema di Pancreas Artificiale (Artificial Pancreas System).

__AMA__ = Advanced Meal Assist. Un algoritmo che permette ad __AAPS__ di aumentare la basale dell'utente in modo più aggressivo dopo un bolo pasto. Ulteriori informazioni → Wiki - 'AMA'.

__Fattore di Aggiustamento__ = utilizzato all'interno del **DynamicISF** ed è un valore impostato nelle **Preferenze** dell'utente tra 1% e 300%. Agisce come moltiplicatore sul valore **TDD**.
- aumentare il valore del **Fattore di Aggiustamento** sopra il 100% rende il **DynamicISF** più aggressivo: i valori **ISF** diventano più piccoli (cioè è necessaria più insulina per diminuire i livelli di **glicemia** di una piccola quantità)
- abbassare il valore del **Fattore di Aggiustamento** sotto il 100% rende il **DynamicISF** meno aggressivo: i valori **ISF** diventano più grandi (cioè è necessaria meno insulina per diminuire i livelli di **glicemia** di una piccola quantità).

__Android Auto__ = sistema usato per ospitare alcune funzioni delle funzionalità dello smartphone Android, incluso __AAPS__, nel display di un'auto. Ulteriori informazioni → Wiki - 'android auto'.

__APK__ = Pacchetto applicazione Android (Android application Package). Un file di installazione software.  Ulteriori informazioni → Wiki - 'Compilazione APK'.

__DIA__ = Durata dell'Azione dell'Insulina (Duration of Insulin Action). Ulteriori informazioni → Wiki - 'tipi di insulina' e vedere anche → DIABETTECH - 'DIA'.

__Azure__ = piattaforma cloud per ospitare l'app web __Nightscout__ Azure → vedere anche __Nightscout__.

__BAT__ = spia di stato batteria scarica nella schermata principale di __AAPS__ nelle __Preferenze__, Screenshot → vedere anche __CAN__ / __RES__ / __SEN__.

__glicemia__ = glicemia (blood glucose).

__BGI__ = impatto sulla glicemia (blood glucose impact). Il grado in cui la __glicemia__ 'dovrebbe' salire o scendere basandosi solo sull'attività dell'insulina.

__Sorgente BG__ = la sorgente dei valori di __glicemia__ dell'utente derivati da __CGM__ o __FGM__ tramite un software di integrazione come __BYODA__, __xDrip+__ ecc. Ulteriori informazioni → Wiki - 'Sorgente BG'  Further info → Wiki - 'sensor noise'. Further info → Wiki - 'temp targets'.

__Bridge__ = dispositivo aggiuntivo che trasforma __FGM__ in __CGM__.

__BR__ = Velocità Basale (Basal Rate). La quantità di insulina in un determinato intervallo di tempo per mantenere la __glicemia__ a un livello stabile. → vedere anche __IC__ / __ISF__.

__BYODA__ = Costruisci la tua app Dexcom (Build Your Own Dexcom App). Un modo per generare la propria app Dexcom per leggere i dati del sensore Dexcom G6.

__CAGE__ = Età Cannula (Cannula AGE). Visualizzato nella schermata principale di __AAPS__ e Nightscout fornendo le informazioni dell'utente inserite nella scheda/menu Azioni → vedere anche __Nightscout__.

__CAN__ = spia di stato cambio cannula in scadenza nella schermata principale di __AAPS__ nelle __Preferenze'__ → vedere anche __BAT__ / __RES__ / __SEN__.

__CGM__ = Monitor Continuo del Glucosio (Continuous Glucose Monitor) → vedere anche __FGM__.

__Closed Loop__ = sistema a loop chiuso che apporta correzioni automatiche all'erogazione basale dell'utente basandosi sull'algoritmo di __AAPS__ e le impostazioni del __Profilo__ dell'utente senza richiedere l'approvazione dell'utente. Ulteriori informazioni → Wiki - 'closed loop'.

__COB__ = Carboidrati Attivi (Carbs On Board). È la quantità di carboidrati attualmente disponibile per la digestione dell'utente → vedere anche IOB.

__CSF__ = Fattore di Sensibilità ai Carboidrati (Carbs Sensitivity Factor). Ovvero quanto aumenta la __glicemia__ dell'utente per 1g di carboidrati assorbiti.

__Tempo di picco__ = tempo dell'effetto massimo dell'insulina somministrata.  Ulteriori informazioni → Wiki - 'costruttore di configurazione'.

__DST__ = Ora Legale (Daylight Savings Time) Wiki DST.

__ISF Dinamico (o DynISF)__ = funzionalità di **AAPS** che adatta dinamicamente il fattore di sensibilità all'insulina (**ISF**) basandosi su:
- Dose Totale Giornaliera di insulina (**TDD**); e
- valori **glicemia** correnti e previsti.


__eCarbs__ = Carboidrati Estesi (extended Carbs). Carboidrati distribuiti su diverse ore per gestire proteine e permettere ad __AAPS__ di erogare boli estesi.  Ulteriori informazioni → Wiki - 'eCarbs', 'utilizzo eCarbs'.

__FGM__ = Flash Glucose Monitor prodotto da Freestyle Libre. Ulteriori informazioni → Wiki - 'Sorgente BG' e vedere anche 'CGM'.

__git__ = strumento usato per archiviare e scaricare il codice sorgente di __AAPS__.

__GitHub__ = servizio di hosting web e processo di compilazione per il sistema di controllo versione del software di __AAPS__ per tracciare le modifiche nei file del computer e coordinare il lavoro su quei file specialmente per i team. È necessario anche per gli aggiornamenti __APK__.  Ulteriori informazioni → Wiki - 'aggiornamento APK'.

__Glimp__ = app per raccogliere i valori da Freestyle Libre Glimp.

__IC (o I:C)__ = Rapporto Insulina-Carboidrati (Insulin to Carb ratio). (ovvero quanti carboidrati sono coperti da un'unità di insulina?).

__IOB__ = Insulina Attiva (Insulin On Board). Insulina attiva nel corpo dell'utente.

__ISF__ = Fattore di Sensibilità all'Insulina (Insulin Sensitivity Factor). La diminuzione prevista della glicemia come risultato di un'unità di insulina.

__Keystore (o JKS)__ = Java Key Store che è un file crittografato dove vengono memorizzati i certificati e le chiavi del tuo sviluppatore personale necessari per la compilazione (e ricompilazione) di __AAPS__.

__LGS__ = Sospensione per Glucosio Basso (Low Glucose Suspend). __AAPS__ ridurrà la basale se la __glicemia__ sta scendendo e se la __glicemia__ sta salendo, aumenterà la basale solo se l'__IOB__ è negativo (da un precedente __LGS__), altrimenti le velocità basali rimarranno le stesse del __Profilo__ selezionato dall'utente. L'utente potrebbe temporaneamente sperimentare picchi dopo la gestione di un'ipoglicemia senza la possibilità di aumentare la basale nel rimbalzo. → vedere anche obiettivo 6.

__LineageOS__ = sistema operativo libero e open-source per smartphone ecc. (Quando si usa Accu-Chek Combo vedere Wiki - Pompa Combo).

__File di log__ = registrazioni di __AAPS__ delle azioni dell'utente (utili per la risoluzione dei problemi e il debug). Ulteriori informazioni → Wiki - 'file di log'.

__maxIOB__ = IOB totale massimo. Questa è una funzione di sicurezza e impedisce ad __AAPS__ di erogare insulina oltre le impostazioni dell'utente.  Ulteriori informazioni → Wiki - 'SMB'.

__min_5m_carbimpact__ = funzione di sicurezza che è un calcolo del decadimento predefinito dei carboidrati quando l'assorbimento dei carboidrati non può essere determinato in base alle reazioni del sangue dell'utente. Questa è una funzione di sicurezza.  Ulteriori informazioni → Wiki - 'costruttore di configurazione'.

__Nightscout__ = progetto open source per accedere e segnalare i dati __CGM__. Il centro dati principale per i dati __AAPS__ dell'utente e può generare rapporti per visualizzare i dati storici __Nightscout__ dell'utente (HbA1c previsto, tempo nel range) o cercare schemi nei dati tramite grafici percentili ecc.

__Nightscout__ → vedere anche __Nightscout Reporter__. Questo è particolarmente utile per i genitori che seguono la gestione del diabete del proprio figlio.

__Strumento Nightscout Reporter__ = strumento che genera rapporti PDF dai dati dell'app web Nightscout. Vedere 'Nightscout Reporter', 'NS Reporter' @ Facebook.

__NSClient__ (o __'AAPSClient'__) = vedere __AAPSClient__.

__OpenAPS__ = Sistema di Pancreas Artificiale Open Source (Open Artificial Pancreas System).

__Sistema Open Loop__ = funzionalità di __AAPS__ che raccomanda correzioni che devono essere eseguite manualmente dall'utente su __AAPS__.  Ulteriori informazioni → Wiki - 'costruttore di configurazione'.

__Oref0 / Oref1__ = rilevamento della sensibilità e "implementazione del design di riferimento versione 0/1". È l'algoritmo principale alla base di OpenAPS Wiki - rilevamento della sensibilità.

__TT__ = temporary target temporary increase/decrease of the user’s __glicemia__ target (range) e.g. for eating or sport activities. Further info → Wiki - 'temp targets'.

__PH__ = Cronologia Microinfusore (Pump History). È accessibile nei trattamenti di __AAPS__ che si trovano nel menu a 3 punti sul lato destro della schermata principale di __AAPS__ Screenshot.

__Previsioni__ = previsioni per la __glicemia__ nel futuro basate su calcoli diversi. Ulteriori informazioni → Wiki - 'linee di previsione'.

__Profilo__ = le impostazioni di trattamento di base dell'utente (velocità basale, __DIA__, __IC__, __ISF__, target __glicemia__). AAPSv3 supporta solo i profili locali creati all'interno di __AAPS__ ma i __Profili__ di __Nightscout__ possono essere copiati (sincronizzati) su __AAPS__. Ulteriori informazioni → Wiki - 'profilo'.

__Cambio Profilo__ = cambio (temporaneo) del __Profilo__ dell'utente con un __Profilo__ diverso salvato in __AAPS__.

__Percentuale Profilo__ = aumento o diminuzione percentuale (temporanea) applicata al __Profilo__ di un utente per un periodo di tempo selezionato.

__RES__ = spia di stato cambio serbatoio in scadenza nella schermata principale di __AAPS__ Preferenze, Screenshot → vedere anche __BAT__ / __CAN__ / __SEN__.

__RileyLink__ = dispositivo hardware open source per collegare Bluetooth Low Energy (BLE) a comunicazioni wireless a 916 MHz (usato per vecchi microinfusori Medtronic) o 433 MHz (usato per microinfusori Omnipod Eros) RileyLink.

__SAGE__ = Età Sensore (sensor age). Viene visualizzato nella schermata principale di __AAPS__ e in __Nightscout__ se le informazioni sono state inserite nella scheda/menu Azioni → vedere anche __Nightscout__.

__SEN__ = spia di stato cambio sensore nella schermata principale Preferenze, Screenshot → vedere anche __BAT__ / __CAN__ / __RES__.

__Rilevamento della Sensibilità__ = calcolo della sensibilità all'insulina come risultato di esercizio, ormoni ecc. vedere anche → DIABETTECH - 'Autosens'.

__Rumore del sensore__ = termine usato per descrivere le letture instabili del __CGM__ che portano a valori di __glicemia__ "saltellanti".  Ulteriori informazioni → Wiki - 'rumore del sensore'.

__SMB__ = Super Micro Bolo (Super Micro Bolus). Funzionalità di __AAPS__ per un'erogazione più rapida di insulina al fine di regolare la __glicemia__.  Ulteriori informazioni → Wiki - '__SMB__' e vedere anche __UAM__.

__Super bolo__ = spostamento di insulina dalla basale al bolo per una regolazione più rapida della __glicemia__.

__TBB__ = basale di base totale (somma della velocità basale nelle 24 ore) → vedere anche __TBR__ / __TDD__.

__TBR__ = basale temporanea (temporary basal rate) → vedere anche __TBB__ / __TDD__.

__TDD__ = dose giornaliera totale (bolo + basale al giorno) → vedere anche __TBB__ / __TBR__.

__TT__ = target temporaneo (temporary target): aumento/diminuzione temporanea del target (intervallo) di __glicemia__ dell'utente, ad es. per attività di pasto o sportive.  Ulteriori informazioni → Wiki - 'target temporanei'.

__UAM__ = Pasti non annunciati (unannounced meals). Rilevamento di un aumento significativo dei livelli di __glicemia__ dovuto a pasti, adrenalina o altre influenze e tentativo di correzione.  Ulteriori informazioni → Wiki - 'UAM' e vedere anche __SMB__.

__Microinfusore virtuale__ = funzionalità di __AAPS__ che permette all'utente di provare le funzioni di __AAPS__ o per le persone con diabete che usano un modello di microinfusore senza driver __AAPS__ per il loop → vedere anche __Open Loop__.

__Sfondo__ = immagine di sfondo di __AAPS__ vedere la pagina dei telefoni.

__xDrip+__ = software open source per leggere i sistemi __CGM__ xDrip+.

__Zero-temp__ = basale temporanea con 0% (nessuna erogazione di insulina basale).

→ vedere anche [la documentazione OpenAPS](https://openaps.readthedocs.io/en/latest/docs/Resources/glossary.html)
