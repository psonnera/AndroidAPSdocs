# Dexcom G7 и ONE+


## Основательно и перспективно

Следует отметить, что системы G7 и ONE+, в отличие от G6, не сглаживают значения ГК ни в самом приложении, ни в считывателе. Подробнее об этом [здесь](https://www.dexcom.com/en-us/faqs/why-does-past-cgm-data-look-different-from-past-data-on-receiver-and-follow-app).

![G7 английский](../images/6fe30b84-227a-4bae-a9a5-527cee341dbf.png)

```{admonition} Smoothing method 
Read [Smoothing method](../CompatibleCgms/SmoothingBloodGlucoseData.md) suggestions to use for Dexcom G7/ONE+/Stelo
```

## 1. xDrip+ (прямое соединение с G7 или ONE+)

- Следуйте инструкциям отсюда: [xDrip+ G7](https://navid200.github.io/xDrip/docs/Dexcom/G7.html)
- В [Конфигураторе, Источник ГК](#Config-Builder-bg-source) выберите xDrip+.

- Отрегулируйте параметры xDrip+ в соответствии с пояснениями на странице настроек xDrip+  [настройки xDrip+](../CompatibleCgms/xDrip.md)

## 2.  Модифицированное приложение Dexcom G7 (DiAKEM)

**Note: AAPS 3.2.0.0 or higher is required! Not available for ONE+.**

### Установите новое модифицированное (!) приложение G7 и запустите сенсор

WARNING --- [BYODA](https://docs.google.com/forms/d/e/1FAIpQLScD76G0Y-BlL4tZljaFkjlwuqhT83QlFM5v6ZEfO7gCU98iJQ/viewform?fbzx=2196386787609383750)--- There are reported issues **AAPS** receiving no BG data when using either BYODA & DiaKEM as its data source. Users are recommended to use [X-Drip+](https://androidaps.readthedocs.io/en/latest/CompatibleCgms/xDrip.html) as **AAPS'** BG data source until this issue has been resolved.


A patched Dexcom G7 app (DiaKEM) gives access to the Dexcom G7 data. This is not the BYODA app as this app can not receive G7 data at the moment.

- Удалите оригинальное приложение Dexcom, если вы его использовали прежде (Рабочая сессия сенсора может продолжаться - запишите код сенсора перед удалением приложения!)

- Скачайте и установите модифицированное приложение (patched.apk) [по ссылке](https://github.com/authorgambel/g7/releases).

- Введите код сенсора в модифицированном приложении.

- Следуйте общим рекомендациям по гигиене НМГ и установке сенсора, которые можно найти [здесь](../CompatibleCgms/GeneralCGMRecommendation.md).

- После фазы прогрева, данные ГК отображаются как обычно в приложении G7.

### Конфигурация в AAPS

- Выберите самостоятельно собранное приложение 'BYODA' в [конфигураторе, источник ГК](#Config-Builder-bg-source)- даже если это не BYODA!

- Если AAPS не получает данных ГК, переключитесь на другой источник ГК, а затем снова на 'BYODA'.

## 3. xdrip+ (режим спутника)

-   Скачайте и установите xDrip+: [xDrip](https://github.com/NightscoutFoundation/xDrip)
- В качестве источника данных в Xdrip должен быть выбран "Companion App" в разделе Менее распространенные настройки > Настройки Bluetooth > поставьте галочку рядом с "Companion Bluetooth".
-   В [Конфигураторе, Источник ГК](#Config-Builder-bg-source) выберите xDrip+.

-   Отрегулируйте параметры xDrip+ в соответствии с пояснениями на странице настроек xDrip+  [настройки xDrip+](../CompatibleCgms/xDrip.md)

## 4. Juggluco

Version 9.0+ required

- Отключите приложение, ранее подключенное к датчику: удалите приложение или выполните «Остановить принудительно» Отключите разрешение для"Устройств поблизости" в настройках приложения. Ограничьте использование батареи в приложении.

- Забудьте датчик в настройках Bluetooth: в настройках Android найдите датчик в прикрепленных устройствах и выберите "Forget." Названия датчиков Dexcom G7 начинаются с DXCM.

- Избегайте вмешательства других датчиков: Держите старые сенсоры Dexcom вне диапазона Bluetooth.

- Подключите датчик G7 к Juggluco: Откройте Juggluco → Левое меню → Фото. Сканируйте матрицу штрих-кода на аппликаторе сенсора G7. Дайте Juggluco до 5 минут, чтобы найти сенсор.

- Требования к сопряжению: Согласитесь с подключением датчика к Juggluco. Убедитесь, что экран не заблокирован во время подключения. Если сопряжение не удалось, подождите 5 минут и повторите попытку.

- Исключение: Часы на Wear OS могут сопрягаться без нажатия кнопки подтверждения.
