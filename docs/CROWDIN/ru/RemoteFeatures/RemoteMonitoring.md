# Удаленный мониторинг

![Monitoring children](../images/KidsMonitoring.png)

AAPS предлагает несколько опций для удаленного мониторинга детей, а также позволяет отправлять удаленные команды. Конечно, его можно использовать для мониторинга партнера или друга.

## Функции

- Помпа ребенка управляется телефоном ребенка с помощью AAPS.
- Родители могут дистанционно следить за всеми данными, такими как уровень глюкозы, активные углеводы, активный инсулин и т. д. с помощью приложения **AAPSClient** на своем телефоне. Настройки должны быть одинаковыми в AAPS и AAPSClient.
- Родители могут слышать оповещения с помощью приложения **xDrip в режиме слежения (follower)** на своем телефоне.
- Remote control of AAPS using [SMS Commands](../RemoteFeatures/SMSCommands.md) secured by two-factor authentication.
- Remote control through AAPSClient app is only recommended if your synchronization is working well (ie. you don’t see unwanted data changes like self modification of TT, TBR etc) see [release notes for Version 2.8.1.1](../Maintenance/ReleaseNotes.md#version-2811) for further details.

## Инструменты и приложения для удаленного мониторинга

- [Nightscout](https://nightscout.github.io/) в интернет-браузере (в основном отображение данных)
- * Приложение AAPSClient-это урезанная версии AAPS для слежения, переключения профилей, постановки временных целей TT и ввода углеводов. Существует два приложения для загрузки:  [AAPSClient & AAPSClient2](https://github.com/nightscout/AndroidAPS/releases/). Единственное отличие-это название приложения. Таким образом имеется возможность установить приложение дважды на одном телефоне, чтобы следить за 2 разными лицами/nightscout.
- Приложение Dexcom Follow, если вы используете оригинальное приложение Dexcom (только ГК)
- [xDrip+](../CompatibleCgms/xDrip.md) in follower mode (mainly BG values and **alarms**)
- [Sugarmate](https://sugarmate.io/) или [Spike](https://spike-app.com/) на iOS (в основном значения ГК и <1>оповещения</1>)
- Некоторые пользователи считают, что инструменты полного доступа к телефону ребенка вроде [TeamViewer](https://www.teamviewer.com/) полезны для решения ситуативных проблем

## Опции для смарт-часов

Смарт-часы бывают очень полезным инструментом для управления AAPS у детей. Возможны несколько различных конфигураций:

- Если AAPSClient установлен на родительский телефон,, приложение [AAPSClient WearOS](https://github.com/nightscout/AndroidAPS/releases/) может быть установлено на смарт-часах, сопряженных с родительским телефоном. На них будет отображаться текущая ГК, статус замкнутого цикла, возможность вписать углеводы, временные цели и изменения профиля. Возможности ввести болюс с приложения на WearOS не будет.
- Alternatively, the [AAPS WearOS app](../UsefulLinks/WearOsSmartwatch.md) can be built and installed on a compatible smartwatch, connected to the kid's phone but worn by the parent. В него войдут все перечисленные выше функции, а также возможность подать болюс. Эта конфигурация позволяет родителям подавать инсулин без обращения к телефону ребенка.

## Важные факторы

- Setting the correct [treatment factors](../UsefulLinks/FAQ.md#how-to-begin) (basal rate, DIA, ISF...) is difficult for kids, especially when growth hormones are involved.
- Настройки должны быть одинаковыми в AAPS и AAPSClient.
- Учитывайте временной разрыв между ведущим телефоном и ведомым из-за времени на загрузку и выгрузку, а также из-за того, что ведущий телефон AAPS начнет выгрузку только после выполнения цикла.
- Так что не торопитесь, установите их правильно и проверьте их в реальной жизни когда ребенок рядом прежде чем начать дистанционный контроль и дистанционное лечение. Школьные каникулы могут быть хорошим временем для этого.
- Определите план действий на тот случай, когда дистанционный контроль не работает (напр. проблемы с сетью).
- Удаленный мониторинг и терапия могут быть особенно нужными в детском саду и начальной школе. Но убедитесь, что учителя и воспитатели в курсе плана лечения вашего ребенка. Примеры таких планов лечения можно найти в [разделе файлов пользователей AAPS](https://www.facebook.com/groups/AndroidAPSUsers/files/) на Facebook.
- Важно всегда держать телефон ребенка в диапазоне связи с помпой и мониторингом. Это может быть особенно сложно если дети маленькие. Существует множество решений, популярный вариант - специальный пояс [SPI Belt](https://spibelt.com/collections/kids-belts)
