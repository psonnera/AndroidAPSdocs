- - -
orphan: true
- - -

# Come configurare un telefono Huawei

Ci sono diverse opzioni, alcune specifiche a Android, altre specifiche a Huawei:

* Aggiungi AAPS e xdrip+ alla lista delle app che ignorano le ottimizzazioni della batteria:
  * Impostazioni / Apps / Impostazioni / Autorizzazioni speciali / Ignora ottimizzazione della batteria / Seleziona "Tutte le app" / Autorizza l'app AAPS

    ![Huawei - ignora l'ottimizzazione della batteria](../images/Huawei_BatteryOptimization.png)


* Imposta le opzioni della batteria:
  * Impostazioni / Apps / Seleziona AndroidAPS/xDrip+ / Batteria / Avvio app
   * Assicurati di rimuovere "gestione automatica"
    * Consenti:
     * Avvio automatico
     * Avvio secondario (può essere avviato da altre applicazioni)
     * Esecuzione in background

       ![Huawei - opzioni batteria](../images/Huawei_BatteryOptions.png)

* Blocca l'app
  * Vai nella lista delle app recente e seleziona l'icona del lucchetto

    ![Huawei - blocco app](../images/Huawei_LockApp.png)



Per xDrip+, è necessario abilitare le notifiche persistenti (all'interno dell'app xDrip+):
* Impostazioni / Impostazioni meno usate / Altre opzioni / Esegui Collettore in primo piano

   ![impostazioni xdrip+ - collettore in primo piano](../images/xdrip_collector_foreground.png)


A seconda della versione di Android, queste impostazioni sono altrove. Queste spiegazioni erano per Android 8.1.
