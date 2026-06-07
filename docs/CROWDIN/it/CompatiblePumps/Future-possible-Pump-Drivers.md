# Driver futuri (possibili) per Microinfusori

Questo è un elenco di alcuni microinfusori disponibili sul mercato, con lo stato del supporto per i sistemi di loop e poi lo stato in AAPS. Alla fine ci sono alcune informazioni su cosa è necessario affinché un microinfusore sia "compatibile con il loop".

## Microinfusori che sono Loopable

### Kaleido ([Homepage](https://www.hellokaleido.com/))

**Stato loop:** Il microinfusore è un candidato al loop, ma il protocollo è sconosciuto al momento. Nessun interesse all'open source da parte del produttore.

**Requisito hardware per AAPS:** Nessuno. Sembra essere abilitato al Bluetooth.

### Tandem: t:slim X2 ([Homepage](https://www.tandemdiabetes.com/))

**Stato loop:** Non ancora compatibile con il loop.

Sebbene in passato l'azienda abbia deciso di non consentire il controllo dei propri microinfusori da dispositivi esterni, sembra che gli ultimi anni abbiano cambiato le carte in tavola. L'azienda ha deciso di aggiornare il microinfusore t:slim X2 per poter essere controllato da remoto (tramite l'app t:connect), il che significa che sono state aperte strade che potrebbero permetterci di controllare il microinfusore tramite AAPS in futuro. È previsto il rilascio a breve di un nuovo firmware del microinfusore (quest'anno o l'anno prossimo, prima dell'uscita del loro microinfusore tubeless t:sport). Non ci sono ancora dettagli su quali operazioni saranno possibili da t:connect (Bolo sicuramente, tutto il resto è sconosciuto).

**Requisito hardware per AAPS:** Nessuno. Sembra essere abilitato al Bluetooth.

### Tandem: t:Mobi & t:slim X3 & t:Mobi Tubeless ([Homepage](https://www.tandemdiabetes.com/about-us/pipeline))

**Stato loop:** Tutti e 3 i microinfusori saranno candidati al loop.

In attesa del rilascio di t:mobi in Europa (gli altri due non sono ancora stati rilasciati da nessuna parte). Lo sviluppo del supporto AAPS per t:mobi è già iniziato e dovrebbe essere disponibile entro la fine del 2025 (vedi ulteriori informazioni su Discord).

**Requisito hardware per AAPS:** Nessuno. Sembra essere abilitato al Bluetooth.

### Willcare Insulin pump ([Homepage](http://shinmyungmedi.com/en/))

**Stato loop:** Al momento non è un candidato al loop, ma siamo stati contattati dal loro staff e sono interessati ad estendere il loro microinfusore per renderlo compatibile con il loop (al momento penso che manchino solo i comandi get/set profilo).

**Requisito hardware per AAPS:** Nessuno. Sembra essere abilitato al Bluetooth.

**Commenti:** Poiché l'azienda è interessata all'integrazione con AAPS, potrebbe fare l'implementazione da sola.

## Microinfusori non più venduti (aziende non più operative)

### Animas Vibe

### Animas Ping

### Cellnovo

### Accu-Chek Insight

**Commenti:** Fine del supporto marzo 2025.

## Pumps that aren't Loopable

### Medtronic Bluetooth

**Commenti:** Nessun successo della comunità nel comunicare con il microinfusore Solo.

### Accu-Chek Solo

**Commenti:** Medtronic si è [ritirata](https://www.tidepool.org/blog/tidepool-loop-partner-update-ace-pumps).

### Ypsomed Pump

**Commenti:** Ypso ha aggiunto una crittografia di terze parti molto pesante.

## Requirements for pumps being loopable

**Prerequisito**
- Il microinfusore deve supportare qualche tipo di controllo remoto. (BT, radiofrequenza, ecc.)
- Il protocollo è stato hackerato/documentato/ecc.

**Requisito minimo**
- Imposta la basale temporanea
- Ottieni lo stato
- Annulla la basale temporanea

**Per oref1(SMB) o il bolo:**
- Imposta il bolo

**Good to have**
- Annulla il bolo
- Ottieni il profilo basale (quasi requisito)
- Imposta il profilo basale (bello avere)
- Leggi la cronologia

**Altro (non richiesto ma utile avere)**
- Imposta il bolo esteso
- Annulla il bolo esteso
- Leggi la cronologia
- Leggi il TDD

### Other pumps support

Se hai altri microinfusori di cui vorresti vedere lo stato, contattaci su Discord.
