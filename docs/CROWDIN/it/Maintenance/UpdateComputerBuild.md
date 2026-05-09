# Update with Android Studio

## Costruisci te stesso invece di scaricare

**AAPS** non è disponibile per il download, a causa delle norme relative ai dispositivi medici. È legale costruire l'app per il proprio uso, ma non devi darne una copia ad altri! Vedi la pagina [FAQ](../UsefulLinks/FAQ.md) per i dettagli.

::: info
In case you want to build **AAPS** on a new computer : copy your back-up keystore file to the new computer. Then follow the [Initial build **AAPS** procedure](../SettingUpAaps/BuildingAaps.md) instead of this guide. Con l'unica differenza che: invece di creare un nuovo keystore, puoi selezionare quello che hai copiato sul nuovo computer.
:::


## Overview for updating to a new version of AAPS with Android Studio


In caso di problemi, vedi la pagina separata per la [risoluzione dei problemi Android Studio](../GettingHelp/TroubleshootingAndroidStudio).

### Esporta le tue impostazioni

Esporta le tue impostazioni dalla versione **AAPS** installata sul tuo telefono. Potresti non averne bisogno, ma prevenire è meglio che curare.

Vedi la pagina [Esporta & importa le impostazioni](ExportImportSettings.md) se non ti ricordi come farlo.

### Controlla la tua versione di Android Studio

La versione minima richiesta è specificata nelle [Istruzioni per la Costruzione](#Building-APK-recommended-specification-of-computer-for-building-apk-file). Se la tua versione è più vecchia, [aggiorna Android Studio](#Building-APK-install-android-studio) prima!

<a id="Update-to-new-version-update-your-local-copy"></a>

### Aggiorna la tua copia locale

::: warning WARNING
If you update from versions prior to 2.8.x, please follow the instructions to do a [New clone](../SettingUpAaps/BuildingAaps.md), as this guide will not work for you!
:::


* Apri il tuo progetto AAPS esistente con Android Studio. Potrebbe essere necessario selezionare il tuo progetto. (Doppio) clicca sul progetto AAPS.

  ![Studio Android - Seleziona Progetto](../images/update/01_ProjectSelection.png)

* Nella barra di menu di Android Studio, seleziona Git -> Fetch

   ![Menu Android Studio - Git - Fetch](../images/update/02_GitFetch.png)

* Vedrai un messaggio nell'angolo in basso a destra che Fetch ha avuto successo.

   ![Menu Android Studio - Git - Fetch riuscito](../images/update/03_GitFetchSuccessful.png)

* Nella barra di menu, ora seleziona Git -> Pull

   ![Menu Android Studio - Git - Pull](../images/update/04_GitPull.png)

* Lascia tutte le opzioni come sono (origin/master) e seleziona Pull

   ![Android Studio - Git - finestra di dialogo Pull](../images/update/05_GitPullOptions.png)

* Attendi mentre il download è in corso, vedrai questo come informazione nella barra in basso. Quando sarà fatto, vedrai un messaggio di successo.

::: info
The files that were updated may vary! This is not an indication
:::


   ![Android Studio - Pull riuscito](../images/update/06_GitPullSuccess.png)

* Gradle Sync verrà eseguito per scaricare alcune dipendenze. Attendi finché non sarà finito.

  ![Android Studio - Gradle Sync](../images/studioSetup/40_BackgroundTasks.png)

### Controlla la versione JVM

Questo controllo è particolarmente racommandato se hai già costruito una versione precedente di **AAPS** sullo stesso computer.

Controlla nelle [Istruzioni di Costruzione](#Building-APK-recommended-specification-of-computer-for-building-apk-file) le versioni necessarie per JVM e Gradle, corrispondenti alla versione **AAPS** che stai costruendo. Quindi segui i passaggi descritti in [Gradle JVM incompatibile](#incompatible-gradle-jvm) per assicurarti di utilizzare la versione corretta.

<a id="Update-to-new-version-build-the-signed-apk"></a>

### Costruisci l'APK Firmato

Il tuo codice sorgente è ora la versione corrente rilasciata, e tutti i prerequisiti sono stati verificati. È tempo di costruire l'apk firmato come descritto nella sezione [costruisci l'apk firmato](#Building-APK-generate-signed-apk).

<a id="Update-to-new-version-transfer-and-install"></a>

### Trasferisci e installa l'apk
Devi trasferire l'apk al telefono in modo da poterla installare.

::: info
If you completed the build with the same existing key store in Android Studio, then you do not need to remove the existing app on your phone. Quando installi l'apk, segui le istruzioni per installare gli aggiornamenti. Per altri scenari come la creazione di un nuovo set di chiavi in Android Studio per il tuo apk firmato, è necessario disinstallare la vecchia app prima di installare l'apk. **Make sure to export your settings!**
:::


Vedi le istruzioni per [trasferire e installare AAPS](../SettingUpAaps/TransferringAndInstallingAaps.md)

Continue [here](#Update-to-new-version-check-aaps-version-on-phone).

## Risoluzione dei problemi

Se qualcosa va storto, non farti prendere dal panico.

Fai un respiro!

Quindi vedi nella pagina separata [risoluzione dei problemi Android Studio](../GettingHelp/TroubleshootingAndroidStudio) se il problema è già documentato!

Se hai bisogno di ulteriore aiuto, contatta gli altri utenti **AAPS** su [Facebook](https://www.facebook.com/groups/AndroidAPSUsers) o [Discord](https://discord.gg/4fQUWHZ4Mw).