# Microinfusori Compatibili

AAPS funziona con un certo numero di microinfusori.  La seguente lista mostra i dispositivi attualmente supportati e indica se AAPS comunica con il microinfusore utilizzando la funzione Bluetooth nativa del telefono o se richiede un dispositivo compatibile Rileylink tra parentesi.

- [Accu-Chek Combo](../CompatiblePumps/Accu-Chek-Combo-Pump-v2.md) (Bluetooth; vedi anche [Accu-Chek Combo consigli per l'uso](../CompatiblePumps/Accu-Chek-Combo-Tips-for-Basic-usage.md))
- [Accu-Chek Insight](../CompatiblePumps/Accu-Chek-Insight-Pump.md) (Bluetooth)
- [DanaR](../CompatiblePumps/DanaR-Insulin-Pump.md) (Bluetooth)
- [DanaRS](../CompatiblePumps/DanaRS-Insulin-Pump.md) (Bluetooth)
- [Dana-i](../CompatiblePumps/DanaRS-Insulin-Pump.md) (Bluetooth)
- [Diaconn G8 ](../CompatiblePumps/DiaconnG8.md)  (Bluetooth)
- [EOPatch2](../CompatiblePumps/EOPatch2.md) (Bluetooth)
- [Omnipod Eros](../CompatiblePumps/OmnipodEros.md)  ([additional communication device](#CompatiblePumps-additional-communication-device) needed)
- [Omnipod DASH](../CompatiblePumps/OmnipodDASH.md)  (Bluetooth)
- [Medtrum Nano](../CompatiblePumps/MedtrumNano.md)  (Bluetooth)
- [Medtrum 300U](../CompatiblePumps/MedtrumNano.md)  (Bluetooth)
- [Equil 5.3](../CompatiblePumps/Equil5.3.md) (Bluetooth)
- Certain older [Medtronic](../CompatiblePumps/MedtronicPump.md) ([additional communication device](#CompatiblePumps-additional-communication-device) needed)

## Il mio microinfusore non è elencato

I dettagli sullo stato di altri microinfusori che potrebbero funzionare con AAPS sono elencati nella pagina [Futuri (possibili) Micro](../CompatiblePumps/Future-possible-Pump-Drivers.md).

(CompatiblePumps-additional-communication-device)=
## Dispositivo di comunicazione aggiuntivo

Se non viene menzionato alcun dispositivo di comunicazione aggiuntivo, la comunicazione tra il microinfusore e **AAPS** si basa sullo stack bluetooth integrato di Android, senza la necessità di un ulteriore dispositivo di comunicazione per tradurre il protocollo di comunicazione.

Per i vecchi micro Medtronic e Omnipod Eros, è necessario un dispositivo di comunicazione aggiuntivo (oltre al telefono) per "tradurre" il segnale radio dal micro a bluetooth. Assicurati di scegliere la versione corretta a seconda del micro.

- ![OrangeLink](../images/omnipod/OrangeLink.png)  [Sito Web OrangeLink](https://getrileylink.org/product/orangelink)
- ![RileyLink](../images/omnipod/RileyLink.png) [RileyLink 433MHz](https://getrileylink.org/product/rileylink433)
- ![EmaLink](../images/omnipod/EmaLink.png)  [Sito Web Emalink](https://github.com/sks01/EmaLink) - [Contatti](mailto:getemalink@gmail.com)
- ![DiaLink](../images/omnipod/DiaLink.png)  DiaLink - [Contatti](mailto:Boshetyn@ukr.net)
- ![LoopLink](../images/omnipod/LoopLink.png)  [Sito Web LoopLink](https://www.getlooplink.org/) - [Contatti](https://jameswedding.substack.com/) - Non Testato