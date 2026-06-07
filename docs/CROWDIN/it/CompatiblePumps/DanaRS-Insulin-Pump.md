# Microinfusore DanaRS e Dana-i

_Queste istruzioni riguardano la configurazione dell'app e del microinfusore per chi possiede un DanaRS dal 2017 in poi o il più recente Dana-i. Visitare [Microinfusore DanaR](./DanaR-Insulin-Pump.md) se si possiede il DanaR originale._

**Il nuovo Dana-i può essere utilizzato dalla versione 3.0 di AAPS in poi.**

**Il nuovo firmware DanaRS v3 può essere utilizzato dalla versione 2.7 di AAPS in poi.**

* Nel microinfusore DanaRS/i, l'app utilizza "BASALE A". I dati esistenti vengono sovrascritti.

(DanaRS-Insulin-Pump-pairing-pump)=
## Pairing pump

* Nella schermata principale di AAPS fare clic sul menu hamburger nell'angolo in alto a sinistra e andare al Costruttore di configurazione.
* Nella sezione microinfusore selezionare 'Dana-i/RS'.
* Fare clic sull'ingranaggio per accedere direttamente alle impostazioni del microinfusore o tornare alla schermata principale.

  ![AAPS config builder Dana-i/RS](../images/DanaRS_i_ConfigB.png)

* Andare alla scheda 'DANA-i/RS'.
* Selezionare il menu preferenze toccando i 3 punti in alto a destra.
* Selezionare 'Preferenze Dana-i/RS'.
* Fare clic su "Microinfusore selezionato".
* Nella finestra di abbinamento, clicca sulla voce del tuo microinfusore.

  ![AAPS pair Dana-i/RS](../images/DanaRS_i_Pairing.png)

* **È necessario confermare l'associazione sul microinfusore!** Esattamente come si è abituati ad altre associazioni Bluetooth (ad es. smartphone e autoradio).

  ![Dana RS confirmation pairing](../images/DanaRS_Pairing.png)

* Seguire il processo di associazione in base al tipo e firmware del microinfusore:

   * Per DanaRS v1 selezionare la password del microinfusore nelle preferenze e impostare la propria password.
   * Per DanaRS v3 è necessario digitare 2 sequenze di numeri e lettere visualizzate sul microinfusore nella finestra di dialogo di associazione AAPS.
   * Per Dana-i appare la finestra di dialogo standard di associazione Android ed è necessario inserire il numero a 6 cifre visualizzato sul microinfusore.

* Selezionare Velocità bolo per cambiare la velocità predefinita del bolo (12 sec per 1U, 30 sec per 1U o 60 sec per 1U).
* Impostare il passo basale del microinfusore a 0,01 U/h usando il menu Medici (vedere il manuale utente del microinfusore).
* Impostare il passo bolo del microinfusore a 0,05 U/h usando il menu Medici (vedere il manuale utente del microinfusore).
* Abilita i boli estesi sul microinfusore

(DanaRS-Insulin-Pump-default-password)=

### Password predefinita

* Per DanaRS con firmware v1 e v2 la password predefinita è 1234.
* Per DanaRS con firmware v3 o Dana-i la password predefinita è derivata dalla data di produzione e si calcola come MMGG dove MM è il mese e GG è il giorno di produzione del microinfusore (ad es. '0124' che rappresenta il mese 01 e il giorno 24).

  * Dal MENU PRINCIPALE selezionare REVISIONE e poi aprire INFORMAZIONI SPEDIZIONE dal sottomenu
  * Il numero 3 è la data di produzione.
  * Per v3/i questa password viene utilizzata solo per bloccare il menu sul microinfusore. Non viene utilizzata per la comunicazione e non è necessario inserirla in AAPS.

(DanaRS-Insulin-Pump-change-password-on-pump)=
## Cambiare la password sul microinfusore

* Premere il pulsante OK sul microinfusore
* Nel menu principale selezionare "OPZIONE" (spostarsi a destra premendo più volte il tasto freccia)

  ![DanaRS Main Menu](../images/DanaRSPW_01_MainMenu.png)

* Nel menu opzioni selezionare "OPZIONE UTENTE"

  ![DanaRS Option Menu](../images/DanaRSPW_02_OptionMenu.png)

* Usare il tasto freccia per scorrere verso il basso fino a "11. password"

  ![DanaRS 11. Password](../images/DanaRSPW_03_11PW.png)

* Premere OK per inserire la vecchia password.

* Inserire la **vecchia password** (password predefinita vedere [sopra](#default-password)) e premere OK

  ![DanaRS Enter old password](../images/DanaRSPW_04_11PWenter.png)

* Se viene inserita la password sbagliata, non verrà mostrato alcun messaggio di errore!
* Impostare la **nuova password** (cambiare i numeri con i pulsanti + e - / spostarsi a destra con il tasto freccia).

  ![DanaRS New password](../images/DanaRSPW_05_PWnew.png)

* Confermare con il pulsante OK.
* Premere OK per salvare l'impostazione.

  ![DanaRS Save new password](../images/DanaRSPW_06_PWnewSave.png)

* Scorrere verso il basso fino a "14. USCITA" e premere OK per uscire.

  ![DanaRS Exit](../images/DanaRSPW_07_Exit.png)

(DanaRS-Insulin-Pump-dana-rs-specific-errors)=
## Errori specifici del Dana RS

### Errore durante l'erogazione dell'insulina
In caso di perdita della connessione tra AAPS e Dana RS durante l'erogazione del bolo insulinico (ad es. ci si allontana dal telefono mentre Dana RS sta erogando insulina), verrà visualizzato il seguente messaggio e si sentirà un suono di allarme.

![Alarm insulin delivery](../images/DanaRS_Error_bolus.png)

* Nella maggior parte dei casi si tratta solo di un problema di comunicazione e la quantità corretta di insulina viene erogata.
* Verifica nella la cronologia del microinfusore (sul microinfusore o tramite scheda Dana > cronologia del micro > boli) se è stato erogato il bolo giusto.
* Eliminare la voce di errore nella [scheda trattamenti](#screens-bolus-carbs) se si desidera.
* La quantità reale viene letta e registrata alla prossima connessione. Per forzarlo premere l'icona BT nella scheda Dana o aspettare la prossima connessione.

## Nota speciale quando si cambia telefono

Quando si passa a un nuovo telefono i seguenti passaggi sono necessari:
* [Esportare le impostazioni](../Maintenance/ExportImportSettings.md) sul vecchio telefono
* Trasferire le impostazioni dal vecchio al nuovo telefono

### DanaRS v1
* **Associare manualmente** Dana RS con il nuovo telefono
* Poiché le impostazioni di connessione del microinfusore vengono anche importate, AAPS sul nuovo telefono "conoscerà" già il microinfusore e quindi non avvierà una scansione Bluetooth. Pertanto il nuovo telefono e il microinfusore devono essere associati manualmente.
* Installare AAPS sul nuovo telefono.
* [Importare le impostazioni](../Maintenance/ExportImportSettings.md) sul nuovo telefono

### DanaRS v3, Dana-i
* Avviare la procedura di associazione come descritto [sopra](#pairing-pump).
* A volte potrebbe essere necessario cancellare le informazioni di associazione in AAPS tenendo premuta l'icona BT nella scheda Dana-i/RS.

## Viaggi con cambi di fuso orario con il microinfusore Dana RS

Per informazioni sui viaggi attraverso i fusi orari vedere la sezione [Viaggi con cambi di fuso orario con i microinfusori](#timezone-traveling-danarv2-danars).
