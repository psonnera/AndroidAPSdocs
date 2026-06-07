# Microinfusore di insulina Diaconn G8

## Abbinamento Bluetooth al Micro

- Fare clic sul menu hamburger nell'angolo in alto a sinistra.

![image](../images/DiaconnG8/DiaconnG8_01.jpg)

- Fare clic su Costruttore di configurazione.

![image](../images/DiaconnG8/DiaconnG8_02.jpg)

- Dopo aver selezionato il Microinfusore Diaconn G8, fare clic sull'icona Impostazioni (ingranaggio).

![image](../images/DiaconnG8/DiaconnG8_03.jpg)

- Scegli il micro selezionato.

![image](../images/DiaconnG8/DiaconnG8_04.jpg)

- Selezionare il numero di modello del microinfusore di insulina una volta che appare nell'elenco.

![image](../images/DiaconnG8/DiaconnG8_05.jpg)

- Ci sono due opzioni per controllare il numero di modello:

1. Le ultime 5 cifre del numero SN sul retro del microinfusore.
2. Fare clic sul pulsante O > Informazioni > BLE > Ultime 5 cifre.

![image](../images/DiaconnG8/DiaconnG8_06.jpg)

- Una volta selezionato il microinfusore, appare una finestra che richiede un codice PIN. Inserire il numero PIN visualizzato sul microinfusore per completare la connessione.

 ![image](../images/DiaconnG8/DiaconnG8_07.jpg)

## Controllo dello stato del microinfusore e sincronizzazione dei log

- Una volta connesso il microinfusore, fare clic sul simbolo Bluetooth per controllare lo stato e sincronizzare i log.

![image](../images/DiaconnG8/DiaconnG8_08.jpg)

## Risoluzione dei problemi Bluetooth

**Cosa fare in caso di connessione Bluetooth instabile con il microinfusore.**

### Metodo 1) Controllare di nuovo il microinfusore dopo che l'applicazione AAPS è stata completata.

- Fare clic sul pulsante con i 3 punti in alto a destra.

![image](../images/DiaconnG8/DiaconnG8_09.jpg)

- Fare clic su Esci.

![image](../images/DiaconnG8/DiaconnG8_10.jpg)

### Metodo 2) Se il primo metodo non funziona, disconnettere il Bluetooth e poi riconnettere.

- Tenere premuto il pulsante Bluetooth in alto per circa 3 secondi.

![image](../images/DiaconnG8/DiaconnG8_11.jpg)

- Fare clic sul pulsante Impostazioni sul microinfusore di insulina Diaconn G8 associato.

![image](../images/DiaconnG8/DiaconnG8_12.jpg)

- Disaccoppia.

![image](../images/DiaconnG8/DiaconnG8_13.jpg)

- Ripetere il processo di associazione Bluetooth per il microinfusore (vedere sopra).

## Ulteriori informazioni

### Impostazione delle opzioni del microinfusore di insulina Diaconn G8

- Gestore configurazione > microinfusore > Diaconn G8 > Impostazioni
- DIACONN G8 in alto > pulsante 3 punti in alto a destra > Preferenze Diaconn G8

![Diaconn G8 pump options](../images/DiaconnG8/DiaconnG8_14.jpg)

- Se l'opzione **Registra cambio serbatoio** è attivata, i dettagli rilevanti vengono caricati automaticamente nel careportal quando si verifica un evento "Cambio insulina".
- Se l'opzione **Registra cambio ago** è attivata, i dettagli rilevanti vengono caricati automaticamente nel careportal quando si verifica un evento "Cambio sito".
- Se l'opzione **Registra cambio tubo** è attivata, i dettagli rilevanti vengono caricati automaticamente nel careportal quando si verifica un evento "Cambio tubo".
- Se l'opzione **Registra cambio batteria** è attivata, i dettagli rilevanti vengono caricati automaticamente nel careportal quando si verifica un evento "Cambio batteria" e il pulsante CAMBIO BATTERIA MICROINFUSORE nella scheda AZIONI viene disattivato. (Nota: per cambiare la batteria, si prega di interrompere tutte le funzioni di iniezione in corso prima di procedere.)

![Diaconn G8 actions menu](../images/DiaconnG8/DiaconnG8_15.jpg)

### Funzione Bolo Esteso

- Se si utilizza il bolo esteso verrà disabilitato il loop chiuso.
- Vedere [questa pagina](#extended-bolus-and-why-they-wont-work-in-closed-loop-environment) per i dettagli sul motivo per cui il bolo esteso non funziona in un ambiente con loop chiuso.
