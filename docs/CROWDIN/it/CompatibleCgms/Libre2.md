# Freestyle Libre 2 e 2+

Il sensore Freestyle Libre 2 è ora un vero e proprio CGM anche con l'app ufficiale. Tuttavia, LibreLink non può inviare dati ad AAPS. Ci sono diverse soluzioni per usarlo con AAPS.

## 1. Usa un trasmettitore Bluetooth e OOP

Bluetooth transmitters can be used with the Libre 2 (EU) or 2+ (EU) and an out of process algorithm app. È possibile ricevere i valori della glicemia ogni 5 minuti come con il [Libre 1](./Libre1.md).

Controlla che il collegamento e l'applicazione che vuoi usare siano compatibili con il tuo sensore e con xDrip+ (i Blucon più vecchi e quelli più recenti non funzionano, Miaomiao 1 richiede il firmware 39 e Miaomiao 2 il firmware 7).

The Libre2 OOP (find it [here](#Libre2_OOP2)) is creating the same BG readings as with the original reader. AAPS con Libre 2 applica uno smussamento da 10 a 25 minuti per ridurre alcuni sbalzi. Vedi sotto [Smussamento dei valori e dati grezzi](#libre2-value-smoothing-raw-values). OOP crea letture ogni 5 minuti utilizzando la media degli ultimi 5 minuti. Di conseguenza, le letture della glicemia non sono molto omogenee, ma coincidono con quelle del dispositivo di lettura originale e ricalcano più rapidamente le letture della glicemia “reale”. Se vuoi provare a utilizzare il loop con OOP, attiva tutte le impostazioni di smussamento dati in xDrip+.

Ci sono alcune buone ragioni per utilizzare un trasmettitore Bluetooth:

-   Puoi scegliere diverse strategie di calibrazione OOP2 (1): avere i valori del lettore utilizzando “nessuna calibrazione”, oppure calibrare il sensore come un Libre 1 utilizzando “calibrazione basata su dati grezzi” o infine calibrare i valori del lettore con “calibrazione basata sul glucosio”.  
  Assicurati di lasciare OOP1 disabilitato (2).

    → Menu → Impostazioni → Impostazioni meno usate → Altre opzioni

![Calibrazione OOP2](../images/Libre2_OOP2Calibration.png)

-   Il sensore Libre 2 può essere usato per 14,5 giorni come il Libre 1
-   Il recupero dei dati entro le 8 ore è totalmente supportato

Nota: Il trasmettitore può essere utilizzato in contemporanea con l'applicazione LibreLink senza interferire.

### Start sensor

- → Menu (1) → Inizializza sensore (2) → Inizializza sensore (3) → Rispondi con "Non oggi" (4).

![xDrip+ Avvia Trasmettitore Libre & Sensore 3](../images/xDrip_Libre_Transmitter03.png)

Questo non avvia alcun sensore Libre2, né vi interagisce in alcun modo. Questo serve semplicemente a dire a xDrip+ che un nuovo sensore sta trasmettendo i valori della glicemia. Se disponibili, inserisci due misurazioni con il glucometro per la calibrazione iniziale. Ora i valori della glicemia dovrebbero essere visibili su xDrip+ ogni 5 minuti. I valori mancanti, ad esempio quando il sensore è distante dal telefono, non verranno reintegrati.

Dopo un cambio di sensore, xDrip+ rileva automaticamente il nuovo sensore ed elimina tutti i parametri di calibrazione vecchi. Dopo l'attivazione è possibile misurare la glicemia con il glucometro ed effettuare una nuova calibrazione iniziale.

### Configure AAPS (for looping only)

-   Su AAPS vai in Configuratore strutturale > Origine BG e seleziona 'xDrip+'.

![sorgente xDrip+ BG](../images/ConfBuild_BG_xDrip.png)

-   Se AAPS non riceve i valori della glicemia quando il telefono è in modalità aereo, usa “Identifica ricevitore” come descritto nella [pagina delle impostazioni di xDrip+](#xdrip-identify-receiver).

## 2. Usa la connessione diretta di xDrip+

```{admonition} Libre 2 EU only
:class: warning
xDrip+ non supporta la connessione diretta a Libre 2 US e AUS.
Solo i modelli Libre 2 e 2+ **EU**.
```

- Follow [these instructions](./Libre2MinimalL00per.md) to setup xDrip+ as the original documentation links to an obsolete OOP2  version.
- Segui le istruzioni di configurazione nella [pagina delle impostazioni di xDrip+](../CompatibleCgms/xDrip.md).

-   Select xDrip+ in in [ConfigBuilder, BG Source](#Config-Builder-bg-source).

(libre2-value-smoothing-raw-values)=

### Smussamento dei valori e dati grezzi

Dal punto di vista tecnico, il valore della glicemia viene trasmesso a xDrip+ ogni minuto. Di default, viene calcolato un valore “smussato” in base alla media ponderata degli ultimi 25 minuti. Puoi modificare questo periodo nelle impostazioni della scansione NFC.

→ Menu → Impostazioni → Funzionalità scansione NFC → Liscia i dati libre 3 quando si usa il metodo xxx

![xDrip+ impostazioni avanzate Libre 2 & valori grezzi](../images/xDrip_Libre3_Smooth.png)

Questo è obbligatorio per il loop. La curva dei valori diventa omogenea e i risultati del loop saranno migliori. I valori grezzi su cui si basano gli allarmi sono leggermente più discontinui, ma corrispondono ai valori mostrati anche dal lettore. Inoltre, i valori grezzi possono essere visualizzati nel grafico di xDrip+ per poter agire in tempo su variazioni improvvise. È sufficiente attivare Impostazioni meno usate \> Impostazioni avanzate per Libre 2 \> "Mostra i valori grezzi nel grafico" e "Mostra informazioni sensore nello stato". In questo modo i valori grezzi saranno indicati come piccoli punti bianchi e le informazioni aggiuntive sul sensore saranno visibili nello stato del sistema.

I valori grezzi sono molto utili quando la glicemia cambia rapidamente. Anche se i punti sono più irregolari, il trend viene individuato molto meglio se si utilizza la curva smussata per prendere decisioni terapeutiche corrette.

→ Menu → Impostazioni → Impostazioni meno usate → Impostazioni avanzate per Libre 2

![xDrip+ impostazioni avanzate Libre 2 & valori grezzi](../images/Libre2_RawValues.png)



#### Calibrazione

Puoi calibrare il Libre2 **con una differenza da -40 mg/dl a +20 mg/dL \[-2,2 mmol/l a +1,1 mmol/l\]** (intercetta). La pendenza non è modificabile. Controlla la glicemia con il glucometro dopo aver impostato un nuovo sensore, tenendo presente che potrebbe non essere preciso nelle prime 12 ore dopo l'inserimento. Visto che possono esserci notevoli differenze rispetto al glucometro, verifica ogni 24 ore e calibra se necessario. Se il sensore è ancora sballato dopo alcuni giorni, è necessario sostituirlo.

## 3. Usa Diabox

- Installa [Diabox](https://www.bubblesmartreader.com/_files/ugd/6afd37_f183eabd4fbd44fcac4b1926a79b094f.pdf). In Settings, Integration, abilita Share data with other apps.

![Diabox](../images/Diabox.png)

- Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

## 4. Usa Juggluco

See [here](./Juggluco.md).
