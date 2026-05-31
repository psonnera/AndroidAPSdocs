# DanaR Pump

_Queste istruzioni riguardano la configurazione dell'app e del microinfusore per chi possiede un DanaR.  Visitare [Microinfusore DanaRS](./DanaRS-Insulin-Pump.md) se si possiede il DanaRS lanciato nel 2017._

* Nel microinfusore andare al Menu Principale > Impostazioni > Opzione Utente
* Attivare "8. Bolo Esteso"

![DanaR pump](../images/danar1.png)

* Andare al Menu Principale > Impostazioni > Discovery
* Nelle impostazioni del telefono andare al Bluetooth, cercare i dispositivi nelle vicinanze, selezionare il numero seriale del DanaR e inserire la password (la password di associazione è 0000).  Se il DanaR non appare nella ricerca, riavviare il telefono, rimuovere e reinserire la batteria del DanaR e ripetere questi due passaggi.

* In AAPS andare al Costruttore di configurazione e selezionare il tipo di DanaR (DanaR, DanaR Korean, DanaRv2)
* Selezionare il Menu toccando i 3 punti in alto a destra. Selezionare Preferenze.
* Selezionare Dispositivo Bluetooth DanaR e fare clic sul numero seriale del DanaR.
* Selezionare Password microinfusore e inserire la password. (La password predefinita è 1234)
* Se si desidera che AAPS permetta una basale superiore al 200%, abilitare Usa boli estesi per >200%. Nota: questo significa che non è possibile fare loop con TBR elevate durante l'utilizzo di boli estesi per i pasti.
* Nelle Preferenze sotto le impostazioni del microinfusore DanaR è possibile cambiare la velocità predefinita del bolo (12 sec per 1U, 30 sec per 1U o 60 sec per 1U).
* Impostare il passo basale del microinfusore a 0,01 U/h
* Impostare il passo bolo del microinfusore a 0,1 U/h
* Enable extended boluses on pump

## Viaggi con cambi di fuso orario con il microinfusore Dana R

Per informazioni sui viaggi attraverso i fusi orari vedere la sezione [Viaggi con cambi di fuso orario con i microinfusori](#timezone-traveling-danarv2-danars).
