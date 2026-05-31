# CareSens

Ci sono diversi modi per utilizzare i dati CareSens con **AAPS**:

- xDrip+
- Juggluco

**Nota:** Non hai bisogno dell'app Sens365 follower per connetterti ad AAPS.

## 1. xDrip+

1. Installa e configura l'app CareSens ufficiale.
2. Nell'app CareSens, vai su impostazioni -> Gestisci dati e connessioni -> attiva l'interruttore xDrip. Se preferisci, disattiva le connessioni dati a CareLevo, DIA:CONN, CloudLoop, ecc. in "altri".

![CareSens App Data Connections](../images/eversenseapp-dataconnections.png)


2. Installa xDrip+: [xDrip](https://github.com/NightscoutFoundation/xDrip).
3. In xDrip+, vai su impostazioni -> sorgente dati hardware, seleziona `Companion App` come sorgente dati.
4. In **AAPS**, seleziona xDrip+ nel [Configuratore Strutturale, Origine BG](#Config-Builder-bg-source).


## 2. Juggluco

1. Installa l'app Juggluco.
2. In Juggluco, apri il menu a sinistra e seleziona `Photo`
3. Scansiona il codice QR sulla confezione del sensore.
4. Nel menu a sinistra -> impostazioni -> scambia dati, assicurati che la trasmissione xDrip sia attivata.
5. In **AAPS**, seleziona xDrip+ nel [Configuratore Strutturale, Origine BG](#Config-Builder-bg-source).
