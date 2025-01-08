- - -
orphan: true
- - -

# Dexcom G7 e ONE+


## Basi anticipate

È da notare che i sensori G7 e ONE+, contrariamente al G6, non lisciano i valori della glicemia, né nell'app, né con il lettore. Maggiori dettagli [qui](https://www.dexcom.com/en-us/faqs/why-does-past-cgm-data-look-different-from-past-data-on-receiver-and-follow-app).

Immagine obsoleta!!!![G7 english](../images/6fe30b84-227a-4bae-a9a5-527cee341dbf.png)
`{admonition} [Metodo di smoothing](../CompatibleCgms/SmoothingBloodGlucoseData.md)`

## 1. xDrip+ (collegamento diretto a G7 o ONE+)

- Segui le istruzioni qui: [xDrip+ G7](https://navid200.github.io/xDrip/docs/Dexcom/G7.html)
- Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

- Regola le impostazioni xDrip+ seguendo le spiegazioni [impostazioni xDrip+](../CompatibleCgms/xDrip.md)

## 2.  App Dexcom G7 Patchata (DiaKEM)

**Nota: è necessario AAPS 3.2.0.0 o superiore! Non è disponibile per ONE+.**

### Installare una nuova app G7 patchata (!) e avviare il sensore

L’app Dexcom G7 patchata (DiaKEM) dà accesso ai dati Dexcom G7. Questa non è l'app BYODA in quanto questa non può ricevere i dati dal G7 al momento.

- Disinstalla l'app Dexcom originale se l'hai utilizzata prima (un sensore già avviato può ancora essere usato dopo - nota il codice del sensore prima di rimuovere l'app!)

- Scarica e installa l'app patchata [qui](https://github.com/authorgambel/g7/releases).

- Inserisci il codice del sensore nell'app patchata.

- Segui le raccomandazioni generali per l'igiene e il posizionamento dei sensori CGM [qui](../CompatibleCgms/GeneralCGMRecommendation.md).

- Dopo la fase di riscaldamento, i valori vengono visualizzati come di consueto nell'app G7.

### Configurazione in AAPS

- Seleziona 'BYODA' nel [Configuratore Strutturale, Origine BG](#Config-Builder-bg-source) - anche se non è l'app BYODA!

- Se AAPS non riceve alcun valore, passa a un altra origine BG e poi torna a 'BYODA' per fare generare la richiesta di scambio di dati tra AAPS e BYODA.

## 3. xDrip+ (modalità app compagno)

-   Scarica e installa xDrip+: [xDrip](https://github.com/NightscoutFoundation/xDrip)
- Come sorgente dati in xDrip+, seleziona "Companion App", nelle Impostazioni avanzate > Impostazioni Bluetooth > abilita "Companion Bluetooth".
-   Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

-   Adjust the xDrip+ settings according to the explanations on the xDrip+ settings page  [xDrip+ settings](../CompatibleCgms/xDrip.md)

## 4. Juggluco

Version 9.0+ required

- Disable the app previously connected to the sensor: Uninstall the app or use "Force Stop." Disable "Nearby Devices" permission in app settings. Restrict the app's battery usage.

- Forget the sensor in Bluetooth settings: In Android settings, find the sensor in bonded devices and select "Forget." Dexcom G7 sensor names start with DXCM.

- Avoid interference from other sensors: Keep old Dexcom sensors out of Bluetooth range.

- Connect the G7 sensor to Juggluco: Open Juggluco → Left menu → Photo. Scan the data matrix on the G7 sensor's applicator. Wait up to 5 minutes for Juggluco to find the sensor.

- Pairing requirements: Agree to pair the sensor with Juggluco. Ensure the screen isn’t locked during pairing. If pairing fails, wait 5 minutes before trying again.

- Exception: Wear OS watches can bond without pressing an agree button.
