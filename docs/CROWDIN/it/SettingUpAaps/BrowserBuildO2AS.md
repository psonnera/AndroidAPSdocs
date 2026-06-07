### Copy your Android Studio key in your Google Cloud drive.

Sul tuo computer, cerca il file keystore usato per compilare AAPS. Ha l'estensione `.jks`.

Trascinalo in [Google Drive](https://drive.google.com/drive/my-drive), tramite il browser o il tuo Google Drive mappato.

![](../images/Building-the-App/CI/BrowserBuildStep20.png)

Open File Manager Plus and select Cloud.

![](../images/Building-the-App/CI/BrowserBuildStep21.png)

Add a Cloud location.

![](../images/Building-the-App/CI/BrowserBuildStep24.png)

Choose Google Drive.

![](../images/Building-the-App/CI/BrowserBuildStep22.png)

Select your Google Drive account email. Tap OK.

![](../images/Building-the-App/CI/BrowserBuildStep23.png)

Your Google Cloud drive should display its contents. Ora torna alla home page dell'app.

![](../images/Building-the-App/CI/BrowserBuildStep25.png)

### Open the CI preparation help file

Apri il file `aaps-ci-preparation-html` scaricato in precedenza.

Select Downloads.

![](../images/Building-the-App/CI/BrowserBuildStep07.png)

And search for this file, tap it to open it, open it with Chrome, tap Just once.

![](../images/Building-the-App/CI/BrowserBuildStep08.png)

It will open like this.

![](../images/Building-the-App/CI/BrowserBuildStep09.png)

Scroll down to Option 2: Upload Existing JKS. Espandi l'interfaccia.

![](../images/Building-the-App/CI/BrowserBuildStep26.png)

Select Choose File.

![](../images/Building-the-App/CI/BrowserBuildStep27.png)

Pick your KeyStore file from your Google Drive files.

![](../images/Building-the-App/CI/BrowserBuildStep28.png)

The field below will populate.

![](../images/Building-the-App/CI/BrowserBuildStep29.png)

Keep this tab open.

### Crea un nuovo segreto in GitHub

Torna alla scheda GitHub nel browser: la tua copia personale di AndroidAPS.

1. In alto a destra, tocca il pulsante `...`
2. Seleziona Impostazioni nell'elenco

![](../images/Building-the-App/CI/BrowserBuildStep10.png)

Scroll down to Security and select Secrets and variables.

![](../images/Building-the-App/CI/BrowserBuildStep11.png)

Now select Actions

![](../images/Building-the-App/CI/BrowserBuildStep12.png)

Scroll down to Repository secrets and tap New repository secret

![](../images/Building-the-App/CI/BrowserBuildStep13.png)

You will see this dialog (scroll down if it's not visible).

![](../images/Building-the-App/CI/BrowserBuildStep14.png)

Leave the tab opened like this.

Passa alla scheda File Explorer Plus.

Tocca il pulsante Copia in alto.

![](../images/Building-the-App/CI/BrowserBuildStep30.png)

Switch back to the GitHub tab.

Nel campo Nome, incolla il testo appena copiato. Usa una pressione prolungata sulla casella di testo per visualizzare il menu di incolla.

![](../images/Building-the-App/CI/BrowserBuildStep31.png)

Switch to the File Explorer Plus tab.

Tocca il secondo pulsante Copia.

![](../images/Building-the-App/CI/BrowserBuildStep32.png)

Switch back to the GitHub tab.

1. Nel campo Segreto, incolla il testo appena copiato. Usa una pressione prolungata sulla casella di testo per visualizzare il menu di incolla.

2. Tap Add secret.

![](../images/Building-the-App/CI/BrowserBuildStep33.png)

Check the secret has been added, scroll down to verify.

![](../images/Building-the-App/CI/BrowserBuildStep34.png)

Add a new secret: tap the New repository secret button.

![](../images/Building-the-App/CI/BrowserBuildStep35.png)

![](../images/Building-the-App/CI/BrowserBuildStep14.png)



Switch to the File Explorer Plus tab.

Tocca il pulsante Copia in alto per copiare `KEYSTORE_PASSWORD`.

Nota: se preferisci digitare i nomi delle chiavi direttamente in GitHub, non hai bisogno di copiare/incollare. Se non sei sicuro di digitare esattamente lo stesso nome della chiave, procedi in questo modo. Nota che non dovresti lasciare `:` alla fine del nome della chiave.

![](../images/Building-the-App/CI/BrowserBuildStep36.png)

Switch back to the GitHub tab.

1.  Incolla il nuovo nome della chiave.
2. Nel campo Segreto, inserisci la password del KeyStore (non lasciarla vuota).
3. Tap Add secret.

![](../images/Building-the-App/CI/BrowserBuildStep37.png)

Check the secret has been added, scroll down to verify.

![](../images/Building-the-App/CI/BrowserBuildStep38.png)

Tap the New repository secret button shown above.

![](../images/Building-the-App/CI/BrowserBuildStep14.png)



Switch to the File Explorer Plus tab.

Tocca il pulsante Copia in alto per copiare `KEYSTORE_ALIAS`.

![](../images/Building-the-App/CI/BrowserBuildStep39.png)

Switch back to the GitHub tab.

1.  Incolla il nuovo nome della chiave.
2. Nel campo Segreto, inserisci il tuo KeyStore Alias (di solito è `key0`, minuscolo con il numero zero, non la lettera O). Non lasciare che Android lo autocorrrechi.
3. Tap Add secret.

![](../images/Building-the-App/CI/BrowserBuildStep40.png)

Check the secret has been added, scroll down to verify.

![](../images/Building-the-App/CI/BrowserBuildStep41.png)

Tap the New repository secret button shown above.

![](../images/Building-the-App/CI/BrowserBuildStep14.png)



Switch to the File Explorer Plus tab.

Tocca il pulsante Copia in alto per copiare `KEY_PASSWORD`.

![](../images/Building-the-App/CI/BrowserBuildStep42.png)

Switch back to the GitHub tab.

1.  Incolla il nuovo nome della chiave.
2. Nel campo Segreto, inserisci la password della chiave (non lasciarla vuota). Di solito è la stessa della password del KeyStore.
3. Tap Add secret.

![](../images/Building-the-App/CI/BrowserBuildStep43.png)

Check the secret has been added, scroll down to verify.
