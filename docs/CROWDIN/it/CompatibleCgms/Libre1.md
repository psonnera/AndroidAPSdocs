- - -
orphan: true
- - -

# Freestyle Libre 1

Per utilizzare il tuo Libre come CGM, ottenendo nuovi valori di glicemia ogni 5 minuti senza dover eseguire la scansione del sensore, è necessario acquistare un ponte NFC a Bluetooth (dispositivi disponibili in commercio, in base al progetto obsoleto [LimiTTer](https://github.com/JoernL/LimiTTer)).

```{admonition} Libre 2, Libre 1 US and Libre Pro
:class: warning
Verifica che il bridge e l'app che vuoi usare siano compatibili con il tuo sensore.  
```

Sul mercato sono disponibili diversi ponti:

-   [MiaoMiao Reader](https://www.miaomiao.cool/) (versione 1, 2 o 3) disponibile anche su AliExpress.
-   [Blucon Nightrider](https://www.ambrosiasys.com/our-products/blucon/) (le versioni recente del firmware potrebbero non essere compatibile con tutte le applicazioni, l'app del fornitore non trasmette dati a AAPS)
-   [Bubble (o Bubble Mini)](https://www.bubblesmartreader.com/) da rivenditori europei ([Bubblan](https://www.bubblan.org/), [BubbleShop](https://bubbleshop.eu/)) o per gli utenti russi [qui](https://vk.com/saharmonitor/). Disponibile anche su AliExpress.
-   Atom per gli utenti russi.

Storicamente è possibile utilizzare un orologio specifico, Sony Smartwatch 3 (SWR50) che ha un chip NFC che può essere abilitato e utilizzato come collettore NFC. Tuttavia i ponti NFC a Bluetooth elencati sopra offrono una soluzione meno complessa e sono utilizzati dalla maggior parte di quelli che vogliono utilizzare il loro Libre 1 (non US) come CGM.

-   Sony Smartwatch 3 (SWR50) <https://github.com/pimpimmi/LibreAlarm/wiki/>

Per ora, utilizzando Libre 1 come origine dati, non è possibile attivare le opzioni “Abilita SMB sempre” e “Abilita SMB dopo i carboidrati” per l'algoritmo SMB. I valori della glicemia del Libre 1 non sono abbastanza omogenei per poterli usare in modo sicuro. Per maggiori dettagli, vedi [Smoothing dei dati glicemici](../CompatibleCgms/SmoothingBloodGlucoseData.md).

## 1. Usando xDrip+

-   xDrip+ supporta Miaomiao, Bubble, Blucon, Atom e LibreAlarm.
-   Puoi scaricare tranquillamente l'[ultimo APK (stabile)](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk) a meno che tu non abbia bisogno di funzionalità più recenti, caso in cui dovresti usare l'ultimo [Nightly Snapshot](https://github.com/NightscoutFoundation/xDrip/releases).
-   Segui le istruzioni di configurazione nella [pagina delle impostazioni di xDrip+](../CompatibleCgms/xDrip.md).
-    You also need OOP2 for Libre 1 US (and Libre 2 EU).
-   Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

(libre1-using-glimp)=
## 2. Usando Glimp

-   Glimp supporta Miaomiao, Blucon e Bubble per Libre 1 e Libre 2 EU.
-   Avrai bisogno di Glimp versione 4.15.57 o più recente. Le versioni precedenti non sono supportate.
-   Installa [Glimp](https://play.google.com/store/apps/details?id=it.ct.glicemia).
-   Seleziona Glimp in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source)

(libre1-using-tomato)=
## 3. Usando Tomato

- Tomato è l'app del fornitore di Miaomiao.
- Installa [Tomato](http://tomato.cool/#download_page) e segui le [istruzioni](http://tomato.cool/how-to-broadcast-data-to-android-aps/tips/) del fornitore.
- Seleziona Tomato in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).

## 4. Usando Diabox

- Diabox è l'app del fornitore per Bubble.
- Installa [Diabox](https://t.me/s/DiaboxApp). Nelle Impostazioni, Integrazione, abilita Condividi i dati con altre applicazioni.

![Diabox](../images/Diabox. png)

- Seleziona xDrip+ in [Configuratore strutturale, Origine BG](#Config-Builder-bg-source).
