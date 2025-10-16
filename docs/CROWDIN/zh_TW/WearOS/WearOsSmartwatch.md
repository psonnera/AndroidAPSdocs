# 在你的 Wear OS 手錶上設置 AAPS

下面的說明適用於你需要建置的**AAPS Wear** apk（如果尚未建置，請參閱[這裡](../WearOS/BuildingAapsWearOS.md)），因為你已經建置了手機的**AAPS** apk。

你還可以使用一些信息用於**AAPSClient**和**PumpControl**的**Wear** apk，這些信息可以直接在[GitHub](https://github.com/nightscout/AndroidAPS/releases/tag/3.2.0.4)中找到。 每個**Wear**應用都將與其一致的手機應用進行通信。 例如：**AAPSClient Wear**應用可用於顯示**AAPSClient**資料，而不是**AAPS**資料。

## Wear OS 版本和相容性

### Wear OS 3

使用[Wear Installer 2](https://youtu.be/abgN4jQqHb0?si=5L7WUeYMSd_8IdPV)、Easy Fire Tools（稍後說明）或 ADB 安裝**AAPS Wear** apk。  
在**AAPS Wear**操作上沒有限制。

(BuildingAapsWearOs-WearOS5)=

### Wear OS 4 和 Galaxy 手錶更新至 Wear OS 5

範例：GW4、GW5、GW6

使用[Wear Installer 2](https://youtu.be/abgN4jQqHb0?si=5L7WUeYMSd_8IdPV)安裝**AAPS Wear** apk。  
在**AAPS Wear**操作上沒有限制。

```{admonition} Android Wear OS 5
翻譯為臺灣常用的繁體中文如下：

:class: warning
**韌體更新極可能會破壞 AAPS 錶面：請停止錶面更新功能**。
```

### 工廠預裝 Wear OS 5 的 Galaxy 手錶

 範例：GW7、GW Ultra

```{admonition} Android Wear OS 5
:class: warning
安裝 AAPS 錶面必須在安裝 Wear 應用程式後，使用 [Wear Installer 2](https://www.youtube.com/watch?v=yef_qGvcCnk) 完成。<br> 若不小心將錶面切換為其他樣式，則需重複上述安裝程序。<br> 無法變更專用錶面的參數，例如：深色模式、錶面分隔線等。<br><br> **韌體更新極可能會破壞 AAPS 錶面：請停用錶面更新功能**。
```

或者考慮改用 [GlucoDataHandler](https://play.google.com/store/apps/details?id=de.michelinside.glucodatahandler) 搭配錶面小工具。

### 配備 Wear OS 5 的 Pixel 手錶

不相容於 AAPS 錶面。  
建議改用 [GlucoDataHandler](https://play.google.com/store/apps/details?id=de.michelinside.glucodatahandler) 搭配錶面小工具。

## 如何設置 Samsung Galaxy 4 智慧型手錶與 **AAPS** 搭配使用

本節假設你對智慧型手錶完全陌生，將向你介紹一款流行手錶（**Galaxy Watch 4**）的基本操作，隨後是逐步設置 **AAPS** 在手錶上運作的指南。

_本指南假設你正在設置運作 Wear OS 3 或更低版本的 Samsung Galaxy 手錶。_ 如果你正在設置運作 Wear OS 4/OneUI 5 或更高版本的手錶，你將需要使用新的 ADB 配對過程，這在 Samsung 手機軟體中有解釋，並將在適當時更新到這裡。

這裡有關於 [Galaxy Watch 5](https://www.youtube.com/watch?v=Y5upzOIxwTU) 和 [Galaxy Watch 6](https://www.youtube.com/watch?v=D6bq20KzPW0) 的基本設置指南

## 智慧型手錶的基本熟悉指南

根據上方影片進行手錶的基本設置後，前往手機上的 Play 商店並下載以下應用程式：“Galaxy Wearable”、“Samsung”和“Easy Fire tools”或“Wear Installer 2”。

有許多第三方 YouTube 影片可幫助你熟悉新手錶，例如：

[https://www.youtube.com/watch?v=tSVkqWNmO2c](https://www.youtube.com/watch?v=tSVkqWNmO2c)

“Galaxy Wearable”應用程式內也有一個使用手冊部分。 在手機上打開 Galaxy Wearable，搜尋手錶，嘗試將手錶與手機配對。 根據你的版本，這可能會提示你從 Play 商店安裝第三個應用程式“Galaxy Watch 4 外掛”（下載需要一些時間）。 在手機上安裝此應用程式，然後再次在 Galaxy Wearable 應用程式中嘗試將手錶與手機配對。 透過一系列選單並勾選各種偏好設定。

## 設置 Samsung 帳號

你需要確保用來設置 Samsung 帳號的電子郵件帳戶的出生日期顯示用戶年齡 13 歲以上，否則 Samsung 的許可權批准將非常困難。 如果你已為 13 歲以下的孩子建立了 Gmail 帳號並使用該電子郵件地址，你無法簡單地將其更改為成人帳戶。 解決此問題的一種方法是將目前的出生日期修改為使目前年齡為 12 歲零 363 天。 第二天，該帳戶將被轉換為成人帳戶，然後你可以繼續設置 Samsung 帳戶。

(remote-control-transferring-the-aaps-wear-app-onto-your-aaps-phone)=

## 將**AAPS** Wear應用傳輸到你的**AAPS**手機

從 Android Studio 將 Wear.apk 載入到你的手機，可以透過以下方式進行：

a) 使用 USB 傳輸線將 **AAPS** wear apk 檔案放入手機，然後將其“側載”到手錶上。 透過 USB 將 Wear.apk 傳輸到手機的下載資料夾；或

b) 從 Android Studio 將 Wear.apk 剪切並粘貼到你的 Gdrive 中。


你可以使用 Wear Installer 2 或 Easy Fire tools 將 AAPS 側載到手錶上。 這裡我們推薦使用 Wear Installer 2，因為影片中的說明和過程非常清晰且解釋得很好。

## 使用 Wear Installer 2 將 **AAPS** Wear 從手機側載到手錶上

 ![圖像](../images/43577a66-f762-4c11-a3b3-4d6d704d26c7.png)

Wear Installer 2 由 [Malcolm Bryant](https://www.youtube.com/@Freepoc) 開發，你可以從 Google Play 將其下載到手機上，並用來將 AAPS wear 應用程式側載到手錶上。 該應用程式包含一個便捷的“如何側載”[影片](https://youtu.be/abgN4jQqHb0?si=5L7WUeYMSd_8IdPV)。

```{tip}
對於 Wear OS 5 智慧型手錶，請參閱[此影片](https://www.youtube.com/watch?v=yef_qGvcCnk)。
參見故障排除提示[如下](#BuildingAapsWearOs-WearOS5-TShoot)。
```

該視頻提供了所有必要的細節（最好在單獨的設備上打開影片，以便在設置手機時觀看）。

如影片中所述，完成後，請關閉手錶上的 ADB 調試，以避免消耗智慧型手錶的電池。

或者，但不適用於 Wear OS 5，你可以：

```{admonition} Use Easy Fire tools to side-load the **AAPS** wear on the watch
:class: dropdown

1)   從 Play 商店下載 _Easy Fire Tools_ 到你的手機 

![image](../images/81ceb8f3-dfa6-468b-b9d0-c31b885bc104.png)

2)  在手錶上成為開發者 (設置好並連接到手機後)： 

前往設定>關於手錶 (底部選項)>- 軟體資訊> 軟體版本。 

快速點擊“軟體版本”，直到出現通知，告知手錶現在處於“開發者模式”。 返回設置選單頂部，向下滾動，並在“關於手錶”下方看到“開發者選項”。 

在“開發者選項”中，打開“ADB 調試”和“無線調試”。 後者將顯示手錶的 IP 地址，其最後兩位數字每次與新手機配對時都會改變。 他會像是：**167.177.0.20.** 5555（忽略最後4位數）。 請注意，每次將 AAPS 切換到新手機時，這個地址的最後兩位數字（這裡為“20”）將發生變化。  

![24-10-23, watch ADB debug pic](../images/643f4e8b-09f3-4a8d-8277-76b1839a5c3a.png)

步驟 3)     在手機上的 Easy Fire Tools 中輸入 IP 位址，例如： **167.177.0.20** (進入左側選單，設定並輸入 IP 位址)。 然後點擊右上角的插頭圖示。  

![image](../images/b927041f-cc53-4cde-9f77-11cd517c9be0.png)


![image](../images/00b2fb8b-5996-4b71-894e-516d63469e1b.png)


步驟 4) 請按照[這裡](https://wearablestouse.com/blog/2022/01/04/install-apps-apk-samsung-galaxy-watch-4/?utm_content=cmp-true)的指示，使用 Easy Fire 工具將 Wear.apk 透過側載（即傳輸）到手錶上

點擊應用中的側 "外掛" 插孔，以將 Wear OS.apk 上傳到手錶: 

![image](../images/d1bc4c9d-d5ef-4402-a9a2-a51ed242eff3.png)


 下一步 > 在手錶上接受授權請求


![image](../images/2c398a34-b865-4aa1-9c53-d83dfef052a7.png)

```

(BuildingAapsWearOs-WearOS5-TShoot)=

### Wear OS 5的一般故障排除建議

- 請勿使用 Wi-Fi 分享。 這樣做是行不通的。
- 不需要在手機上啟用 ADB 調試（僅在手錶上）。 在手機上停用 ADB 調試。
- 確保你連接到手機和手錶可以彼此看到的本地網路（不要使用 Wi-Fi 客用網路連接）。
- 對於 GW7，需使用 Wear Installer安裝，因為它在安裝時提供選擇**AAPS（自訂）**錶面的選項。
- 確保手錶和手機在同一網路和 Wi-Fi 設備上。 特別是 Wi-Fi 重複器或接取點可能會產生問題。
- 確保靠近你的主要路由器，然後重啟手機和手錶。

**配對中 :**

- 手錶：無線調試：記下 IP 地址。
- Wear Installer：在 Wear Installer 應用程式中輸入 IP 地址。
- 選擇配對新設備，記下顯示的配對碼和埠號。
- Wear Installer：輸入配對碼 + 空格 + 埠號。
- Wear Installer 應該報告配對成功。 如果沒有，請退出 Wear Installer，然後重試。

一旦配對成功，你應該能安裝 AAPS Wear apk：

- 退出/關閉，然後重啟 Wear Installer。
- 在無線調試中，記下 IP 和埠號，並確保在 Wear Installer 中檢查/輸入 IP 和埠號。
- 注意：埠號與配對時使用的不同！

## 設置 **AAPS** 手機與手錶的連線

最後一步是在手機上設定 **AAPS**，使其能與手錶上的 **Wear.apk** 進行互動。 為此，在 組態建置工具 中啟用 Wear 外掛：

* 前往手機上的 **AAPS** 應用程式

* 在左側漢堡按鈕中選擇 > 組態建置工具

* 在一般設定下勾選手錶選項

![Wear OS](../images/WearOS.png)

要更改 **AAPS** 手錶錶盤，請按下手錶的主畫面，他將進入“自訂”模式。 然後向右滑動，直到看到所有 **AAPS** 錶盤。

如果 **AAPS** Wear.apk 已成功側載到智慧型手錶上，他將顯示如下：


![24-10-23，成功的 Galaxy 手錶照片](../images/628e46d8-c7dc-4741-9eba-ae83f396c04c.png)


對於某些智慧手錶，例如 Samsung Galaxy，若要透過 Wi-Fi 遠端使用 **Wear.apk** 與 **AAPS**，必須在 Samsung Galaxy 的「進階功能」中將 **遠端連線** 設為 <0>開啟</0>。

![MURCIMG-20251007-WA0000](https://github.com/user-attachments/assets/5db08a08-f256-49a0-8843-46bdd01b33d6)

### 排除 **AAPS** 手錶與 **AAPS** 手機通訊的問題

1.  如果 EasyFire tools 無法連線，或者你收到“授權失敗”訊息 > 請檢查 IP 地址是否正確輸入。
2.  檢查智慧型手錶是否已連線到網際網路（而不僅僅是透過藍牙與手機連線）。
3.  檢查 **AAPS** 手機和智慧型手錶是否已在 Samsung 應用程式中配對或連線。
4.  也可能需要對手機和智慧型手錶進行硬重啟（即關閉並重新啟動手機）。
5.  假設你已經成功下載 Wear.apk 到手機，但未收到任何血糖資料，_請檢查_ 你是否已將正確的 **AAPS** apk 版本側載到手錶上。 如果你的 AAPS wear.apk 版本列為以下任一項： a) “wear-AAPSClient-release”； b) ‘wear-full-release.aab’; 或 c) 標題中出現“debug”字樣， 則表明你在建置過程中未選擇正確的 Wear OS apk 版本。
6.  檢查路由器是否未將設備相互隔離。

更多問題排除提示請參閱[這裡](https://freepoc.org/wear-installer-help-page/#:~:text=If%20you%20are%20having%20problems,your%20phone%20and%20your%20watch.)

(WearOS_changing-to-AAPS-watchface)=

## 在 WearOS 手錶上切換到 AAPS 手錶外觀

AAPS Wear OS APK 的標準版本中提供了多種手錶外觀。 當你在手錶上安裝 AAPS Wear APK 後，他們將可供使用。 以下是選擇其中一個手錶外觀的步驟：

1. 在手錶上（假設使用 WearOS），長按目前手錶外觀以打開手錶外觀選擇畫面，然後向右捲動直到看到「新增手錶外觀」按鈕並選擇他

![Screenshot_20231123_124657_sysui](../images/efd4268f-0536-4a31-9ba1-f98108f32483.png)

2. 向下捲動到列表底部，直到看到「已下載」部分，找到「AAPS（自訂）」並點擊圖像中央將其新增至你目前的手錶外觀清單。 不用擔心目前「AAPS（自訂）」手錶外觀的外觀，我們將在下一步選擇你喜歡的外觀。

![Screenshot_20231123_124619_sysui](../images/036dc7c4-6672-46c8-b604-8810a16a2eb3.png)

3. 現在打開你手機上的 AAPS，進入 Wear 外掛（如果你在頂部的外掛列表中未看到他，請在組態建置工具中啟用他（位於同步選項下）。

![Screenshot_20231123_090941_AAPS](../images/5df23fa3-791b-4c9a-999a-251391a82835.png)

4. 點擊「載入手錶外觀」按鈕，並選擇你喜歡的手錶外觀。

![Screenshot_20231123_130410_AAPS](../images/adde2eca-1df7-4382-b9ab-346819c35d9d.png)

5. 查看你的手錶，現在應該顯示你選擇的「AAPS（自訂）」手錶外觀。 等待幾秒鐘讓他重新整理。 你現在可以透過長按錶面，然後在錶面圖像上按“自訂”按鈕來自訂錶面等項目。

## AAPSv2 手錶外觀 - 圖例

![AAPSv2 手錶外觀圖例](../images/Watchface_Legend.png)

A - 從最後一次循環運作以來的時間

B - CGM 資料讀取值

C - 自最後一次 CGM 資料讀取以來的分鐘數

D - 與上次 CGM 讀取值相比的變化（以 mmol 或 mg/dl 為單位）

E - 過去 15 分鐘的 CGM 讀取值平均變化

F - 手機電池

G - 基礎率（標準率顯示為U/h，臨時基礎率（TBR）顯示為百分比）

H - BGI（血糖互動） -> 基於胰島素活動時，血糖“應該”上升或下降的程度。

H - BGI（血糖影響） -> 基於胰島素活性，血糖「應該」上升或下降的程度。

I - 碳水化合物（碳水化合物在體內的數量 | 未來的碳水化合物）
