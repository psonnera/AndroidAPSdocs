(Sensitivity-detection-and-COB-sensitivity-detection)=
# Rilevamento della sensibilità

## Algoritmo di sensibilità
Attualmente sono disponibili 3 modelli di rilevamento della sensibilità:

* Sensitivity AAPS
* Sensitivity WeightedAverage
* Sensitivity Oref1

### Sensitivity AAPS
La sensibilità viene calcolata allo stesso modo di Oref1, ma è possibile specificare il periodo di tempo nel passato. L'assorbimento minimo dei carboidrati viene calcolato dal tempo massimo di assorbimento dei carboidrati nelle preferenze.

### Sensitivity WeightedAverage
La sensibilità viene calcolata come media ponderata delle deviazioni. È possibile specificare il periodo di tempo nel passato. Le deviazioni più recenti hanno un peso maggiore. L'assorbimento minimo dei carboidrati viene calcolato dal tempo massimo di assorbimento dei carboidrati nelle preferenze. Questo algoritmo è il più rapido nel seguire le variazioni di sensibilità.

(SensitivityDetectionAndCob-sensitivity-oref1)=
### Sensitivity Oref1
La sensibilità viene calcolata dagli 8 ore di dati nel passato, o dall'ultimo cambio del sito se questo è avvenuto meno di 8 ore fa. I carboidrati (se non ancora assorbiti) vengono eliminati dopo il tempo specificato nelle preferenze. Solo l'algoritmo Oref1 supporta i pasti non annunciati (UAM). Ciò significa che i periodi con UAM rilevato vengono esclusi dal calcolo della sensibilità. Pertanto, se si utilizza SMB con UAM, è necessario scegliere l'algoritmo Oref1 per il corretto funzionamento. Per ulteriori informazioni consultare la [documentazione OpenAPS Oref1](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/oref1.html).

Oref1 è l'opzione consigliata: è l'unica in grado di rilevare i pasti UAM e funzionare con [OpenAps SMB](#Open-APS-features-super-micro-bolus-smb), l'algoritmo più recente.

## Carboidrati simultanei
Esiste una differenza significativa nell'utilizzo di AAPS, WeightedAverage rispetto a Oref1. I plugin Oref si aspettano che un solo pasto si stia degradando alla volta. Ciò significa che il secondo pasto inizia a degradarsi solo dopo che il primo pasto è completamente assorbito. AAPS+WeightedAverage inizia la degradazione immediatamente quando si inseriscono i carboidrati. Se ci sono più pasti in corso, la degradazione minima dei carboidrati si adatterà in base alle dimensioni del pasto e al tempo massimo di assorbimento. L'assorbimento minimo sarà quindi più elevato rispetto ai plugin Oref.
