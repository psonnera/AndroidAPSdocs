(Accessing-logfiles-accessing-logfiles)=
# Accesso ai file di log

* Collega il telefono al computer in modalità trasferimento file
* Individua i file di log nella directory dei dati di AAPS, in `Android\data\info.nightscout.androidaps\files`.<br/> Il nome della cartella radice può variare leggermente a seconda del telefono.
* Per [AAPSClient](#RemoteControl_aapsclient), il percorso è `Android\data\info.nightscout.aapsclient\files`.
* Nota: il percorso dei log è cambiato in **AAPS 3.3**. Consulta la documentazione delle versioni precedenti se necessario.

![logs](../images/aapslog.png)

* Il log corrente è un file .log che può essere visualizzato in diversi modi, ad esempio con [LogCat](https://developer.android.com/studio/debug/am-logcat.html) in Android Studio, con qualsiasi app Log Viewer per Android, o semplicemente come testo normale.
* I file di log precedenti sono compressi e archiviati in cartelle ordinate per data/ora.
* Se stai condividendo il tuo file di log su [Discord](https://discord.gg/4fQUWHZ4Mw) per segnalare un potenziale bug, decomprimi e carica il file datato prima che si verificasse l'errore.
