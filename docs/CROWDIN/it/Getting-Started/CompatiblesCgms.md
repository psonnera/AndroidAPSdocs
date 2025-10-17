# Sensori Compatibili

Questa sezione fornisce una breve panoramica di tutti i **sensori CGMs/FGMs** compatibili con **AAPS**.

*Suggerimento*: Se è possibile visualizzare i dati del glucosio nell'app xDrip+, puoi scegliere xDrip+ come sorgente dati di **glicemia** in **AAPS**.

* [Raccomandazioni generali](../CompatibleCgms/GeneralCGMRecommendation.md)
* [Lisciamento Dei Dati](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [Impostazioni xDrip+](../CompatibleCgms/xDrip.md)
* [Nightscout come fonte di valori di glicemia](../CompatibleCgms/CgmNightscoutUpload.md): Mentre è possibile utilizzare Nightscout come fonte di glicemia per il rilascio di insulina a circuito chiuso, **questo metodo non è raccomandato** a causa della sua dipendenza da dati mobili stabili o connettività Wi-Fi. Ciò significa che i tuoi dati di **glicemia** saranno ricevuti solo da **AAPS** quando hai una connessione online al tuo sito Nightscout. Per una configurazione più affidabile, utilizzare un sensore con trasmissione locale dal ricevitore (come elencato di seguito) a **AAPS**, è un'opzione molto migliore.

| CGM                                                    | Available [BG Sources](#Config-Builder-bg-source)                                                                    |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| [Dexcom G7](../CompatibleCgms/DexcomG7.md)             | [xDrip+](../CompatibleCgms/xDrip.md), DiaKEM app or [Juggluco](../CompatibleCgms/Juggluco.md)                        |
| [Dexcom ONE+ and Stelo](../CompatibleCgms/DexcomG7.md) | [xDrip+](../CompatibleCgms/xDrip.md)                                                                                 |
| [Dexcom G6](../CompatibleCgms/DexcomG6.md)             | [xDrip+](../CompatibleCgms/xDrip.md) or BYODA                                                                        |
| [Dexcom ONE](../CompatibleCgms/DexcomG6.md)            | [xDrip+](../CompatibleCgms/xDrip.md)                                                                                 |
| [Dexcom G5](../CompatibleCgms/DexcomG5.md)             | [xDrip+](../CompatibleCgms/xDrip.md)                                                                                 |
| [Libre 3/3+](../CompatibleCgms/Libre3.md)              | [Juggluco](../CompatibleCgms/Juggluco.md) (with or without xDrip+)                                                   |
| [Libre 2/2+](../CompatibleCgms/Libre2.md)              | [xDrip+](../CompatibleCgms/xDrip.md) (EU only) or [Juggluco](../CompatibleCgms/Juggluco.md) (with or without xDrip+) |
| [Libre 1](../CompatibleCgms/Libre1.md)                 | [xDrip+](../CompatibleCgms/xDrip.md), Glimp, Tomato or Diabox. Serve un trasmettitore                                |
| [Eversense](../CompatibleCgms/Eversense.md)            | [xDrip+](../CompatibleCgms/xDrip.md) or ESEL/Eversense patched App                                                   |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md)  | [xDrip+](../CompatibleCgms/xDrip.md) or MM640g + 600SeriesAndroidUploader App                                        |
| [PocTech](../CompatibleCgms/PocTech.md)                | PocTech                                                                                                              |
| [Ottai](../CompatibleCgms/OttaiM8.md)                  | Ottai                                                                                                                |
| [Syai Tag](../CompatibleCgms/SyaiTagX1.md)             | Syai Tag                                                                                                             |
| Sibionics CGM                                          | [Juggluco](../CompatibleCgms/Juggluco.md)                                                                            |

(GettingStarted-TrustedBGSource)=

## Trusted BG data sources

Regulatory approved **CGM**s for commercial hybrid closed loop systems are considered trusted **BG** data sources.

In order for **AAPS** to correctly identify them, the app sending **BG** readings must be able to provide sensor information.

Trusted data sources allow **SMB** delivery, all the time.

| Sensor                |                                                        CGM app                                                         |
| --------------------- |:----------------------------------------------------------------------------------------------------------------------:|
| Dexcom G5/G6          |                                           BYODA, xDrip+ (**Direct, Native**)                                           |
| Dexcom G7             |                DiaKEM, xDrip+ (**Direct, Native**), </br>Juggluco (**xDrip broadcast** without xDrip+)                 |
| Dexcom ONE/ONE+/Stelo |                                              xDrip+ (**Direct, Native**)                                               |
| Libre 2/2+ (EU)       | xDrip+ (OOP2 **no calibration**), </br>Juggluco (**xDrip broadcast** without xDrip+, or **Patched Libre** with xDrip+) |
| Libre 2/2+/3/3+       |                    Juggluco (**xDrip broadcast** without xDrip+, or **Patched Libre** with xDrip+)                     |

**Note: xDrip+ Companion apps and Follower modes (includes 640G/Eversense) are not trusted data sources.**
