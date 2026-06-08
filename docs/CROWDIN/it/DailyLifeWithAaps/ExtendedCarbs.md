(Extended-Carbs-extended-carbs-ecarbs)=
# Carboidrati estesi / "eCarbs"

## Cosa sono gli eCarbs e quando sono utili?

Con la terapia con microinfusore tradizionale, i boli estesi sono un buon metodo per gestire pasti grassi o comunque ad assorbimento lento, che aumentano la glicemia più a lungo di quanto dura l'effetto dell'insulina. Nel contesto del loop, tuttavia, i boli estesi non hanno molto senso (e pongono difficoltà tecniche), poiché sono essenzialmente una basale temporanea elevata e fissa, che va contro il funzionamento del loop, il quale regola la basale in modo dinamico. Per i dettagli vedere [bolo esteso](#extended-bolus-and-why-they-wont-work-in-closed-loop-environment) di seguito.

La necessità di gestire tali pasti esiste comunque. Ecco perché AAPS dalla versione 2.0 supporta i cosiddetti carboidrati estesi o eCarbs.

Gli eCarbs sono carboidrati suddivisi su più ore. Per i pasti standard con più carboidrati che grassi/proteine, inserire i carboidrati in anticipo (e ridurre il bolo iniziale se necessario) è solitamente sufficiente per evitare una somministrazione di insulina troppo precoce.  Ma per i pasti ad assorbimento più lento, in cui l'inserimento completo dei carboidrati in anticipo genera troppa IOB dagli SMB, è possibile usare gli eCarbs per simulare più accuratamente come i carboidrati (e qualsiasi equivalente di carboidrati inserito per altri macronutrienti) vengono assorbiti e influenzano la glicemia. Con queste informazioni, il loop può somministrare SMB in modo più graduale per gestire quei carboidrati, il che può essere visto come un bolo esteso dinamico (questo dovrebbe funzionare anche senza SMB, ma probabilmente è meno efficace).

**Nota:** gli eCarbs non si limitano ai pasti ricchi di grassi/proteine: possono essere usati anche per gestire qualsiasi situazione in cui vi siano influenze che aumentano la glicemia, ad esempio altri farmaci come i corticosteroidi.

## Modalità di utilizzo degli eCarbs

Per inserire gli eCarbs, impostare una durata nella finestra di dialogo *Carboidrati* nella scheda panoramica, il totale dei carboidrati e, facoltativamente, uno sfasamento temporale (*i numeri sottostanti sono solo esempi; sarà necessario provare i propri valori per ottenere una risposta glicemica soddisfacente per i propri casi d'uso*):

![Enter carbs](../images/eCarbs_Dialog.png)

Gli eCarbs nella scheda panoramica; si notino i carboidrati tra parentesi nel campo COB, che mostra i carboidrati futuri:

![eCarbs in graph](../images/eCarbs_Graph.png)

______________________________________________________________________

Un metodo per gestire grassi e proteine con questa funzionalità è descritto qui: [https://adriansloop.blogspot.com/2018/04/page-margin-0.html](https://adriansloop.blogspot.com/2018/04/page-margin-0.html)

______________________________________________________________________

## Configurazione consigliata, scenario di esempio e note importanti

La configurazione consigliata prevede l'utilizzo del plugin APS OpenAPS SMB, con SMB abilitato e la preferenza *Abilita SMB con COB* attivata.

Uno scenario, ad esempio per una pizza, potrebbe essere quello di somministrare un bolo (parziale) in anticipo tramite il *calcolatore* e poi usare il pulsante *carboidrati* per inserire i carboidrati rimanenti per una durata di 4-6 ore, a partire da 1 o 2 ore dopo.

**Note importanti:** sarà necessario sperimentare per trovare i valori concreti più adatti alle proprie esigenze. Si potrebbe anche regolare con attenzione l'impostazione *minuti massimi di basale per limitare SMB a* per rendere l'algoritmo più o meno aggressivo. Con pasti a basso contenuto di carboidrati e alto contenuto di grassi/proteine, potrebbe essere sufficiente usare solo gli eCarbs senza boli manuali (vedere il post del blog sopra). Quando vengono generati gli eCarbs, viene creata anche una nota nel Careportal per documentare tutti gli input, in modo da semplificare l'iterazione e il miglioramento degli input.

(extended-bolus-and-why-they-wont-work-in-closed-loop-environment)=
## Bolo esteso e perché non funziona in un ambiente a loop chiuso?

Come menzionato sopra, i boli estesi o multiwave non funzionano davvero in un ambiente a loop chiuso. [Vedere sotto](#why-extended-boluses-wont-work-in-a-closed-loop-environment) per i dettagli.

(Extended-Carbs-extended-bolus-and-switch-to-open-loop-dana-and-insight-pump-only)=
### Bolo esteso e passaggio al loop aperto - solo microinfusori Dana e Insight

Alcune persone richiedevano la possibilità di usare comunque il bolo esteso in AAPS per poter trattare alimenti speciali nel modo a cui erano abituati.

Ecco perché dalla versione 2.6 esiste un'opzione per il bolo esteso per gli utenti dei microinfusori Dana e Insight.

- Il loop chiuso verrà automaticamente interrotto e si passerà alla modalità loop aperto per tutta la durata del bolo esteso.
- Le unità del bolo, il tempo rimanente e quello totale verranno mostrati nella schermata principale.
- Sul microinfusore Insight il bolo esteso *non è disponibile* se viene utilizzata l'[emulazione TBR](#Accu-Chek-Insight-Pump-settings-in-aaps).

![Extended bolus in AAPS 2.6](../images/ExtendedBolus2_6.png)

(why-extended-boluses-won-t-work-in-a-closed-loop-environment)=
### Perché i boli estesi non funzionano in un ambiente a loop chiuso

1. Il loop determina che ora devono essere somministrate 1,55 U/h. Che ciò venga somministrato come bolo esteso o TBR non è importante per l'algoritmo. Alcuni microinfusori usano effettivamente il bolo esteso. Cosa dovrebbe accadere allora? La maggior parte dei driver del microinfusore interrompe il bolo esteso -> non era nemmeno necessario avviarlo.

2. Se il bolo esteso fosse usato come input, cosa dovrebbe accadere nel modello?

   1. Dovrebbe essere considerato neutro insieme alla BR e messo in loop? Allora il loop dovrebbe anche poter ridurre il bolo se, ad esempio, la glicemia scende troppo e tutta l'insulina "neutrale" viene eliminata?
   2. Il bolo esteso dovrebbe semplicemente essere aggiunto? Quindi il loop dovrebbe semplicemente continuare? Anche nella peggiore delle ipoglicemie? Non sembra una buona idea: è prevista un'ipoglicemia ma non deve essere prevenuta?

3. L'IOB accumulato dal bolo esteso si materializza dopo 5 minuti alla successiva esecuzione. Di conseguenza, il loop eroga meno basale. Quindi non cambia molto... tranne che viene eliminata la possibilità di evitare l'ipoglicemia.
