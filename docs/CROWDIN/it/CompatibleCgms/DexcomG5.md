- - -
orphan: true
- - -

# Dexcom G5

## Se usi un G5 con xDrip+

-   Puoi scaricare tranquillamente l'[ultimo APK (release)](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk) se non desideri nuove funzionalità specifiche.
-   Imposta xDrip+ con G5 seguendo [queste istruzioni](https://navid200.github.io/xDrip/docs/G5-Recommended-Settings.html).
-   Imposta xDrip+ leggendo la pagina delle [impostazioni xDrip+](../CompatibleCgms/xDrip.md).
-   Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

## Se usi un G5 con l'app Dexcom patchata

```{admonition} Legacy apps
:class: warning
Queste app non sono compatibili con le versioni recenti di Android.  
```

-   Scarica l'apk da <https://github.com/dexcomapp/dexcomapp>, e scegli la versione che si adatta alle tue esigenze (versione mg/dl o mmol/l, G5).

    -   La cartella 2.4 era per gli utenti di AAPS 2.5 e sopra.
    -   Apri <https://play.google.com/store/search?q=dexcom%20g5> sul tuo computer. La regione sarà visibile nell'URL.

    ![Regione nell'URL di Dexcom G5](../images/DexcomG5regionURL.PNG)

-   Forza l'arresto e disinstalla l'app Dexcom originale, se non già fatto.

-   Installa l'apk scaricato

-   Avvia il sensore

- Seleziona BYODA in [Configuratore Strutturale, Origine BG](#Config-Builder-bg-source).

-   Se vuoi utilizzare gli avvisi xDrip+ tramite trasmissione locale: nel menu hamburger xDrip+ > impostazioni > scegli la sorgente dati hardware > 640G / EverSense.
