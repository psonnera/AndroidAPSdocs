# Ramo sviluppatori (Dev)

<font color="#FF0000">**Attenzione:**</font> Il ramo Dev è solo usato per ulteriori sviluppi di AAPS. Dovrebbe essere usato su un telefono separato per testare <font color="#FF0000">**non per un circuito chiuso reale!**</font>

La versione più stabile di AAPS da usare è quella del ramo [Master](https://github.com/nightscout/AndroidAPS/tree/master).  Si consiglia di rimanere sul ramo Master per il circuito chiuso effettivo.

La versione dev di AAPS è solo per sviluppatori e collaudatori che sono al loro agio con le tracce dello stack, guardando attraverso i file di log e magari attivando il debugger per produrre segnalazioni di bug che sono utili agli sviluppatori (in breve: persone che sanno cosa stanno facendo senza essere assistite!). Quindi molte funzioni incompiute sono disabilitate. Per abilitare queste funzionalità entra in **Modalità Ingegneria** creando un file chiamato `engineering_mode` nella cartella /AAPS/extra . Abilitare la modalità di ingegneria potrebbe rompere completamente il circuito chiuso.

Tuttavia, il ramo Dev è un buon posto per vedere quali funzionalità vengono testate, per aiutare a risolvere i bug e dare un feedback su come le nuove funzionalità saranno implementate in pratica.  Spesso le persone testanno il ramo Dev su un vecchio telefono e micro fino a quando non sono sicuri che sia stabile - qualsiasi uso di esso è a tuo rischio.  Quando provi nuove funzionalità, ricorda che stai scegliendo di testare una funzionalità ancora in fase di sviluppo. Fai così al tuo rischio & con la dovuta diligenza per tenerti al sicuro.

Se trovi un bug o pensi che sia successo qualcosa di sbagliato quando usi il ramo Dev poi verificare nella [scheda Issues](https://github.com/nightscout/AndroidAPS/issues) di GitHub, per verificare se qualcun altro lo ha trovato, o aggiungerlo se nuovo.  Più informazioni puoi condividere qui meglio è (non dimenticare che potrebbe essere necessario condividere i tuoi [file di log](../GettingHelp/AccessingLogFiles.md).  Le nuove funzionalità possono essere discusse anche su [Discord](https://discord.gg/4fQUWHZ4Mw).

Una versione Dev ha una data di scadenza. Questo sembra scomodo quando lo usi in modo soddisfacente, ma serve a uno scopo. Quando una singola versione dev è in giro, è più facile tenere traccia degli errori che le persone segnalano. Gli sviluppatori non vogliono essere in una posizione in cui ci sono tre versioni di dev in giro, dove i bug sono risolti in alcuni e non altri, e la gente continua a segnalare quelli fissi.
