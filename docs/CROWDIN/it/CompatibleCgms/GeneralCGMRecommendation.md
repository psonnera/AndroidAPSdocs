- - -
orphan: true
- - -

# Raccomandazioni generali sui sensori

## Manutenzione del sensore

Qualunque sia il sistema CGM in uso, se si vuole utilizzare la calibrazione con il glucometro, ci sono alcune regole molto chiare da seguire, sia che si utilizzi un software DIY che per le applicazioni ufficiali.

-   Assicurati che le mani e il kit siano puliti.
-   Cerca di calibrare quando hai una sequenza di valori con una freccia orizzontale (15-30 minuti di solito è sufficiente).
-   Evita di calibrare quando la glicemia è in rialzo o discesa.
-   Fai “abbastanza” calibrazioni – sulle applicazioni ufficiali, ti verrà chiesto di effettuare controlli una o due volte al giorno. Sui sistemi DIY potrebbe non accadere, e si dovrebbe essere cauti nel continuare senza calibrazioni.
-   Per i sensori che non richiedono o non consentono la calibrazione, controlla almeno una volta al giorno la glicemia con il glucometro. AAPS sarà sicuro tanto quanto le letture del sensore sono attendibili.
-   Se possibile, calibra con alcuni valori in un intervallo basso (4-5 mmol/l o 72-90 mg/dl) e altri in un intervallo leggermente più alto (7-9 mmol/l o 126-160 mg/dl) in modo da fornire un margine migliore per la calibrazione del punto/pendenza.

## Inserimento del sensore (G6)

Quando si posiziona il sensore, si consiglia di non premere con troppa forza l'inseritore per evitare perdite di sangue. I contatti del sensore non dovrebbero venire a contatto con il sangue.

Dopo aver inserito il sensore, è possibile applicare il trasmettitore al supporto del sensore. Attenzione! Fare clic prima sul lato squadrato e poi premere sul lato rotondo.

(general-cgm-troubleshooting)=
## Risoluzione dei problemi

### Problemi di connessione

Bluetooth connection may be disturbed by other nearby Bluetooth devices such as blood glucose meters, headsets, tablets or kitchen devices such as microwave ovens or ceramic hobs. In this case xDrip+ does not display any BG values. When Bluetooth connection is re-established the data is backfilled.

### Sensor Errors

If recurring sensor errors occur try selecting a different body site to set your sensor. The sensor contacts should not come into contact with blood.

Often a "Sensor Error" can be corrected by immediate drinking and massage around the sensor!

### Jumpy values

You might try to change settings for noise blocking in xDrip+ (Settings - Inter-App Settings - Noise Blocking) i.e. "Block Very High noise and worse". See also [Smoothing BG data](../CompatibleCgms/SmoothingBloodGlucoseData.md).

### Negative Sensor Age

![Negative sensor age](../images/Troubleshooting_SensorAge.png)

This occurs if there is either a double "CGM Sensor Insert" entry in [actions tab / menu](#screens-action-tab) or a sensor insert with wrong date. Go to treatments tab \> careportal and delete the wrong entry.
