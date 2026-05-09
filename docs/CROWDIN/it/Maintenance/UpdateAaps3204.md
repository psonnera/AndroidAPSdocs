# Updating to AAPS 3.2.0.4

<a id="update-aaps-3204"></a>

## Costruisci te stesso invece di scaricare

**L'app AAPS (un file apk) non è disponibile per il download, a causa delle normative sui dispositivi medici. È legale costruire l'app per il proprio uso, ma non devi darne una copia ad altri!**

Vedi la pagina [Domande frequenti](../UsefulLinks/FAQ.md) per i dettagli.

## Computer and software specifications for building AAPS 3.2.0.4

* Una versione specifica di **[Android Studio](https://developer.android.com/studio/)** potrebbe essere necessaria per costruire l'apk.

| Versione AAPS           | Versione<br/>Android Studio<br/>preferita | Versione Alternative<br/>Android Studio<br/> | Gradle | JVM |
| ----------------------- | ----------------------------------------------------- | -------------------------------------------------------- | ------ |:--- |
| [3.2.0.4](#version3200) | Hedgehog (2023.1.1)                                   | up to Meerkat                                            | 8.2    | 17  |

La "versione preferita" contiene già la versione JVM appropriata. La versione preferita è anche la versione minima che puoi usare per costruire **AAPS**. **NON PUOI** costruire su una versione più vecchia di quella "preferita". Se usi una versione diversa, potresti incontrare dei problemi con la versione JVM. Guarda la pagina [Risoluzione dei problemi Android Studio](#troubleshooting_androidstudio-uncommitted-changes) per aiutarti a risolverli. Se la tua versione attuale di Android Studio non è elencata nella tabella, è necessario aggiornarla prima.

La versione Gradle è legata al codice sorgente, otterrai sempre la versione corretta Gradle quando scarichi / aggiorni il codice sorgente. E menzionata qui solo per riferimento, non è necessario intervenire su di esso.

* I sistemi [Windows 32 bit](#troubleshooting_androidstudio-unable-to-start-daemon-process) non sono supportati da Android Studio. Tieni presente che sia **la CPU 64 bit che il sistema operativo a 64 bit sono condizioni obbligatorie.** Se il sistema NON soddisfa queste condizioni, è necessario cambiare il computer, il software, o l'intero sistema.

<table class="tg">
<tbody>
  <tr>
    <th class="tg-baqh">OS (solo 64 bit)</th>
    <td class="tg-baqh">Windows 8 o superiore</td>
    <td class="tg-baqh">Mac OS 10.14 o superiore</td>
    <td class="tg-baqh">Qualsiasi Linux che supporta Gnome, KDE o Unity DE;&nbsp;&nbsp;librerie GNU C 2.31 o versioni successive</td>
  </tr>
  <tr>
    <th class="tg-baqh">CPU (solo 64 bit)</th>
    <td class="tg-baqh">CPU di architettura x86_64; Intel Core di seconda generazione o più recente, o CPU AMD con supporto per <br/><a href="https://developer.android.com/studio/run/emulator-acceleration#vm-windows" target="_blank" rel="noopener noreferrer"><span style="text-decoration:var(--devsite-link-text-decoration,none)">Windows Hypervisor</span></a></td>
    <td class="tg-baqh">Chip basati su ARM, o Intel Core di seconda generazione o più recenti con supporto per <br/><a href="https://developer.android.com/studio/run/emulator-acceleration#vm-mac" target="_blank" rel="noopener noreferrer"><span style="text-decoration:var(--devsite-link-text-decoration,none)">Hypervisor.Framework</span></a></td>
    <td class="tg-baqh">CPU di architettura x86_64; Intel Core di seconda generazione o più recente, o processore AMD con supporto per la virtualizzazione AMD (AMD-V) e SSSE3</td>
  </tr>
  <tr>
    <th class="tg-baqh">Memoria</th>
    <td class="tg-baqh" colspan="3">Uguale o superiore a 8GB</td>
  </tr>
  <tr>
    <th class="tg-baqh">Disco fisso</th>
    <td class="tg-baqh" colspan="3">Almeno 30GB di spazio libero. SSD consigliato.</td>
  </tr>
  <tr>
    <th class="tg-baqh">Risoluzione</th>
    <td class="tg-baqh" colspan="3">1280 x 800 Minimo <br/></td>
  </tr>
  <tr>
    <th class="tg-baqh">Internet</th>
    <td class="tg-baqh" colspan="3">Banda larga</td>
  </tr>
</tbody>
</table>

**E' fortemente consigliato (non obbligatorio) utilizzare un disco SSD (stato solido) invece di un HDD (meccanico) perché ci vorrà meno tempo per costruire il file apk di AAPS.**  Puoi comunque usare un disco fisso meccanico per costruire il file apk di **AAPS**. Se ne usi uno, il processo di costruzione può richiedere molto tempo, ma una volta che è iniziato, puoi lasciarlo in esecuzione incustodito.

## Help and support during 3.2.0.4 building process

Se incontri difficoltà nel processo di costruzione dell'app **AAPS**, consulta la sezione [**dedicata alla risoluzione dei problemi Android Studio**](https://androidaps.readthedocs.io/en/3.2/GettingHelp/TroubleshootingAndroidStudio.html).

Se pensi che qualcosa nelle istruzioni di costruzione sia sbagliato, mancante o confusionale, o ancora stai lottando, contatta il gruppo di utenti **AAPS** su [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) o [Discord](https://discord.gg/4fQUWHZ4Mw). Se vuoi cambiare qualcosa te stesso (aggiornamento screenshot _etc_), ti preghiamo di inviare una [pull request (PR)](../SupportingAaps/HowToEditTheDocs.md).

::: info
This page provides both example pictures for the **New** and old (**Classic**) Android Studio user interfaces.
:::


## Overview for updating 3.2.0.x to 3.2.0.4


### Export your current settings

Esporta le tue impostazioni dalla versione **AAPS** installata sul tuo telefono. Potresti non averne bisogno, ma prevenire è meglio che curare.

Vedi la pagina [Esporta & importa le impostazioni](ExportImportSettings.md) se non ti ricordi come farlo.

### Update your local AAPS copy

* Apri il tuo progetto AAPS esistente con Android Studio. Potrebbe essere necessario selezionare il tuo progetto. (Doppio) clicca sul progetto AAPS.

![Studio Android - Seleziona Progetto](../images/update/01_ProjectSelection.png)

<br/>

![Studio Android - Seleziona Progetto](https://androidaps.readthedocs.io/en/3.1/_images/01_ProjectSelection.png)

* Nella barra di menu di Android Studio, seleziona Git -> Fetch

![Menu Android Studio - Git - Fetch](../images/update/02_GitFetch.png)

<br/>

![Menu Android Studio - Git - Fetch](https://androidaps.readthedocs.io/en/3.1/_images/02_GitFetch.png)

* Vedrai un messaggio nell'angolo in basso a destra che Fetch ha avuto successo.

![Menu Android Studio - Git - Fetch riuscito](../images/update/03_GitFetchSuccessful.png)

<br/>

![Menu Android Studio - Git - Fetch riuscito](https://androidaps.readthedocs.io/en/3.1/_images/03_GitFetchSuccessful.png)

* Nella barra di menu, ora seleziona Git -> Pull

![Menu Android Studio - Git - Pull](../images/update/04_GitPull.png)

<br/>

![Menu Android Studio - Git - Pull](https://androidaps.readthedocs.io/en/3.1/_images/04_GitPull.png)

* Lascia tutte le opzioni come sono (origin/master) e seleziona Pull

![Android Studio - Git - finestra di dialogo Pull](../images/update/05_GitPullOptions.png)

<br/>

![Android Studio - Git - finestra di dialogo Pull](https://androidaps.readthedocs.io/en/3.1/_images/05_GitPullOptions.png)

* Attendi mentre il download è in corso, vedrai questo come informazione nella barra in basso. Quando sarà fatto, vedrai un messaggio di successo.

::: info
The files that were updated may vary! This is not an indication
:::



![Android Studio - Pull riuscito](../images/update/06_GitPullSuccess.png)

<br/>

![Android Studio - Pull riuscito](https://androidaps.readthedocs.io/en/3.1/_images/06_GitPullSuccess.png)

* Gradle Sync verrà eseguito per scaricare alcune dipendenze. Attendi finché non sarà finito.

![Android Studio - Gradle Sync](../images/studioSetup/40_BackgroundTasks.png)

<br/>

![Android Studio - Gradle Sync](https://androidaps.readthedocs.io/en/3.1/_images/40_BackgroundTasks.png)

### Select JVM version 17

- Apri la scheda Gradle cliccando sull'elefante (1) sul lato destro di Android Studio, apri le impostazioni (2) e seleziona **Gradle Settings** (3):

![Apri Le Impostazioni Gradle](../images/studioTroubleshooting/161_GradleSettings.png)

<br/>

![Apri Le Impostazioni Gradle](../images/studioTroubleshooting/09_GradleSettings.png)

- In **Gradle JDK** field, check if the appropriate version: **jbr-17** is selected (1) If not, click on the field, and see if it is already available in the list.

![Seleziona Download JDK](../images/studioTroubleshooting/162_DownloadJDK.png)



- In Version (1), select **17**. In Vendor (2) select JetBrains Runtime or any Vendor. Location (3): non modificare.

![Seleziona JDK 17](https://androidaps.readthedocs.io/en/3.2/_images/163_JDKSelection.png)

- Chiudi la finestra di dialogo **Settings** con **OK**.

### Select the AAPS 3.2.0.4 branch

- At the bottom left, select the Git symbol, right-click on 3.2.0.4 and Checkout.

![Seleziona Download JDK](../images/studioTroubleshooting/17_Checkout.png)

<br/>

![Seleziona Download JDK](../images/studioTroubleshooting/17_CheckoutOld.png)

### Sync project with Gradle

::: warning WARNING!
**Never update Gradle.** Always sync it with the project.
:::


Use the elephant icon and Sync Project with Gradle Files (or follow [this](#gradle-resync)) for the new UI.

![Sync Project with Gradle Files](../images/studioTroubleshooting/06_GradleResyncElephant.png)

Or ([this](https://androidaps.readthedocs.io/en/3.2/GettingHelp/TroubleshootingAndroidStudio.html#gradle-resync)) for the classic UI.

![Sync Project with Gradle Files](../images/studioTroubleshooting/06_GradleResyncElephantOld.png)

### Build the Signed 3.2.0.4 APK

Il tuo codice sorgente è ora la versione corrente rilasciata, e tutti i prerequisiti sono stati verificati. È tempo di costruire l'apk firmato come descritto nella sezione [costruisci l'apk firmato](#Building-APK-generate-signed-apk).

### Transfer and install the 3.2.0.4 APK

Devi trasferire l'apk al telefono in modo da poterla installare.

::: info
If you completed the build with the same existing key store in Android Studio, then you do not need to remove the existing app on your phone. Quando installi l'apk, segui le istruzioni per installare gli aggiornamenti. Per altri scenari come la creazione di un nuovo set di chiavi in Android Studio per il tuo apk firmato, è necessario disinstallare la vecchia app prima di installare l'apk. **Make sure to export your settings!**
:::


Vedi le istruzioni per [trasferire e installare AAPS](../SettingUpAaps/TransferringAndInstallingAaps.md)

### Check AAPS version 3.2.0.4 on phone

Dopo aver installato il nuovo apk, è possibile controllare la versione AAPS sul telefono facendo clic sul menu a tre punti in alto a destra e poi su Informazioni su. Dovresti vedere la versione attuale.

