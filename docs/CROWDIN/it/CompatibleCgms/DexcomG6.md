- - -
orphan: true
- - -

# Dexcom G6 e ONE

## Prima le basi

-   Segui i consigli generali di igiene del sensore e le impostazioni corrispondente [qui](../CompatibleCgms/GeneralCGMRecommendation.md).

## Suggerimenti generali per il circuito chiuso con G6 e ONE

- I trasmettitori recenti sono chiamati Firefly. I sensori non possono essere riavviati senza rimuovere il trasmettitore, il quale non può essere resettato, e non generano dati grezzi.

- Se stai riavviando i sensori, assicurati di essere pronto a calibrare e tieni d'occhio le variazioni di glicemia.

- È probabile che l'inserimento anticipato dei sensori G6/ONE crei variazioni nei risultati, data la calibrazione di fabbrica di questi sensori. Se usi questa strategia, dovrai probabilmente calibrare il sensore per ottenere risultati migliori.

Leggi di più nell'[articolo](https://www.diabettech.com/artificial-pancreas/diy-looping-and-cgm/) pubblicato da Tim Street su [www.diabettech.com](https://www.diabettech.com).

## Se usi un sensore G6 o ONE con xDrip+

- Se stai usando un trasmettitore recente (Firefly), il riavvio preventivo è **ignorato**.
- Se stai usando un trasmettitore modificato, **non hai bisogno** di impostare i riavvii preventivi.
-   Se stai usando un vecchio trasmettitore ricondizionato, la cosa più sicura da fare è di **disabilitare** il [riavvio preventivo](https://navid200.github.io/xDrip/docs/Preemptive-Restart.html). Però, in questo caso dovrai usare il G6 in [ modalità nativa](https://navid200.github.io/xDrip/docs/Native-Algorithm.html) (che è sconsigliato in quanto disabilita la calibrazione di fabbrica e non filtra le letture rumorose), oppure il sensore si fermerà dopo 10 giorni.
-   I trasmettitori Dexcom G6 e ONE possono essere collegati contemporaneamente al ricevitore Dexcom (o in alternativa al micro t:slim) e a un’app sul telefono.
-   Quando utilizzi xDrip+ collegato al sensore, disinstalla prima l'app Dexcom. **Non è possibile collegare le app xDrip+ e Dexcom al trasmettitore contemporaneamente!**
-   Se hai bisogno di Clarity e vuoi approfittare degli allarmi xDrip+ usa [BYODA](#DexcomG6-if-using-g6-with-build-your-own-dexcom-app) (solo G6) con trasmissione locale (broadcast) verso xDrip+.
-   È anche possibile utilizzare xDrip+ come app di compagno dell'app ufficiale Dexcom, ma si potrebbero verificare ritardi nelle letture di glicemia.
-   Se non lo hai già installato, scarica [xDrip+](https://github.com/NightscoutFoundation/xDrip) e segui le istruzioni sulla pagina [Impostazioni xDrip+](../CompatibleCgms/xDrip.md).
-   Select xDrip+ in in [ConfigBuilder, BG Source](#Config-Builder-bg-source).

- Adjust settings in xDrip+ according to [xDrip+ settings page](../CompatibleCgms/xDrip.md)

(DexcomG6-if-using-g6-with-build-your-own-dexcom-app)=
## If using G6 with Build Your Own Dexcom App

-   [Build Your Own Dexcom App](https://docs.google.com/forms/d/e/1FAIpQLScD76G0Y-BlL4tZljaFkjlwuqhT83QlFM5v6ZEfO7gCU98iJQ/viewform?fbzx=2196386787609383750) (BYODA) supports local broadcast to AAPS and/or xDrip+ (not for G5/ONE/G7 sensors!)

![BYODA broadcast options](../images/BYODA.png)

-   This app lets you use your Dexcom G6 with any Android smartphone.
-   Uninstall the original Dexcom app or patched Dexcom app if you used one of those previously (**do not stop** the currently running sensor)
-   Install the downloaded apk
-   Enter sensor code and transmitter serial no. in patched app.
-   In phone settings go to apps > Dexcom G6 > permissions > additional permissions and press 'Access Dexcom app'.
-   After short time BYODA should pick-up transmitter signal.

### Settings for AAPS

-   Select 'Dexcom App (patched)' in in [ConfigBuilder, BG Source](#Config-Builder-bg-source).

-   If you don't receive any values select any other data source, then re-select 'Dexcom App (patched)' to trigger the demand for permissions to establish the connection between AAPS and BYODA-broadcast.

### Settings for xDrip+

-   Select '640G/Eversense' as data source.
-   Command 'start sensor' must be performed in xDrip+ in order to receive values. This will not affect your current sensor controlled by Build Your Own Dexcom App.


(DexcomG6-troubleshooting-g6)=
## Troubleshooting G6 and ONE

### Dexcom G6/ONE specific troubleshooting

-   Scroll down to **Troubleshooting** [here](https://navid200.github.io/xDrip/docs/Dexcom_page.html).

### General troubleshooting

General Troubleshooting for CGMs can be found [here](#general-cgm-troubleshooting).

### New transmitter with running sensor

If you happen to change transmitter during a running sensor session you might try to remove the transmitter without damaging the sensor mount. A video can be found [here](https://navid200.github.io/xDrip/docs/Remove-transmitter.html). If you opt for [this solution](https://youtu.be/tx-kTsrkNUM) instead, you must be careful to avoid [damaging sensor contacts](https://navid200.github.io/xDrip/docs/Petroleum-jelly-in-Dexcom-G6-Sensor.html) with the strip.
