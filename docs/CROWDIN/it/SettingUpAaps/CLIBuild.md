# Istruzioni di compilazione da riga di comando

```{admonition} For users familiar with the command-line and git
:class: information

L'opzione più semplice per compilare AAPS è il metodo [Browser build](./BrowserBuild.md).
```

Testato su Fedora e Debian Linux; altri sistemi dovrebbero funzionare con adattamenti minimi.

## Requisiti

Consultare la versione minima di Java richiesta in [questa tabella](#Building-APK-recommended-specification-of-computer-for-building-apk-file). Installare il pacchetto OpenJDK appropriato tramite il gestore di pacchetti di sistema. Ad esempio, su Debian i pacchetti si chiamano come `openjdk-21-jdk`. Deve includere i binari `javac` e `keytool`.

Scaricare il pacchetto *Android Command line tools* dalla [pagina di Android Studio](https://developer.android.com/studio#command-line-tools-only). Android Studio non è necessario. Ulteriori informazioni sull'installazione di questo pacchetto sono disponibili nella [documentazione di sdkmanager](https://developer.android.com/tools/sdkmanager). Dopo aver installato il pacchetto, è necessario impostare manualmente due [variabili d'ambiente](https://developer.android.com/tools/variables): `ANDROID_HOME` e `PATH`. Infine, eseguire `sdkmanager --licenses` per completare l'installazione.

## Compilare AAPS con il wrapper Gradle

### 1. Generare un file Java keystore per la firma di AAPS

Se hai già un file keystore per la firma di AAPS, riutilizzalo.

```sh
keytool -genkeypair -v \
  -keystore aaps-keystore.jks \
  -alias aaps-key \
  -keyalg RSA \
  -keysize 4096 \
  -validity 20000
```

Il file keystore e la passphrase saranno necessari ogni volta che si aggiorna AAPS.

### 2. Compilare il file APK di AAPS

Clonare il [repository git](https://github.com/nightscout/AndroidAPS) se non lo si è già fatto. AAPS utilizza il branch master per l'ultima versione stabile; assicurarsi di essere sul branch/tag che si vuole compilare.

Eseguire `./gradlew :app:assembleFullRelease` nel repository. Verrà scaricato automaticamente Gradle, le dipendenze, e poi verrà compilato il codice. Al termine della compilazione, dovresti avere un APK non firmato in `app/build/outputs/apk/full/release/app-full-release-unsigned.apk`. Verrà inoltre installato un binario `apksigner` in `$ANDROID_HOME`. Aggiornare di nuovo `PATH`.

### 3. Creare un file APK firmato a partire da quello non firmato

<!-- Suggest building outside the git repo, to minimize risk of accidental APK commits -->

Spostarsi nella propria directory home e creare un file APK firmato:

```sh
apksigner sign \
  --ks path/to/aaps-keystore.jks \
  --ks-key-alias aaps-key \
  --out app-full-release-signed.apk \
  ./AndroidAPS/app/build/outputs/apk/full/release/app-full-release-unsigned.apk
```

Ora hai `app-full-release-signed.apk` pronto per l'installazione o l'aggiornamento.
