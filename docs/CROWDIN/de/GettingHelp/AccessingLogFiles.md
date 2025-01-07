(Accessing-logfiles-accessing-logfiles)=

# Logdateien erhalten

* Verbinde das Smartphone mit dem Computer im Dateiübertragungsmodus
* Locate the log files in the AAPS data directory, in `Android\data\info.nightscout.androidaps\files`.  
    The naming of the root storage folder may vary a little depending on the phone.
* The location is `Android\data\info.nightscout.aapsclient\files` for [AAPSClient](#RemoteControl_aapsclient).
* Note : log location has changed in **AAPS 3.3**. See the previous versions' documentation if needed.

![Logdateien](../images/aapslog.png)

* Die aktuelle Logdatei ist eine Datei mit der Erweiterung .log, die auf verschiedene Arten angezeigt werden kann wie [LogCat](https://developer.android.com/studio/debug/am-logcat.html) in AndroidStudio, der Android App Log Viewer oder einfach als normaler Text. 
* Ältere Logdateien werden als Zipdatei komprimiert und in Verzeichnissen gespeichert, die nach Datum/Uhrzeit sortiert sind. 
* Wenn du deine Logdatei in [discord](https://discord.gg/4fQUWHZ4Mw) teilen willst, um über ein mögliches Problem zu berichten, dann entpacke sie und lade das Verzeichnis hoch, dessen Datum dem Auftreten des Fehlers entspricht.