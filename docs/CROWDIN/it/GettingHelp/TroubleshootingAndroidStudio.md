(troubleshooting_androidstudio-troubleshooting-android-studio)=
# Risoluzione dei Problemi Android Studio

(troubleshooting_androidstudio-lost-keystore)=
## Chiave persa
Se utilizzi la stessa chiave (keystore) durante l'aggiornamento di **AAPS** non è necessario disinstallare la versione precedente sullo smartphone. Ecco perché è consigliato memorizzare la chiave in un luogo sicuro.

Se provi a installare l'apk, firmato con una chiave diversa, avrai un messaggio di errore che spiega che l'installazione è fallita!

Nel caso in cui non sia possibile rintracciare la tua chiave originale o la password, procedi come segue:

1. [Esporta le impostazioni](../Maintenance/ExportImportSettings.md) sul tuo telefono.
2. Copia o carica il file delle impostazioni dal telefono in una postazione esterna (un computer, un servizio di cloud...).
4. Genera una nuova versione dell'apk firmato come descritto nella guida [Aggiornamento ](../Maintenance/UpdateToNewVersion) e trasferiscila sul tuo telefono.
5. Disinstalla la versione **AAPS** precedente sul tuo telefono.
6. Installa la nuova versione **AAPS** sul tuo telefono.
7. [Importa le impostazioni](#ExportImportSettings-restoring-from-your-backups-on-a-new-phone-or-fresh-installation-of-aaps) per ripristinare gli obiettivi e la configurazione.

   Se non riesci a trovarle sul tuo telefono, copiale dalla memoria esterna al tuo telefono.

8. Controlla le opzioni di ottimizzazione della batteria e disabilitale di nuovo.
9. Continua con il tuo circuito chiuso.

## Gradle Sync fallito
Gradle Sync può fallire per vari motivi. Se ricevi un messaggio che dice 'gradle sync failed', apri la scheda "Build" (1) nella parte inferiore di Android Studio e controlla quale messaggio di errore (2) viene visualizzato.

  ![Gradle Failed](../images/studioTroubleshooting/07_GradleSyncFailed2.png)

I motivi più comuni per i fallimenti di sincronizzazione del Gradle sono:
* [Uncommitted changes](#uncommitted-changes)
* [No cached version of ... available](#could-not-resolveno-cached-version)
* [Incompatible Gradle JVM](#incompatible-gradle-jvm)
* [Incompatible version of the Android Gradle plugin](#incompatible-version-of-android-gradle-plugin)

*Importante*: Dopo aver seguito le istruzioni per il tuo problema, devi attivare nuovamente la sincronizzazione del [gradle](#gradle-resync).


### Uncommitted changes

Se ricevi un messaggio di errore come questo:

![Gradle Uncommited Changes](../images/studioTroubleshooting/02_GradleUncommitedChanges.png)

#### Fase 1 - Controlla l'installazione di Git
  * Apri la scheda del terminale (1) nella parte inferiore di Android Studio e copia/incolla (o digita) il testo sotto, nel terminale.
    ```
    git --version
    ```

    ![Gradle Git Version](../images/studioTroubleshooting/03_GitVersion.png)

    Nota: C'è uno spazio e due trattini tra git e version!

  * Devi ricevere un messaggio che dica quale versione di Git è installata, come puoi vedere nella schermata sopra. In questo caso, vai alla [Fase 2](#troubleshooting-android-studio-check-for-uncommitted-changes).

  * Se ottieni un messaggio che dice
    ```
    Git: command not found
    ```
    la tua installazione Git non è corretta.

  * [Controlla l'installazione di Git](#BuildingAaps-steps-for-installing-git)

  * se hai appena installato Git su Windows, devi riavviare il computer per rendere Git disponibile a livello globale

  * Se Git è installato, il computer è stato riavviato (con Windows), e Git non è ancora stato trovato:

  * Cerca nel tuo computer un file "git.exe".

    Nota per te, in quale cartella si trova.

  * Vai alle Variabili di Ambiente in Windows, seleziona la variabile "PATH" e fai clic su modifica. Aggiungi la cartella in cui hai trovato la tua installazione di Git.

  * Save and close.

  * Restart Android Studio.


#### Step 2: Check for uncommitted changes.

  * In Android Studio, open the 'Commit' tab (1) on the left-hand side. ![Commit Tab: Uncommitted changes](../images/studioTroubleshooting/04_CommitTabWithChanges.png)
  * You can see either a "Default changeset" (2) or "Unversioned files" (3):

    * For "Default changeset", you probably updated 'Gradle' or changed some of the file contents by mistake.

    * Right click on "Default Changeset" and select "Rollback"

      ![Commit Tab: Rollback changes](../images/studioTroubleshooting/05_CommitTabRollback.png)

    * The files are fetched again from the Git server. If there are no other changes in the commit tab, go to [Step 3](#gradle-resync).

  * If you can see "Unversioned Files", you might have stored files in your sourecode directory which should be better places somewhere else, e.g. your keystore file.

    * Use your regular file explorer on your computer to move or cut and paste that file to a safe place.

    * Go back to Android Studio and click the Refresh button (4) within the Commit tab to make sure the file is not stored in the **AAPS** directory anymore.

      If there are no other changes in the Commit tab, go to [Step 3](#gradle-resync).




#### Step 3: Resync Gradle (again)

Follow the instructions at [Gradle Resync](#gradle-resync).

(troubleshooting_androidstudio-android-gradle-plugin-requires-java-11-to-run)=

(incompatible-gradle-jvm)=
### Incompatible Gradle JVM

![Incompatible Gradle JVM](../images/studioTroubleshooting/160_InkompatibelAndroidGradleJVM.png) If you experience the above error message, you need to download a correct JVM version before you can try rebuild again:
1.  Check in the [requirement table](#Building-APK-recommended-specification-of-computer-for-building-apk-file) which JVM version you need for the **AAPS** version you are building, and make a note of it.

2. Open the Gradle view by clicking on the elephant (1) on the right side of Android Studio and open the settings (2) and select **Gradle Settings** (3):

![Open Gradle Settings](../images/studioTroubleshooting/161_GradleSettings.png)

3.  Open the **Gradle JDK** options, then select **Download JDK...**

![Select Download JDK](../images/studioTroubleshooting/162_DownloadJDK.png)

4. At tab (1), select the JDK version required for your **AAPS** version (the one you made a note of at the first step). Then select the **JetBrains Runtime** from the **Vendor** at tab (2). Do not change the **Location** at tab (3).

![Select JDK 17](../images/studioTroubleshooting/163_JDKSelection.png)

5.  Close the **Settings** dialog with **OK**.
6. You now need to restart the Gradle Sync. Follow the instructions at [Gradle Resync](#gradle-resync).

(incompatible-version-of-android-gradle-plugin)=
### Incompatible version of Android Gradle plugin

  If you experience the following error message

  ![Incompatible version of Android Gradle plugin](../images/studioTroubleshooting/15_InkompatibelAndroidGradlePlugin.png)

  You are using an outdated version of Android Studio. In the menu, go to Help > Check for updates and install any updates of Android Studio and its plugins that are found.

(troubleshooting_androidstudio-could-not-resolve-no-cached-version)=
### Could not resolve/No cached version

  You might get this error message:

![Could not resolve... No cached version](../images/studioTroubleshooting/08_NoCachedVersion.png)

  * On the right side, open the Gradle tab (1).

    Make sure the button shown at (2) is *NOT* selected.

    ![Gradle Offline Mode](../images/studioTroubleshooting/10_GradleOfflineMode.png)

  * Now you need to trigger a [Gradle Resync](#gradle-resync)

(troubleshooting_androidstudio-unable-to-start-daemon-process)=
### Unable to start daemon process

  If you see an error message like the one below you probably use a Windows 10 32-bit system. This is not supported by Android Studio 3.5.1 and above and unfortunately there is nothing that the **AAPS** developers can do about this!

  There  is information on the internet about how to determine wether you have a 32-bit or 64-bit OS - i.e. [this one](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d).

  ![Screenshot Unable to start daemon process](../images/AndroidStudioWin10_32bitError.png)

(gradle-resync)=
### Gradle Resync

  If you can still see the message that the gradle sync failed, now select the Link "Try again". ![Gradle Sync Failed Mode](../images/studioTroubleshooting/01_GradleSyncFailed.png)


  If you don't see the message anymore, you can still trigger this manually:

  * Open the Gradle tab (1) on the right border of Android Studio.

    ![Gradle Reload](../images/studioTroubleshooting/06_GradleResyncManually.png)

  * Right-click on AAPS (2)

  * Click on "Reload Gradle Project" (3)

## Generate Signed APK generated successfully with 0 build variants

When you generate the signed apk, you might get the notification that generation was successfully but are told that this is with '0 build variants' were generated:

![APK generated with 0 build variants](../images/studioTroubleshooting/14_BuildWith0Variants.png)

This is a false warning. Check the directory for your selected "Destination folder" for generation (step [Generate Signed APK](#Building-APK-generate-signed-apk)) and you will find the generated apk there!


## App was created with compiler/kotlin warnings

If your build completed successfully but you get compiler or kotlin warnings (indicated by a yellow or blue exclamation mark) then you can just ignore these warnings.

 ![Gradle finished with warnings](../images/studioTroubleshooting/13_BuildWithWarnings.png)

Your apk was built successfully and can be transferred to your phone!


## Key was created with errors

When creating a new keystore for building the signed apk, on Windows the following error message might appear

![Key was created with errors](../images/AndroidStudio35SigningKeys.png)

This seems to be a bug with Android Studio 3.5.1 and its shipped Java environment in Windows. The key is created correctly but a recommendation is falsely displayed as an error. This can currently be ignored.


## No CGM data is received by AAPS

* If you are using patched Dexcom G6 app: this app is outdated. Use the [BYODA](#DexcomG6-if-using-g6-with-build-your-own-dexcom-app) app instead.

* If you are using xDrip+: identify receiver as described on [xDrip+ settings page](#xdrip-identify-receiver).


## Apk not installed

![phone app note installed](../images/Update_AppNotInstalled.png)

* Make sure you have transferred the “app-full-release.apk” file to your phone.
* If "App not installed" is displayed on your phone follow these steps:

1. [Export settings](../Maintenance/ExportImportSettings.md) (in AAPS version already installed on your phone)
2. Uninstall **AAPS** on your phone.
3. Enable airplane mode & turn off bluetooth.
4. Install new version (“app-full-release.apk”)
5. [Import settings](../Maintenance/ExportImportSettings.md)
6. Turn bluetooth back on and disable airplane mode

## Apk installed but old version

If you built the app successfully, transferred it to your phone and installed it successfully but the version number stays the same then you might have missed to [update your local copy](#Update-to-new-version-update-your-local-copy)

## None of the above worked

If non of the above tips helped you might consider building the apk from scratch:

1. [Export settings](../Maintenance/ExportImportSettings.md) (in AAPS version already installed on your phone)

2. Have your key password and key store password ready. In case you have forgotten passwords you can try to find them in project files as described [here](https://youtu.be/nS3wxnLgZOo).

    Or you just use a new keystore.

3. Build the apk from scratch as described [here](#Building-APK-download-AAPS-code).

4. When you have built the apk successfully delete the exiting apk on your phone, transfer the new apk to your phone and install.
5. [Import settings](../Maintenance/ExportImportSettings.md) again to restore your objectives and settings.
6. You should check your battery optimization options and disable them again.

## Worst case scenario

If the above does not solve your build issue you may wish to try to uninstall Android Studio completely and rebuild from scractch.  Some users find that this can resolve their build problem.  When deleting Android Studio, do not delete Android user settings and **Make sure to uninstall all files associated with Android Studio.** If you do not completely remove Android Studio with all hidden files, uninstalling may cause new problems instead of solving your existing one(s). Manuals for complete uninstall can be found online i.e.

[https://stackoverflow.com/questions/39953495/how-to-completely-uninstall-android-studio-from-windowsv10](https://stackoverflow.com/questions/39953495/how-to-completely-uninstall-android-studio-from-windowsv10).

Install Android Studio from scratch as described [here](#Building-APK-install-android-studio).
