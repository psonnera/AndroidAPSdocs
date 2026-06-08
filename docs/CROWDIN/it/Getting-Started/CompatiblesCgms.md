# Sensori Compatibili

Questa sezione fornisce una breve panoramica di tutti i **sensori CGMs/FGMs** compatibili con **AAPS**.

*Suggerimento*: Se è possibile visualizzare i dati del glucosio nell'app xDrip+, puoi scegliere xDrip+ come sorgente dati di **glicemia** in **AAPS**.

* [Raccomandazioni generali](../CompatibleCgms/GeneralCGMRecommendation.md)
* [Lisciamento Dei Dati](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [Impostazioni xDrip+](../CompatibleCgms/xDrip.md)
* [Nightscout come fonte di valori di glicemia](../CompatibleCgms/CgmNightscoutUpload.md): Mentre è possibile utilizzare Nightscout come fonte di glicemia per il rilascio di insulina a circuito chiuso, **questo metodo non è raccomandato** a causa della sua dipendenza da dati mobili stabili o connettività Wi-Fi. Ciò significa che i tuoi dati di **glicemia** saranno ricevuti solo da **AAPS** quando hai una connessione online al tuo sito Nightscout. Per una configurazione più affidabile, utilizzare un sensore con trasmissione locale dal ricevitore (come elencato di seguito) a **AAPS**, è un'opzione molto migliore.

| CGM                                                                         | Sorgenti BG [disponibili](#Config-Builder-bg-source)                                                            |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [Dexcom G7](../CompatibleCgms/DexcomG7.md)                                  | BYODA, [xDrip+](../CompatibleCgms/xDrip.md) o [Juggluco](../CompatibleCgms/Juggluco.md)                         |
| [Dexcom ONE+ and Stelo](../CompatibleCgms/DexcomG7.md)                      | [xDrip+](../CompatibleCgms/xDrip.md)                                                                            |
| [Dexcom G6](../CompatibleCgms/DexcomG6.md)                                  | BYODA o [xDrip+](../CompatibleCgms/xDrip.md)                                                                    |
| [Dexcom ONE](../CompatibleCgms/DexcomG6.md)                                 | [xDrip+](../CompatibleCgms/xDrip.md)                                                                            |
| [Libre 3/3+](../CompatibleCgms/Libre3.md)                                   | [Juggluco](../CompatibleCgms/Juggluco.md) (con o senza xDrip+)                                                  |
| [Libre 2/2+](../CompatibleCgms/Libre2.md)                                   | [xDrip+](../CompatibleCgms/xDrip.md) (solo UE) o [Juggluco](../CompatibleCgms/Juggluco.md) (con o senza xDrip+) |
| [Libre 1](../CompatibleCgms/Libre1.md)                                      | [xDrip+](../CompatibleCgms/xDrip.md) o Diabox. Serve un trasmettitore                                           |
| [Eversense](../CompatibleCgms/Eversense.md)                                 | [xDrip+](../CompatibleCgms/xDrip.md) o App Eversense patchata ESEL                                              |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md)                       | [xDrip+](../CompatibleCgms/xDrip.md) o MM640g + App 600SeriesAndroidUploader                                    |
| [PocTech](../CompatibleCgms/PocTech.md)                                     | PocTech app                                                                                                     |
| Glunovo                                                                     | Glunovo App                                                                                                     |
| Intelligo                                                                   | Intelligo App                                                                                                   |
| [Ottai](../CompatibleCgms/OttaiM8.md)                                       | Ottai App                                                                                                       |
| [Syai](../CompatibleCgms/SyaiTagX1.md)                                      | Syai Tag App                                                                                                    |
| Sibionics CGM                                                               | [Juggluco](../CompatibleCgms/Juggluco.md) o App SI patchata                                                     |
| Sinocare                                                                    | Patched Sino App                                                                                                |
| [Caresens](../CompatibleCgms/Caresens.md), Simplera, iCan, LinX, SmartGuide | xDrip+ Companion App                                                                                            |

(GettingStarted-TrustedBGSource)=

## Trusted BG data sources

I **CGM** approvati dagli enti normativi per i sistemi commerciali a circuito chiuso ibrido sono considerati sorgenti di dati **glicemia** affidabili.

Affinché **AAPS** possa identificarli correttamente, l'app che invia le letture di **glicemia** deve essere in grado di fornire informazioni sul sensore.

Le sorgenti dati affidabili consentono sempre l'erogazione di **SMB**.

| Sensore               |                                                         App CGM                                                         |
| --------------------- |:-----------------------------------------------------------------------------------------------------------------------:|
| Dexcom G6             |                                           BYODA, xDrip+ (**Direct, Native**)                                            |
| Dexcom G7             |                 BYODA, xDrip+ (**Direct, Native**), </br>Juggluco (**xDrip broadcast** without xDrip+)                  |
| Dexcom ONE/ONE+/Stelo |                                               xDrip+ (**Direct, Native**)                                               |
| Libre 2/2+ (EU)       | xDrip+ (OOP2 **senza calibrazione**), </br>Juggluco (**xDrip broadcast** senza xDrip+, o **Libre patchato** con xDrip+) |
| Libre 2/2+/3/3+       |                      Juggluco (**xDrip broadcast** senza xDrip+, o **Libre patchato** con xDrip+)                       |
| Syai                  |                                                        Syai App                                                         |

**Nota: le app companion di xDrip+ e le modalità follower (incluso 640G/Eversense) non sono sorgenti di dati affidabili.**
