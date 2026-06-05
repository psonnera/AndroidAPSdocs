# Ramo sviluppatori (Dev)

```{warning}
Il ramo Dev è solo usato per ulteriori sviluppi di AAPS. Deve essere usato su un telefono separato per testare <font color="#FF0000">**non per un circuito chiuso reale!**</font>
```

La versione la più stabile di AAPS da usare è quella del ramo [Master](https://github.com/nightscout/AndroidAPS/tree/master).  Si consiglia di rimanere sul ramo Master per il circuito chiuso effettivo.

La versione dev di AAPS è solo per sviluppatori e testers che sono al loro agio con le tracce dello stack, guardare nei file di log e attivare il debugger per documentare le segnalazioni di bug che sono utili agli sviluppatori (in breve: persone che sanno cosa stanno facendo senza essere assistite!). Quindi molte funzioni incompiute sono disabilitate. Per abilitare queste funzionalità entra in **Modalità Ingegneria** creando un file chiamato `engineering_mode` nella cartella /AAPS/extra . Abilitare la modalità di ingegneria potrebbe rompere completamente il circuito chiuso.

Tuttavia, il ramo Dev è un buon posto per vedere quali funzionalità vengono testate, per aiutare a risolvere i bug e dare un feedback su come le nuove funzionalità saranno implementate in pratica.  Spesso le persone testanno il ramo Dev su un vecchio telefono e micro fino a quando non sono sicuri che sia stabile - qualsiasi uso di esso è a tuo rischio.  Quando provi nuove funzionalità, ricorda che stai scegliendo di testare una funzionalità ancora in fase di sviluppo. Fai così al tuo proprio rischio & con la necessaria diligenza per tenerti al sicuro.

Se trovi un bug o pensi che sia successo qualcosa di sbagliato quando usi il ramo Dev poi verificare nella scheda [Issues](https://github.com/nightscout/AndroidAPS/issues) di GitHub, per verificare se qualcun altro lo ha trovato, o aggiungerlo se è nuovo.  Più informazioni puoi condividere qui, meglio è (non dimenticare che potrebbe essere necessario condividere i tuoi [file di log](../GettingHelp/AccessingLogFiles.md).  Le nuove funzionalità possono anche essere discusse su [Discord](https://discord.gg/4fQUWHZ4Mw).

Una versione Dev ha una data di scadenza. Questo sembra scomodo quando lo usi in modo soddisfacente, ma serve a uno scopo. Quando una singola versione dev è in giro, è più facile tenere traccia degli errori che le persone segnalano. Gli sviluppatori non vogliono essere in una posizione in cui ci sono tre versioni di dev in giro, dove i bug sono risolti in alcuni e non altri, e la gente continua a segnalare quelli sistemati.

(branch-ci-test)=

## Testare un ramo specifico (branch-ci)

Per compilare un ramo di test, selezionare branch-ci, che consente di scegliere un ramo specifico per la creazione dell'APK. Puoi usare questo metodo quando hai bisogno di testare il ramo dev.

![aaps_ci_branch_ci1](../images/Building-the-App/CI/aaps_ci_branch_ci1.png)

![aaps_ci_branch_ci2](../images/Building-the-App/CI/aaps_ci_branch_ci2.png)

(github-pr-test)=

## Testare elementi in una pull request (azioni CI di GitHub deploy)

Disponibile dalla versione 3.3.2.1.dev

 - Adatto per tester o per coloro che aiutano nel testing.

```{eval-rst}
.. raw:: html

    <!--crowdin: exclude-->
    <div align="center" style="max-width: 360px; margin: auto; margin-bottom: 2em;">
      <div style="position: relative; width: 100%; aspect-ratio: 9/16;">
        <iframe
          src="https://www.dailymotion.com/embed/video/x9rdx1q"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
          frameborder="0"
          allowfullscreen>
        </iframe>
      </div>
    </div>
```

![aaps_ci_pr_ci](../images/Building-the-App/CI/aaps_ci_pr_ci.png)

- Numero PR: Inserire il numero della PR che si vuole testare.

- Tipi di riferimento PR: I tipi di riferimento PR includono due opzioni:

  - head:
    - Recupera il contenuto effettivo dal ramo dell'autore della PR (cioè, la cronologia dei commit originale senza operazioni di merge).
    - Equivale allo stato originale del ramo PR, come se fosse recuperato direttamente da un fork o da un ramo di funzionalità.

  - merge:
    - Recupera il risultato del merge pre-simulato di GitHub della PR nel ramo di destinazione (ad es. dev).
    - Si tratta di un commit di merge virtuale creato automaticamente da GitHub.
    - Questo commit esiste solo quando la PR non ha conflitti e può essere sottoposta a merge.

  - variant:
    - Vedi [variante](#browserbuild-variant)
