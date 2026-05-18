# Freestyle Libre 1

Per utilizzare il tuo Libre come CGM, ottenendo nuovi valori di glicemia ogni 5 minuti senza dover eseguire la scansione del sensore, è necessario acquistare un ponte NFC a Bluetooth (dispositivi disponibili in commercio, in base al progetto obsoleto [LimiTTer](https://github.com/JoernL/LimiTTer)).

```{admonition} Libre 2, Libre 1 US and Libre Pro
:class: warning
Verifica che il bridge e l'app che vuoi usare siano compatibili con il tuo sensore.  
```

Some bridges are still available on the market:

-   [MiaoMiao Reader](https://www.miaomiao.cool/) (versione 1, 2 o 3) disponibile anche su AliExpress.
-   [Bubble / Mini / Nano](https://www.bubblesmartreader.com/) from European vendors ([BubbleShop](https://bubbleshop.eu/)) or for Russian users [here](https://vk.com/saharmonitor/). Disponibile anche su AliExpress.
-   Atom per gli utenti russi.

## 1. Usando xDrip+

-   xDrip+ supporta Miaomiao, Bubble, Blucon, Atom e LibreAlarm.
-   Puoi scaricare tranquillamente l'[ultimo APK (stabile)](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk) a meno che tu non abbia bisogno di funzionalità più recenti, caso in cui dovresti usare l'ultimo [Nightly Snapshot](https://github.com/NightscoutFoundation/xDrip/releases).
-   Segui le istruzioni di configurazione nella [pagina delle impostazioni di xDrip+](../CompatibleCgms/xDrip.md).
-    Hai anche bisogno di OOP2 per Libre 1 US (e Libre 2 EU).
-   Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

## 2. Usando Diabox

- Diabox è l'app del fornitore per Bubble.
- Installa [Diabox](https://t.me/s/DiaboxApp). Nelle Impostazioni, Integrazione, abilita Condividi i dati con altre applicazioni.

![Diabox](../images/Diabox. png)

- Select xDrip+ in [ConfigBuilder, BG Source](#Config-Builder-bg-source).
