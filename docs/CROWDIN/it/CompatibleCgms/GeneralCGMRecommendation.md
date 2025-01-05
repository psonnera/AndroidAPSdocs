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

La connessione Bluetooth può essere disturbata da altri dispositivi Bluetooth nelle vicinanze, come glucometri, cuffie, tablet o elettrodomestici come forni a microonde o piani cottura in ceramica. In questo caso xDrip+ non mostra alcun valore di glicemia. Quando sarà ristabilita la connessione Bluetooth, i dati precedenti verranno recuperati.

### Errori del sensore

Se si verificano continui errori del sensore, prova a cambiare il punto del corpo in cui inserire il sensore. I contatti del sensore non dovrebbero venire a contatto con il sangue.

Spesso un “errore del sensore” può essere corretto bevendo e massaggiando attorno al sensore!

### Valori instabili

Puoi provare a modificare le impostazioni per il blocco del rumore in xDrip+ (Impostazioni - Impostazioni Inter-app - Blocco rumore), ad esempio “Blocca rumore molto alto e superiore”. Vedi anche [Smussamento dei dati glicemici](../CompatibleCgms/SmoothingBloodGlucoseData.md).

### Età negativa del sensore

![Età negativa del sensore](../images/Troubleshooting_SensorAge.png)

Questo si verifica se c'è una doppia registrazione “Inserimento sensore CGM” nella scheda [tab azioni / menu](#screens-action-tab) o un inserimento del sensore con data errata. Vai alla scheda trattamenti \> portale ed elimina la voce sbagliata.
