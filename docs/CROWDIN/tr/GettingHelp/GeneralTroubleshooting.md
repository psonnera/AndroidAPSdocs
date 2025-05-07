# Troubleshooting

Sorun giderme bilgilerini viki'deki birçok sayfada bulabilirsiniz. Bu sayfa, sorununuzu çözecek bilgileri bulmanıza yardımcı olacak bir bağlantılar topluluğudur.

Additional useful information might also be available in the [FAQ](../UsefulLinks/FAQ.md).

## AAPS app

### Yapım & güncelleme

* [Kayıp keystore](#troubleshooting_androidstudio-lost-keystore)
* [Android Studio'da Sorun Giderme](TroubleshootingAndroidStudio)

### Installing

You may see a Google Play Protect warning that the app is unsafe, was built for older Android versions and doesn't include latest privacy protections.

Ignore it: More details, Install anyway.

![Google Play Protect warning](../images/troubleshooting/InstallGPP.png)

### Ayarlar
* Profile

  ![Hata: Bazal saatlere göre ayarlanamadı](../images/Screen_DifferentPump.png)

* [Pompa - farklı pompadan alınan veriler](#update30-failure-message-data-from-different-pump)

  ![Hata mesajı: Farklı pompadan gelen veriler](../images/BasalNotAlignedToHours2.png)

* [Nightscout Client](../GettingHelp/TroubleshootingNsClient.md)

### Kullanım
* [Yanlış karbonhidrat değerleri](#CobCalculation-detection-of-wrong-cob-values)

   ![Hata: Yavaş karbonhidrat emilimi](../images/Calculator_SlowCarbAbsorption.png)

* [SMS Komutları](#SMSCommands-troubleshooting)

### Sık bluetooth bağlantı sorunları

Bu, çeşitli pompalarda olabilir. AAPS'i pil optimizasyonunun dışında tutmanın yanı sıra, sistem bluetooth uygulamasını da pil optimizasyonunun dışında tutabilirsiniz. Bu, bazı durumlarda yardımcı olabilir. Kullandığınız telefona bağlı olarak, bluetooth ayarları farklı olacaktır.

Bunları belirli android telefonlarda nasıl bulacağınıza dair örnekler aşağıda verilmiştir.


#### Pixel telefonlar (stok android)

* Android ayarlarına gidin, "Uygulamalar" ı seçin.

  ![Android Ayarları¦Uygulamalar](../images/troubleshooting/pixel/01_androidsettings.png)

* "Tüm uygulamaları gör" seçeneğini seçin

  ![Tüm uygulamaları göster](../images/troubleshooting/pixel/02_apps.png)

* Sağdaki menüden "Sistemi göster" uygulamalarını seçin.

  ![Sistem uygulamalarını göster](../images/troubleshooting/pixel/03_allapps.png)

* Şimdi "Bluetooth" uygulamasını arayın ve seçin.

  ![Bluetooth uyg.](../images/troubleshooting/pixel/03_bluetooth.png)

* "Uygulama pil kullanımı"na tıklayın ve "Optimize edilmedi"yi seçin.

  ![BT Pil optimizasyonu](../images/troubleshooting/pixel/04_btunrestricted.png)


#### Samsung telefonlar

* Android ayarlarına gidin, "Uygulamalar" ı seçin

* Sıralama algoritmasını değiştiren simgede (1), "Sistem uygulamalarını göster"i (2) seçin.

  ![Uyg. Filtresi](../images/troubleshooting/samsung/Samsung01_Apps.png)

  ![Sistem uygulamalarını göster](../images/troubleshooting/samsung/Samsung02_ShowSystemApps.png)

* Şimdi bluetooth uygulamasını arayın ve ayarları görmek için seçin.

  ![Bluetooth Uyg.](../images/troubleshooting/samsung/Samsung03_BtApp.png)

* "Pil"i seçin

  ![Pil](../images/troubleshooting/samsung/Samsung04_Battery.png)

* "Optimize edilmedi" olarak ayarlayın

  ![Optimize edilmedi](../images/troubleshooting/samsung/Samsung05_NotOptimized.png)


## CGM

* [General](#general-cgm-troubleshooting)
* [Dexcom G6](#DexcomG6-troubleshooting-g6)
* [Libre 3](#libre3-experiences-and-troubleshooting)
* [Libre 2](#Libre2-experiences-and-troubleshooting)
* [xDrip - CGM verisi yok](#xdrip-identify-receiver)
* [xDrip - Dexcom sorun giderme](#xdrip-troubleshooting-dexcom-g5-g6-and-xdrip)

## Pompalar

* [DanaRS](#DanaRS-Insulin-Pump-dana-rs-specific-errors)
* [Accu-Chek Combo genel](../CompatiblePumps/Accu-Chek-Combo-Tips-for-Basic-usage.md)
* [Accu-Chek Insight](#Accu-Chek-Insight-Pump-insight-specific-errors)
* [Medtronic + RileyLink](#MedtronicPump-what-to-do-if-i-loose-connection-to-rileylink-and-or-pump)

## Telefonlar

* [Jelly](../CompatiblePhones/Jelly.md)
* [Huawei bluetooth & pil optimizasyonu](../CompatiblePhones/Huawei.md)

## Akıllı saatler

* [Troubleshooting Wear app](#Watchfaces-troubleshooting-the-wear-app)
