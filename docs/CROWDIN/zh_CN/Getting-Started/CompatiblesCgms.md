# 兼容的CGM设备

本节简要概述了所有与**AAPS**兼容的**持续血糖监测系统（CGMs）/扫描式血糖监测系统（FGMs）**。

*提示*：如果您可以在xDrip+应用程序中显示您的血糖数据，则可以在**AAPS**中选择xDrip+作为**BG（血糖）**来源。

* [一般建议](../CompatibleCgms/GeneralCGMRecommendation.md)
* [数据平滑](../CompatibleCgms/SmoothingBloodGlucoseData.md)
* [xDrip+设置](../CompatibleCgms/xDrip.md)
* [将Nightscout作为血糖来源](../CompatibleCgms/CgmNightscoutUpload.md)：虽然可以将Nightscout用作闭环胰岛素输注的血糖来源，但**并不推荐这种方法**，因为它依赖于稳定的移动数据或Wi-Fi连接。 这意味着，只有当您与Nightscout站点在线连接时，您的**CGM（持续葡萄糖监测系统）**数据才会被**AAPS**接收。 为了获得更可靠的设置，使用能够从接收器本地广播到**AAPS**的CGM（如下所列）是一个更好的选择。

| CGM                                                    | 可用的[血糖数据源](../SettingUpAaps/ConfigBuilder.md#bg-source)                                           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| [德康 G7](../CompatibleCgms/DexcomG7.md)                 | xDrip+, DiaKEM 或者 [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html)                 |
| [Dexcom ONE+ and Stelo](../CompatibleCgms/DexcomG7.md) | xDrip+                                                                                            |
| [Dexcom G6](../CompatibleCgms/DexcomG6.md)             | xDrip+ 或者 BYODA                                                                                   |
| [Dexcom ONE](../CompatibleCgms/DexcomG6.md)            | xDrip+                                                                                            |
| [Dexcom G5](../CompatibleCgms/DexcomG5.md)             | xDrip+                                                                                            |
| [Libre 3/3+](../CompatibleCgms/Libre3.md)              | [Juggluco](https://www.juggluco.nl/Juggluco/libre3/) (搭配/不搭配xDrip+)                               |
| [Libre 2/2+](../CompatibleCgms/Libre2.md)              | xDrip+ (仅限欧盟地区) or [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html) (搭配/不搭配xDrip+) |
| [Libre 1](../CompatibleCgms/Libre1.md)                 | xDrip+, Glimp, Tomato 或者 Diabox. 需要发射器                                                            |
| [Eversense](../CompatibleCgms/Eversense.md)            | xDrip+ 或 ESEL/Eversense 修补版应用                                                                     |
| [Enlite (MM640G/MM630G)](../CompatibleCgms/MM640g.md)  | xDrip+ or MM640g + 600Series 安卓上传程序 App                                                           |
| [PocTech](../CompatibleCgms/PocTech.md)                | PocTech                                                                                           |
| [Ottai](../CompatibleCgms/OttaiM8.md)                  | Ottai                                                                                             |
| [Syai Tag](../CompatibleCgms/SyaiTagX1.md)             | Syai Tag                                                                                          |
| 硅基 CGM                                                 | [Juggluco](https://www.juggluco.nl/Jugglucohelp/introhelp.html)                                   |

(GettingStarted-TrustedBGSource)=

## 可信血糖数据源

经监管部门批准的**持续葡萄糖监测系统（CGM）**，在商用混合闭环系统中被视为可信**血糖**数据源。

为了使**AAPS**正确识别它们，发送**血糖**读数的应用必须能够提供传感器信息。

可信数据源支持**SMB**全天候输注。

| 传感器                   |               CGM 应用                |
| --------------------- |:-----------------------------------:|
| Dexcom G5/G6          |      BYODA, xDrip+ (直连, 原生支持)       |
| 德康 G7                 | DiaKEM, xDrip+ (直连, 原生支持), Juggluco |
| Dexcom ONE/ONE+/Stelo |          xDrip+ (直连, 原生支持)          |
| Libre 2/2+ (EU)       |   xDrip+, Juggluco (搭配/不搭配xDrip+)   |
| Libre 2/2+/3/3+       |      Juggluco (搭配/不搭配 xDrip+)       |

注：xDrip+配套应用及关注者模式不被视为可信数据源。
