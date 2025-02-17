* * *

orphan: true

* * *

# Pompe Accu-Chek Combo

**Ce logiciel est un système "Do it yourself" (faire soi-même), et ce n’est pas un produit fini destiné à la mise sur le marché. VOUS devez obligatoirement lire, apprendre et comprendre ce système, y compris la façon de l’utiliser. Ce logiciel ne fait pas toute la gestion de votre diabète pour vous, mais il peut améliorer votre diabète et votre qualité de vie si vous êtes prêt à y consacrer le temps nécessaire. Ne vous précipitez pas, mais laissez vous le temps d’apprendre. Attention, vous êtes le seul responsable de ce que vous faite avec ce système.**

(Accu-Chek-Combo-Pump-hardware-requirements)=

## Configuration matérielle requise

- Une pompe Roche Accu-Chek Combo (avec n’importe quel firmware, ils fonctionnent tous)
- Un dispositif Accu-Chek Smartpix V1 ou Accu-Chek Realtyme, ainsi que le logiciel de configuration Accu-Chek 360. (Sur demande Roche envoie gratuitement ces dispositifs Smartpix et la configuration logiciel à leurs clients, sauf en France ou il faut contacter son prestataire).
- Un téléphone compatible : un smarphone Android avec comme système LineageOS 14.1 (anciennement CyanogenMod) ou Android 8.1 (Oreo). Depuis AAPS 3.0, Android 9 est obligatoire. See [release notes](#maintenance-android-version-aaps-version) for details.
- Avec LineageOS 14.1, il doit être une version récente d’au moins juin 2017 car les changements nécessaires pour se connecter à la pompe Combo ont été mis en œuvre seulement à ce moment-là. 
- A list of phones can be found in the [AAPS Phones](#Phones-list-of-tested-phones) document.
- Cette liste n’est pas une liste complète. Elle reflète l’expérience personnelle de quelques utilisateurs. Nous vous encourageons à partager également votre expérience et ainsi aider les autres.
- Ayez bien en tête que bien qu'Android 8.1 autorise la communication avec le Combo, il y a toujours des problèmes avec AAPS sur 8.1.
- Pour les utilisateurs avancés, il est possible d'effectuer l'appairage sur un téléphone rooté et de le transférer vers un autre téléphone qui doit également être rooté pour l'utiliser avec Ruffy/AAPS. Ceci permet d'utiliser des téléphones avec [Android 8.1](https://github.com/gregorybel/combo-pairing/blob/master/README.md) mais n'a pas été largement testé.

## Limitations

- Extended bolus and multiwave bolus are not supported (see [Extended Carbs](../DailyLifeWithAaps/ExtendedCarbs.md) instead).
- Seulement un profil de basal est pris en charge.
- Sélectionner un profil de basal autre que 'Basal1' sur la pompe, ou délivrer via la pompe des bolus 'carré' et 'mixte', interfère avec les DBT et force la boucle en mode 'AGB' pendant 6 heures car la boucle ne peut pas fonctionner en toute sécurité dans ces conditions.
- It's currently not possible to set the time and date on the pump, so [daylight saving time changes](#time-adjustment-daylight-savings-time-dst) have to be performed manually (you may disable the phone's automatic clock update in the evening and change it back in the morning together with the pump clock to avoid an alarm during the night).
- Actuellement, seuls les débits de basals de 0,05 à 10 U/h sont supportés. Ceci s'applique également lors de la modification du profil, par exemple, lorsqu'il augmente à 200%, le taux basal le plus élevé ne doit pas dépasser 5 U/h car il sera doublé. De même, en réduisant à 50%, le taux basal le plus bas doit être au moins 0,10 U/h.
- Si la boucle demande l'annulation d'un DBT en cours, le Combo fixera un DBT de 90% ou 110% pendant 15 minutes à la place. C'est parce que l'annulation d'un DBT provoque une alerte sur la pompe qui cause beaucoup de vibrations.
- Occasionnellement (tous les deux jours ou plus), AndroidAPS risque de ne pas annuler automatiquement une alerte 'TBR CANCELLED', donc l’utilisateur doit s’en occuper (en appuyant sur le bouton actualiser dans AndroidAPS afin de transférer l’alarme à AAPS, ou en confirmant l’alerte sur la pompe).
- La stabilité de la connexion Bluetooth varie en fonction des téléphones utilisés. La perte de connection provoque des alertes "pompe injoignable", pendant laquelle aucune connexion avec la pompe n'est établie. 
- Si cette erreur survient, assurez-vous que Bluetooth est activé, puis appuyez sur le bouton Rafraichir dans l'onglet Combo pour voir si cela a été causé par un problème intermittent. Si aucune connexion n'est encore établie, le redémarrage du téléphone devrait normalement corriger cela. 
- Il y a une autre solution si le redémarrage du téléphone n'a pas aidé. Il s'agit de presser un bouton sur la pompe (pour réinitialiser le Bluetooth de la pompe) afin que celle-ci accepte de nouveau les connexions du téléphone. 
- A ce stade, il n’y a plus de solution pour remédier à la perte de connections. Si vous voyez souvent ces erreurs, votre seule option est d'acquérir un autre téléphone connu pour fonctionner correctement avec AAPS et le Combo (voir ci-dessus).
- Un bolus délivré à partir de la pompe ne sera pas toujours détecté immédiatement (il faut vérifier à chaque fois qu'AndroidAPS est bien connecté à la pompe), et cela peut prendre jusqu'à 20 minutes dans le pire des cas. 
- Les bolus sur la pompe sont toujours vérifiés avant un DBT élevé ou un bolus délivré par AAPS, mais en raison des limitations, AAPS refusera ensuite de délivrer le DBT/Bolus comme il a été calculé sous de fausses prédictions. (-> La solution est de ne pas délivrer de bolus via la pompe! See chapter [Usage](#usage) below)
- Le paramétrage d'un DBT sur la pompe doit être évité puisque la boucle assure le contrôle des DBT. La détection d'un nouveau DBT sur la pompe peut prendre jusqu'à 20 minutes et l'effet du DBT est seulement comptabilisé à l’instant où il est détecté, donc dans le pire des cas, il peut y avoir 20 minutes d’un DBT qui n’est pas pris en compte dans l’IA. 

## Paramètres

- Configurez la pompe en utilisant le logiciel de configuration Accu-Chek 360. 
- Si vous n’avez pas le logiciel, veuillez contacter votre prestataire en france ou la hotline Accu-Chek dans les autres pays. Ils envoient généralement aux utilisateurs enregistrés un CD ou une clé USB avec le logiciel de configuration de la pompe et un périphérique de connexion infrarouge USB SmartPix (le périphérique Realtyme fonctionne aussi si vous en avez). Ou cherchez sur un forum de votre pays.
- **Paramètres requis** (marqués en vert dans les captures d'écran) :
    
    - Choisissez ou laissez la configuration du menu sur "Standard", cela affichera uniquement les menus et actions pris en charge sur la pompe, et masquera ceux qui ne sont pas supportés par AAPS (bolus duo/carré, débits de base multiples) et qui entraînent une limitation du fonctionnement de la boucle lors de leurs utilisation, et donc ne permet pas une exécution sécurisée de la boucle.
    - Vérifiez le *Quick Info Text* est défini à "QUICK INFO" (sans les guillemets, trouvés sous *Insulin Pump Options*).
    - Paramétrez le DBT *Maximum Adjustment* à 500%
    - Désactivez *Signal End of Temporary Basal Rate*
    - Paramétrez le DBT *Duration increment* à 15min
    - Activez le Bluetooth

- **Paramètres recommandés** (marqués en bleu dans les captures d'écran) :
    
    - Définissez une alarme de cartouche basse à votre convenance
    - Configurez un bolus max adapté à votre thérapie afin de se protéger contre les bugs logiciel et matériel
    - De même, configurez une durée maximale de débit de basal temporaire DBT en tant que protection. Autorisez au moins 3 heures, puisque l'option de déconnecter la pompe pendant 3 heures défini un DBT à 0% pendant 3 heures.
    - Activez le verrouillage des touches sur la pompe pour empêcher les bolus via la pompe, surtout si la pompe a déjà été utilisée et que vous aviez l'habitude d'utiliser les bolus rapides.
    - Définissez un délai d'affichage et de menu aux valeurs minimales respectivement de 5,5s et 5s. Cela permet à AAPS de récupérer plus rapidement de situations d’erreur et réduit la quantité de vibrations qui peuvent se produire pendant ces erreurs.

![Capture d’écran de réglages du menu utilisateur](../images/combo/combo-menu-settings.png)

![Capture d'écran des paramètres DBT](../images/combo/combo-tbr-settings.png)

![Capture d'écran des paramètres de bolus](../images/combo/combo-bolus-settings.png)

![Capture d'écran des paramètres de cartouche d'insuline](../images/combo/combo-insulin-settings.png)

- Installez AAPS comme décrit dans le wiki [AAPS](https://androidaps.readthedocs.io/)
- Assurez vous de bien lire le wiki pour comprendre comment configurer AAPS.
- Sélectionnez le plugin MDI dans AAPS, surtout pas le plugin Combo à ce stade afin d'éviter que le plugin Combo n'interfère avec Ruffy pendant le processus d'appairage.
- Clonez ruffy via git depuis [MilosKozak/Ruffy](https://github.com/MilosKozak/ruffy). Pour le moment, la branche principale est la branche `combo` , en cas de problème, vous pouvez également essayer la branche 'appairage' (voir ci-dessous).
- Construisez et Installez Ruffy et utilisez le pour appairer la pompe. S'il ne fonctionne pas après plusieurs tentatives, passez à la branche `pairing`, appairez la pompe puis reprenez le fil de cette page. Si la pompe est déjà appariée et peut être contrôlée via Ruffy, l'installation de la branche `combo` est suffisante. Notez que l'appairage doit seulement être lancé une fois, le traitement est un peu fragile et long car il peut y avoir plusieurs tentatives; Acquittez rapidement les notifications et si vous recommencez, supprimez de la liste Bluetooth du téléphone le dispositif pompe au préalable. Une autre option à essayer est d’aller dans le menu Bluetooth après l’initialisation du processus d’appairage (cela permet de maintenir le Bluetooth du téléphone détectable tant que le menu est affiché) et à revenir à Ruffy après la confirmation de l’appairage sur la pompe, lorsque la pompe affiche le code d’autorisation. Si vous n’avez pas réussi l’appairage de la pompe (disons après 10 tentatives), essayez d’attendre jusqu'à 10s avant de confirmer l’appairage sur la pompe (lorsque le nom du téléphone est affiché sur la pompe). Si vous avez configuré ci-dessus le délai d'affichage du menu à 5s, vous devez l'augmenter à nouveau. Certains utilisateurs ont signalé qu'ils avaient eu besoin de le faire. Enfin, envisagez de passer dans une autre pièce en cas d’interférence avec des ondes radio. Au moins un utilisateur a immédiatement résolu les problèmes d'appairage en changeant simplement de pièce.
- Quand AAPS utilise Ruffy, l'application Ruffy ne peut pas être utilisée. La façon la plus simple est de redémarrer le téléphone après le processus d'appairage et de laisser AAPS démarrer ruffy en arrière-plan.
- Si la pompe est complètement nouvelle, vous devez faire un bolus sur la pompe pour que celle-ci crée une première entrée dans l'historique.
- Avant d'activer le plugin Combo dans AAPS, assurez-vous que votre profil est bien configuré et activé et que votre profil de basal est à jour car AAPS synchronisera le profil basal à la pompe. Ensuite, activez le plugin Combo. Appuyez sur le bouton *Actualiser* dans l'onglet Combo pour initialiser la pompe.
- Pour vérifier votre configuration, avec la pompe **déconnectée**, utilisez AAPS pour définir un DBT de 500% pendant 15 min et faite un bolus. La pompe doit normalement avoir un DBT en cours et un bolus dans l'historique. AAPS doit aussi de son côté montrer le DBT actif et le bolus délivré.

(Accu-Chek-Combo-Pump-why-pairing-with-the-pump-does-not-work-with-the-app-ruffy)=

## Pourquoi l'appairage avec la pompe ne fonctionne pas avec l'application "Ruffy"?

Il y a plusieurs raisons possibles. Essayez les étapes suivantes :

1. Insérer une **pile neuve ou un accu complètement chargé** dans la pompe. Consultez la section "Considérations relatives à la pile" pour plus de détails. Assurez-vous que la pompe est très proche du smartphone.

![Le Combo doit être proche du téléphone](../images/Combo_next_to_Phone.png)

2. Désactivez ou supprimez tous les autres périphériques bluetooth afin qu'ils ne soient pas en mesure d'établir une connexion au téléphone pendant que l'appairage est en cours. Toute communication bluetooth parallèle ou demande de connexions peut perturber le processus d'appairage.

3. Supprimez tous les appareils connectés dans le menu Bluetooth de la pompe : **RÉGLAGE BLUETOOTH / CONNEXION / SUPPR. APPAREIL** jusqu'à ce que **AUCUN APPAREIL LIÉ** soit affiché.

4. Supprimer une pompe déjà connecté au téléphone via Bluetooth : dans Paramètres / Bluetooth, retirez l'appareil couplé "**SpiritCombo**"
5. Assurez-vous que AAPS n'exécute pas la boucle en arrière-plan. Désactiver la boucle dans AAPS.
6. Essayez d'utiliser la branche '**appairage**' du dépôt [MilosKozak/Ruffy](https://github.com/MilosKozak/ruffy/tree/pairing) pour établir la connexion 
7. Maintenant, démarrez ruffy sur le téléphone. Vous pouvez appuyer sur Reset! et supprimez l'ancienne connexion. Puis appuyez sur **Connect!**.
8. Dans le menu Bluetooth de la pompe, allez à **ADD DEVICE / ADD CONNECTION**. Appuyez sur **CONNECTER !** 
    - Les trois étapes suivantes sont sensibles au timing, donc vous devrez essayer différentes pauses / vitesses si le jumelage échoue. Lisez la séquence complète avant de l'essayer.

9. A présent, la pompe doit afficher le nom BT du téléphone à sélectionner pour l'appairage. Ici, il est important d'attendre au moins 5s avant de cliquer sur le bouton de sélection sur la pompe. Sinon, la Pompe n'enverra pas correctement la demande d'appairage au téléphone.
    
    - Si le délai d'affichage de l'écran de la pompe Combo est défini sur 5s, vous pouvez faire le test avec 40s (paramètre d'origine). Par expérience la durée entre le moment où la pompe est affichée sur le téléphone et celui où le téléphone est sélectionné est d'environ 5-10s. Dans de nombreux autres cas, le couplage expire sans succès. Ultérieurement, vous devrez le redéfinir sur 5 s pour répondre aux paramètrage du combo dans AAPS et accélérer les connexions.
    - Si la pompe n'affiche pas du tout le téléphone comme appareil de couplage, la puce Bluetooth de votre téléphone n'est probablement pas compatible avec la pompe. Vérifiez que vous exécutez une version de **LineageOS ≥ 14.1** ou **Android ≥ 8.1 (Oreo)**. Si possible, essayez un autre smartphone. You can find a list of already successfully used smartphones under [AAPS Phones](#Phones-list-of-tested-phones). 

10. Parfois, le téléphone demande un code PIN bluetooth (typiquement 4 chiffres) qui n'est pas lié au PIN à 10 chiffres affiché plus tard sur la pompe. Habituellement, Ruffy défini ce code PIN automatiquement, mais cela ne fonctionne pas toujours. Si une demande de code PIN d'appairage Bluetooth apparaît sur le téléphone avant qu'un code ne soit affiché sur la pompe, vous devez entrer **}gZ='GD? j2r|B}>** comme code PIN. C'est plus facile si vous copiez ce texte de 16 caractères dans le presse-papiers avant de commencer la séquence d'appairage et juste coller dans la boîte de dialogue à cette étape. Voir le [problème Github](https://github.com/MilosKozak/ruffy/issues/14) associé pour plus de détails.

11. Ensuite la pompe doit afficher un code de sécurité à 10 chiffres, et Ruffy affiche un écran pour le renseigner. Donc entrez le dans Ruffy et vous devriez être prêt.
12. Si l'appairage a échoué et que vous avez obtenu un message hors délai sur la pompe, vous devrez redémarrer le processus de zéro.
13. Si vous avez utilisé la branche 'appairage' pour construire l'application Ruffy, installez maintenant la version de version à partir de la branche 'combo' au-dessus de celle-ci. Assurez-vous que vous avez utilisé les mêmes clés lors de la signature des deux versions de l'application pour conserver tous les paramètres et les données, car elles contiennent aussi les propriétés de connexion.
14. Redémarrer le téléphone.
15. Maintenant, vous pouvez redémarrer la boucle AAPS.

(Accu-Chek-Combo-Pump)=

## Utilisation

- Gardez à l'esprit qu'il ne s'agit pas d'un produit, en particulier au début, l'utilisateur doit surveiller et comprendre le système, ses limites et comment il peut échouer. Il est fortement conseillé de NE PAS utiliser ce système lorsque la personne n'est pas en mesure de bien le comprendre entièrement.
- Lisez la documentation d'OpenAPS https://openaps.org pour comprendre l'algorithme de boucle sur lequel est basé AAPS.
- Lisez la documentation en ligne pour en savoir plus sur AAPS https://androidaps.readthedocs.io/
- Cette intégration utilise la même fonctionnalité que le lecteur fournit avec le Combo. Le lecteur permet de reproduire l'écran de la pompe et de transférer à la pompe les appuis sur les touches. La connexion à la pompe et la redirection des boutons est ce que fait l'application ruffy. Un `automate` lit les informations de l'écran et automatise la saisie des bolus, des DBTs, etc. et s'assure que les entrées sont traitées correctement. AAPS interagit ensuite avec l'automate pour appliquer les commandes de la boucle et pour administrer des bolus. Ce mode a quelques restrictions : il est relativement lent (mais suffisament rapide pour l'usage qu'on en fait), et quand on active un DBT ou un bolus, cela fait vibrer la pompe.
- L'intégration de la Combo avec AAPS part du principe que toutes les entrées de données sont faites via AAPS. Les bolus entrés directement sur la pompe seront détectés par AAPS, mais cela peut prendre jusqu'à 20 min avant qu'AAPS ne prenne connaissance d'un tel bolus. Les bolus saisis directement sur la pompe sont lus et pris en compte dans AAPS par sécurité, mais ce n'est pas une fonction destinée à être utilisée régulièrement (la boucle doit également connaitre les glucides consommés qui, eux, ne peuvent pas être saisis sur la pompe, ce qui est une autre raison pour laquelle toutes les entrées devraient être faites dans AAPS).
- Ne faites pas ou n'annulez pas de DBT sur la pompe. La boucle assure le contrôle des DBT et ne peut pas fonctionner de manière fiable autrement, car il n'est pas possible de déterminer l'heure exacte du début d'un DBT qui a été défini par l'utilisateur sur la pompe.
- Le profil 1 de la pompe pour les débits de basal est lu au démarrage de l'application et est mis à jour par AAPS. Le débit de basal ne doit pas être modifié manuellement sur la pompe, mais il sera détecté et corrigé en tant que mesure de sécurité (il ne faut en revanche pas compter sur ces mesures de sécurité par défaut, elles sont simplement destinées à détecter des modifications non intentionnelles effectuées sur la pompe).
- Il est recommandé d'activer le verrouillage sur la pompe pour empêcher les bolus à partir de la pompe, en particulier quand la pompe a déjà été utilisée et que vous aviez l'habitude d'utiliser les bolus rapides. Aussi, lorsque le verrouillage du clavier est activé, un appui accidentellement sur une touche n'interrompra PAS la communication active entre AAPS et la pompe.
- Lorsqu'une alerte BOLUS/DBT ANNULÉ débute à la pompe pendant un bolus ou la configuration d'un DBT, c'est causé par une déconnexion entre la pompe et le téléphone, ce qui arrive de temps à autre. AAPS tentera de se reconnecter et de confirmer l'alerte, puis de relancer la dernière action (les bolus ne sont PAS relancés pour des raisons de sécurité). Par conséquent, une telle alarme peut être ignorée car AAPS la confirmera automatiquement, généralement dans les 30 secondes (l'annuler n'est pas un problème, mais retardera l'action en cours pour attendre que l'affichage de la pompe s'éteigne avant de pouvoir se reconnecter à la pompe). Si l'alarme de la pompe se poursuit, la confirmation automatique a échoué, dans ce cas l'utilisateur doit confirmer l'alarme manuellement.
- Lorsqu'une alerte cartouche faible ou batterie faible est déclenchée pendant un bolus ils sont confirmés et affichés comme une notification dans AAPS. S'ils se produisent alors qu'aucune connexion n'est ouverte avec la pompe, allez dans l'onglet Combo et appuyez sur le bouton Rafraîchir pour forcer la confirmation de ces alertes et afficher une notification dans AAPS.
- Lorsqu'AAPS ne parvient pas à confirmer une alerte DBT ANNULÉE, ou si une autre alerte est déclenchée pour une raison différente, le fait d'activer Actualiser dans l'onglet Combo établit une connexion, confirme l'alerte et affiche la notification correspondante dans AAPS. Cela peut être fait en toute sécurité, car ces alertes sont bénignes : un DBT approprié sera défini lors à nouveau lors de la prochaine itération de la boucle.
- Pour toutes les autres alertes déclenchées par la pompe, la connexion à la pompe montrera le message d'alerte dans l'onglet Combo : p.ex. "Etat: E4: Occlusion" et affichage d'une notification sur l'écran principal. Une erreur déclenchera une notification urgente. AAPS ne confirme jamais les erreurs graves sur la pompe, mais laisse la pompe vibrer et sonner pour s'assurer que l'utilisateur est informé d'une situation critique qui nécessite une action.
- Après l'appairage, Ruffy ne doit pas être utilisé directement (AAPS le lancera en arrière-plan si nécessaire), car l'utilisation simultanée de ruffy sur AAPS n'est pas prise en charge.
- Si AAPS se bloque (ou est arrêté à partir du débogueur), alors que AAPS et la pompe étaient en communication (via Ruffy), il peut être nécessaire de forcer la fermeture de Ruffy. Le fait de redémarrer AAPS redémarrera à nouveau Ruffy. Redémarrer le téléphone est aussi un moyen facile de résoudre cela si vous ne savez pas comment forcer l'arrêt d'une application.
- N'appuyez jamais sur les boutons de la pompe quand AAPS communique avec celle-ci (le logo Bluetooth est affiché sur la pompe).