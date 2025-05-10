# Sensori Compatibili

Questa sezione fornisce una breve panoramica di tutti i **sensori CGMs/FGMs** compatibili con **AAPS**.

*Suggerimento*: Se è possibile visualizzare i dati del glucosio nell'app xDrip+, puoi scegliere xDrip+ come sorgente dati di **glicemia** in **AAPS**.

* [Raccomandazioni generali](../CompatibleCgms/GeneralCGMRecommendation.md)
* [Lisciamento Dei Dati](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [Impostazioni xDrip+](../CompatibleCgms/xDrip.md)
* [Nightscout come fonte di valori di glicemia](../CompatibleCgms/CgmNightscoutUpload.md): Mentre è possibile utilizzare Nightscout come fonte di glicemia per il rilascio di insulina a circuito chiuso, **questo metodo non è raccomandato** a causa della sua dipendenza da dati mobili stabili o connettività Wi-Fi. Ciò significa che i tuoi dati di **glicemia** saranno ricevuti solo da **AAPS** quando hai una connessione online al tuo sito Nightscout. Per una configurazione più affidabile, utilizzare un sensore con trasmissione locale dal ricevitore (come elencato di seguito) a **AAPS**, è un'opzione molto migliore.

| CGM                                                    | Available [BG Sources](../SettingUpAaps/ConfigBuilder.md#bg-source)                                          |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [Dexcom G7](../CompatibleCgms/DexcomG7.md)             | xDrip+, DiaKEM app or [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html)                        |
| [Dexcom ONE+ and Stelo](../CompatibleCgms/DexcomG7.md) | xDrip+                                                                                                       |
| [Dexcom G6](../CompatibleCgms/DexcomG6.md)             | xDrip+ or BYODA                                                                                              |
| [Dexcom ONE](../CompatibleCgms/DexcomG6.md)            | xDrip+                                                                                                       |
| [Dexcom G5](../CompatibleCgms/DexcomG5.md)             | xDrip+                                                                                                       |
| [Libre 3/3+](../CompatibleCgms/Libre3.md)              | [Juggluco](https://www.juggluco.nl/Juggluco/libre3/) (with or without xDrip+)                                |
| [Libre 2/2+](../CompatibleCgms/Libre2.md)              | xDrip+ (EU only) or [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html) (with or without xDrip+) |
| [Libre 1](../CompatibleCgms/Libre1.md)                 | xDrip+, Glimp, Tomato o Diabox. Serve un trasmettitore                                                       |
| [Eversense](../CompatibleCgms/Eversense.md)            | xDrip+ o ESEL/Eversense App patchata                                                                         |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md)  | xDrip+ o MM640g + 600SeriesAndroidUploader App                                                               |
| [PocTech](../CompatibleCgms/PocTech.md)                | PocTech                                                                                                      |
| [Ottai](../CompatibleCgms/OttaiM8.md)                  | Ottai                                                                                                        |
| [Syai Tag](../CompatibleCgms/SyaiTagX1.md)             | Syai Tag                                                                                                     |
| Sibionics CGM                                          | [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html)                                              |

(GettingStarted-TrustedBGSource)=

## Trusted BG data sources

Regulatory approved **CGM**s for commercial hybrid closed loop systems are considered trusted **BG** data sources.

In order for **AAPS** to correctly identify them, the app sending **BG** readings must be able to provide sensor information.

Trusted data sources allow **SMB** delivery, all the time.

| Sensor                |                  CGM app                  |
| --------------------- |:-----------------------------------------:|
| Dexcom G5/G6          |      BYODA, xDrip+ (Direct, Native)       |
| Dexcom G7             | DiaKEM, xDrip+ (Direct, Native), Juggluco |
| Dexcom ONE/ONE+/Stelo |          xDrip+ (Direct, Native)          |
| Libre 2/2+ (EU)       | xDrip+, Juggluco (with or without xDrip+) |
| Libre 2/2+/3/3+       |     Juggluco (with or without xDrip+)     |

Note: xDrip+ Companion app and Followers are not trusted data sources.
