# Compatible CGMs

В этом разделе представлена краткая информация о всех поддерживаемых **AAPS** **системах НМГ** (непрерывного мониторинга глюкозы) **и ФМГ** (флеш-мониторинга глюкозы).

*Совет*: если вы уже видите свой сахар в приложении xDrip+, вы можете выбрать его как **источник СК** в **AAPS**.

* [Общие рекомендации](../CompatibleCgms/GeneralCGMRecommendation.md)
* [Сглаживание данных](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [Настройки xDrip+](../CompatibleCgms/xDrip.md)
* [Nightscout как источник СК](../CompatibleCgms/CgmNightscoutUpload.md): Хотя использовать Nightscout в качестве источника СК для замкнутого цикла возможно, **этот метод использовать не рекомендуется** из-за того, что он полагается на стабильность мобильного интернета или Wi-Fi. Это означает, что данные с вашего **НМГ** будут приниматься **AAPS** только лишь при наличии соединения с вашим сайтом Nightscout. В качестве более надежной конфигурации рекомендуется использовать НМГ с локальной трансляцией в **AAPS** из источников, описанных ниже.

| CGM /  НМГ                                            | Доступные [Источники ГК](../SettingUpAaps/ConfigBuilder.md#bg-source) |
| ----------------------------------------------------- | --------------------------------------------------------------------- |
| [Dexcom G7 и ONE+](../CompatibleCgms/DexcomG7.md)     | xDrip+, DiaKEM app or Juggluco                                        |
| [Dexcom G6 и ONE](../CompatibleCgms/DexcomG6.md)      | xDrip+ or BYODA (only G6)                                             |
| [Работа с Dexcom G5](../CompatibleCgms/DexcomG5.md)   | xDrip +                                                               |
| [Libre 3](../CompatibleCgms/Libre3.md)                | xDrip+ (no transmitter) or Juggluco                                   |
| [Libre 2](../CompatibleCgms/Libre2.md)                | xDrip+ (no transmitter) or Juggluco                                   |
| [Libre 1](../CompatibleCgms/Libre1.md)                | xDrip+, Glimp, Tomato или Diabox. Need a transmitter                  |
| [Eversense](../CompatibleCgms/Eversense.md)           | xDrip+ or ESEL/Eversense patched App                                  |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md) | xDrip+ или MM640g + приложение 600SeriesAndroidUploader               |
| [Poctech](../CompatibleCgms/PocTech.md)               | Poctech                                                               |
| [Ottai](../CompatibleCgms/OttaiM8.md)                 | Ottai                                                                 |
| [Syai Tag](../CompatibleCgms/SyaiTagX1.md)            | Syai Tag                                                              |
| Sibionics CGM                                         | Juggluco                                                              |
