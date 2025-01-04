# Compatible CGMs

This section provides a brief overview of all compatible **CGMs/FGMs** with **AAPS**.

*Tip*: If you can display your glucose data in xDrip+ app, you can choose xDrip+ as **BG** source in **AAPS**.

* [General recommendations](../CompatibleCgms/GeneralCGMRecommendation.md)
* [Data Smoothing](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [xDrip+Settings](../CompatibleCgms/xDrip.md)
* [Nightscout as BG Source](../CompatibleCgms/CgmNightscoutUpload.md): While it's possible to use Nightscout as a BG source for closed-loop insulin delivery, **this method is not recommended** due to its reliance on stable mobile data or Wi-Fi connectivity. This means your **CGM** data would only be received by **AAPS** when you have an online connection to your Nightscout site. For a more reliable set up, using a CGM with local broadcast from the receiver (as listed below) to **AAPS**, is a much better option.

| CGM                                                   | Available [BG Sources](../SettingUpAaps/ConfigBuilder.md#bg-source) |
| ----------------------------------------------------- | ------------------------------------------------------------------- |
| [Dexcom G7 and ONE+](../CompatibleCgms/DexcomG7.md)   | xDrip+, DiaKEM app or Juggluco                                      |
| [Dexcom G6 and ONE](../CompatibleCgms/DexcomG6.md)    | xDrip+ or BYODA (only G6)                                           |
| [Dexcom G5](../CompatibleCgms/DexcomG5.md)            | xDrip+                                                              |
| [Libre 3](../CompatibleCgms/Libre3.md)                | xDrip+ (no transmitter) or Juggluco                                 |
| [Libre 2](../CompatibleCgms/Libre2.md)                | xDrip+ (no transmitter) or Juggluco                                 |
| [Libre 1](../CompatibleCgms/Libre1.md)                | xDrip+, Glimp, Tomato or Diabox. Need a transmitter                 |
| [Eversense](../CompatibleCgms/Eversense.md)           | xDrip+ or ESEL/Eversense patched App                                |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md) | xDrip+ or MM640g + 600SeriesAndroidUploader App                     |
| [PocTech](../CompatibleCgms/PocTech.md)               | PocTech                                                             |
| [Ottai](../CompatibleCgms/OttaiM8.md)                 | Ottai                                                               |
| [Syai Tag](../CompatibleCgms/SyaiTagX1.md)            | Syai Tag                                                            |
| Sibionics CGM                                         | Juggluco                                                            |
