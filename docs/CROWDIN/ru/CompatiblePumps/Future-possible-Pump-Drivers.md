* * *

orphan: true

* * *

# Вероятные будущие драйверы для помп

Это список некоторых помп и состояние их поддержки в системах ИПЖ, а затем статус в AAPS. В конце есть перечень того, что требуется, чтобы помпа стала совместимой с системами ИПЖ

## Помпы, способные к работе в качестве компонента ИПЖ

### Kaleido ([Домашняя страница](https://www.hellokaleido.com/))

**Loop status:** Pump is a Loop candidate, but protocol is unknown at the time. No interest in open source from the vendor.

**Требования к оборудованию для AAPS:** Никаких. It seems to be BT enabled.

### Tandem: t:slim X2 ([Домашняя страница](https://www.tandemdiabetes.com/))

**Статус реализации:** Пока не пригодна.

Хотя в прошлом компания не допускала контроля помпы с внешних устройств, за последние несколько лет правила изменились. Компания решила обновить помпу t:slim X2 и допустить возможность удаленного контроля (через приложение t:connect), это означает, что мы можем рассчитывать на управление помпой через AAPS в будущем. В ближайшее время планируется обновить прошивку помпы (в этом или в следующем году, а затем появится беструбочная помпа t:sport). Пока нет информации о том, какие операции можно будет выполнять на t:connect (разумеется, подача болюса, а все остальное пока неизвестно).

**Требования к оборудованию для AAPS:** Никаких. It seems to be BT enabled.

### Tandem: t:Mobi & t:slim X3 & t:Mobi Tubeless ([Домашняя страница](https://www.tandemdiabetes.com/about-us/pipeline))

**Статус реализации:** Все 3 помпы будут кандидатами в ИПЖ.

Awaiting release of t:mobi in Europe (other two are not yet released anywhere). Development of AAPS t:mobi support has already started and should be available by end of 2025 (see more info on Discord).

**Требования к оборудованию для AAPS:** Никаких. It seems to be BT enabled.

### Инсулиновая помпа Willсare ([ Домашняя страница ](http://shinmyungmedi.com/en/))

**Статус реализации:** В настоящий момент не является кандидатом, но их сотрудники связывались с нами, и они заинтересованы в том, чтобы сделать помпу пригодной для ИПЖ (на данный момент в помпе отсутствуют команды get/set profile).

**Требования к оборудованию для AAPS:** Никаких. It seems to be BT enabled.

** Комментарии: ** Поскольку компания заинтересована в интеграции с AAPS, они могут сами предпринять необходимые действия.

## Помпы, снятые с производства (компании больше не работают)

### Animas Vibe

### Animas Ping

### Cellnovo

### Accu-Chek Insight

**Comments:** End of support March 2025.

## Помпы, неспособные к работе в качестве компонента ИПЖ

### Medtronic Bluetooth

**Комментарии:** Medtronic [отказался](https://www.tidepool.org/blog/tidepool-loop-partner-update-ace-pumps).

### Accu-Chek Solo

**Comments:** No community success in communicating with the Solo pump.

### Ypsomed Pump

**Comments:** Ypso added very heavy 3rd party encryption.

## Требования к пригодности помп для ИПЖ

**Предварительные условия**

- Помпа должна поддерживать дистанционное управление. (блутус, радио и т. п.)
- Протокол взломан/документирован/и т. д.

**Минимальные требования**

- Устанавливать временную скорость базала
- Получать сведения о состоянии
- Отменять временную базальную скорость

**Для oref1(SMB) или болюсов:**

- Настраивать ввод болюса

**Желательно иметь**

- Отмену болюса
- Получать профиль базала (почти требование)
- Устанавливать профиль базала (хорошо иметь)
- Чтение истории 

**Другое (не обязательно, но желательно)**

- Настраивать пролонгированный болюс
- Отменять пролонгированный болюс
- Чтение истории
- Чтение суммарной суточной дозы инсулина TDD

### Поддержка других помп

Если у вас есть какие-либо другие помпы, для которых вы хотите увидеть статус, пожалуйста, свяжитесь со мной (@andyrozman на gitter).