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

## Gradle Sync failed
Gradle Sync può fallire per vari motivi. Se ricevi un messaggio che dice 'gradle sync failed', apri la scheda "Build" (1) nella parte inferiore di Android Studio e controlla quale messaggio di errore (2) viene visualizzato.

  ![Gradle Failed](../images/studioTroubleshooting/07_GradleSyncFailed2.png)

I motivi più comuni per i fallimenti di sincronizzazione del Gradle sono:
* [Uncommitted changes](#uncommitted-changes)
* [No cached version of ... available](#could-not-resolveno-cached-version)
* [Incompatible Gradle JVM](#incompatible-gradle-jvm)
* [Incompatible version of the Android Gradle plugin](#incompatible-version-of-android-gradle-plugin)

*Importante*: Dopo aver seguito le istruzioni per il tuo problema, devi attivare nuovamente la sincronizzazione del [gradle](#gradle-resync).


### Modifiche senza commit

Se ricevi un messaggio di errore come questo:

![Gradle Uncommited Changes](../images/studioTroubleshooting/02_GradleUncommitedChanges.png)

#### Passo 1 - Controlla l'installazione di Git
  * Apri la scheda del terminale (1) nella parte inferiore di Android Studio e copia/incolla (o digita) il testo sotto, nel terminale.
    ```
    git --version
    ```

    ![Gradle Git Version](../images/studioTroubleshooting/03_GitVersion.png)

    Nota: C'è uno spazio e due trattini tra git e version!

  * Devi ricevere un messaggio che dica quale versione di Git è installata, come puoi vedere nella schermata sopra. In questo caso, vai al [Passo 2](#troubleshooting-android-studio-check-for-uncommitted-changes).

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

  * Salva e chiudi.

  * Riavvia Android Studio.


#### Passo 2: Controlla le modifiche senza commit

  * In Android Studio, apri la scheda 'Commit' (1) sul lato sinistro. ![Commit Tab: Uncommitted changes](../images/studioTroubleshooting/04_CommitTabWithChanges.png)
  * Puoi vedere "Default changeset" (2) oppure "Unversioned files" (3):

    * Per "Default changeset", probabilmente hai aggiornato 'Gradle' o cambiato alcuni contenuti del file per errore.

    * Fai clic con il tasto destro su "Default Changeset" e seleziona "Rollback"

      ![Commit Tab: Rollback changes](../images/studioTroubleshooting/05_CommitTabRollback.png)

    * I file vengono recuperati nuovamente dal server Git. Se nella scheda commit non ci sono altre modifiche, vai al [Passo 3](#gradle-resync).

  * Se vedi "Unversioned Files", potresti aver memorizzato dei file nella tua cartella di codice sorgente, file che dovrebbero essere salvati da qualche altra parte, es. il tuo file di chiavi (keystore).

    * Usa il gestionario di file (explorer) sul tuo computer per spostare o tagliare e incollare quei file in un luogo sicuro.

    * Torna a Android Studio e fai clic sul pulsante Aggiorna (4) all'interno della scheda Commit per assicurarti che il file non sia più memorizzato nella cartella **AAPS**.

      Se non ci sono altre modifiche nella scheda Commit, vai al [Passo 3](#gradle-resync).




#### Passo 3: Risincronizza Gradle (ancora)

Segui le istruzioni di [Risincronizza Gradle](#gradle-resync).

(troubleshooting_androidstudio-android-gradle-plugin-requires-java-11-to-run)=

(incompatible-gradle-jvm)=
### Incompatible Gradle JVM

![Incompatible Gradle JVM](../images/studioTroubleshooting/160_InkompatibelAndroidGradleJVM.png) Se vedi il messaggio di errore sopra, devi scaricare la versione corretta di JVM prima di riprovare a ricostruire:
1.  Controlla nella [tabella dei prerequisiti](#Building-APK-recommended-specification-of-computer-for-building-apk-file) la versione JVM necessaria per la versione **AAPS** che stai costruendo, e prendine nota.

2. Apri la scheda Gradle cliccando sull'elefante (1) sul lato destro di Android Studio, apri le impostazioni (2) e seleziona **Gradle Settings** (3):

![Open Gradle Settings](../images/studioTroubleshooting/161_GradleSettings.png)

3.  Apri le opzioni **Gradle JDK**, quindi seleziona **Download JDK...**

![Select Download JDK](../images/studioTroubleshooting/162_DownloadJDK.png)

4. Nella scheda (1), seleziona la versione JDK richiesta per la tua versione **AAPS** (quella della quale hai preso nota al primo passaggio). Quindi seleziona **JetBrains Runtime** da **Vendor** nella scheda (2). Non modificare **Location** nella scheda (3).

![Select JDK 17](../images/studioTroubleshooting/163_JDKSelection.png)

5.  Chiudi la finestra di dialogo **Settings** con **OK**.
6. Ora è necessario riavviare la sincronizzazione di Gradle. Segui le istruzioni di [Risincronizza Gradle](#gradle-resync).

(incompatible-version-of-android-gradle-plugin)=
### Incompatible version of Android Gradle plugin

  Se vedi questo messaggio di errore

  ![Incompatible version of Android Gradle plugin](../images/studioTroubleshooting/15_InkompatibelAndroidGradlePlugin.png)

  Stai usando una versione obsoleta di Android Studio. Nel menu, vai a Help > Check for updates e installa gli aggiornamenti di Android Studio e di tutti i plugin che vengono trovati.

(troubleshooting_androidstudio-could-not-resolve-no-cached-version)=
### Could not resolve/No cached version

  Potresti ricevere questo messaggio di errore:

![Could not resolve... No cached version](../images/studioTroubleshooting/08_NoCachedVersion.png)

  * Sul lato destro, apri la scheda Gradle (1).

    Assicurati che il pulsante visualizzato su (2) *NON* sia selezionato.

    ![Gradle Offline Mode](../images/studioTroubleshooting/10_GradleOfflineMode.png)

  * Ora devi attivare [Risincronizza Gradle](#gradle-resync)

(troubleshooting_androidstudio-unable-to-start-daemon-process)=
### Unable to start daemon process

  Se vedi un messaggio di errore come quello sotto, probabilmente stai utilizzando un sistema Windows 10 a 32 bit. Non è supportato da Android Studio 3.5.1 e oltre, e purtroppo non c'è nulla che gli sviluppatori **AAPS** possano fare a riguardo!

  Ci sono informazioni su internet su come determinare se hai un sistema operativo a 32 bit o 64 bit - [questo](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d).

  ![Screenshot Unable to start daemon process](../images/AndroidStudioWin10_32bitError.png)

(gradle-resync)=
### Gradle Resync

  Se vedi ancora il messaggio che la sincronizzazione del Gradle non è riuscita, seleziona il link "Try again". ![Gradle Sync Failed Mode](../images/studioTroubleshooting/01_GradleSyncFailed.png)


  Se non vedi più il messaggio, puoi comunque attivarlo manualmente:

  * Apri la scheda Gradle (1) sul bordo destro di Android Studio.

    ![Gradle Reload](../images/studioTroubleshooting/06_GradleResyncManually.png)

  * Clicca col tasto destro su AAPS (2)

  * Clicca su "Reload Gradle Project" (3)

## Generate Signed APK generated successfully with 0 build variants

Quando generi l'apk firmata, potresti avere la notifica che è stata creata correttamente ma che '0 varianti di generazione' sono stati generati:

![APK generated with 0 build variants](../images/studioTroubleshooting/14_BuildWith0Variants.png)

Questo è un falso allarme. Controlla la cartella selezionata come "Destination folder" (passo [Genera APK Firmato](#Building-APK-generate-signed-apk)) e troverai l'apk generato lì!


## L'app è stata creata con dei warning compilatore/kotlin

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
