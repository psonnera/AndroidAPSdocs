# ממשק AndroidAPS

## מסך הבית

![Homescreen V2.7](../images/Home2020_Homescreen.png)

זהו המסך הראשון שתתקלו בו בעת פתיחת AndroidAPS והוא מכיל את רוב המידע שתצטרכו ביום יום.

### חלק A - לשוניות

* ניווט בין מודולי AndroidAPS השונים.
* לחלופין ניתן לעבור בין המסכים ע"י החלקה שמאלה וימינה.
* Displayed tabs can be selected in [config builder](../SettingUpAaps/ConfigBuilder.md#tab-or-hamburger-menu).

### חלק B - פרופיל וערכי מטרה

#### פרופיל נוכחי

![Profile switch remaining duration](../images/Home2020_ProfileSwitch.png)

* הפרופיל הנוכחי מוצג בסרגל הימיני (כששפת המערכת עברית).
* לחיצה קצרה על הפרופיל מציגה את פרטי הפרופיל
* Long press profile bar to [switch between different profiles](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md#profile-switch--profile-percentage).
* אם החלפת הפרופיל בוצעה עם משך זמן מוגדר, הזמן הנותר מוצג בסוגריים.

#### ערך מטרה

![Temp target remaining duration](../images/Home2020_TT.png)

* ערך המטרה הנוכחי של הסוכר בדם מוצג בסרגל השמאלי (כששפת המערכת עברית).
* Short press target bar to set a [temporary target](../DailyLifeWithAaps/TempTargets.md).
* אם הוגדר ערך מטרה זמני, צבע הכפתור יצבע בצהוב והזמן הנותר בדקות מוצג בסוגריים.

#### הצגת שינויים דינמיים בערכי המטרה

![Visualization of dynamic target adjustment](../images/Home2020_DynamicTargetAdjustment.png)

* AAPS יכול להתאים באופן דינמי את ערכי המטרה על סמך הרגישות אם אתם משתמשים באלגוריתם SMB.
* Enable either one or both of the [following options](../SettingUpAaps/Preferences.md#openaps-smb-settings) 
   * "רגישות מעלה את ערך המטרה" ו\או 
   * "תנגודת מורידה את ערך המטרה" 
* אם AAPS מזהה תנגודת או רגישות, המטרה תשונה ממה שנקבע בפרופיל. 
* כאשר ערך המטרה ישונה, רקע כפתור ערך המטרה יצבע ירוק.

### חלק C - רמת הסוכר בדם וסטטוס לולאה

#### רמת סוכר נוכחית

* קריאת הסוכר האחרונה מהחיישן מוצגת בצד ימין.
* Color of the BG value reflects the status to the defined [range](../SettingUpAaps/Preferences.md#range-for-visualization). 
   * ירוק = בטווח
   * אדום = מתחת לטווח
   * צהוב = מעל הטווח
* הערכים האפורים באמצע מציגים דקות מאז הקריאה האחרונה ושינויים מאז הקריאה האחרונה, ב-15 וב-40 הדקות האחרונות.

#### סטטוס הלולאה

![סטטוס הלולאה](../images/Home2020_LoopStatus.png)

* סמל חדש מציג את מצב הלולאה:
   
   * עיגול ירוק = לולאה פועלת
   * green circle with dotted line = [low glucose suspend (LGS)](../SettingUpAaps/CompletingTheObjectives.md#objective-6-starting-to-close-the-loop-with-low-glucose-suspend)
   * מעגל אדום = לולאה מושבתת (קבוע)
   * עיגול צהוב = לולאה מושהת (השהיה זמנית אך אינסולין בזאלי יינתן) - הזמן שנותר להשהיה מוצג מתחת לסמל
   * עיגול אפור = המשאבה מנותקת (האופן זמני, ללא הזרמת כל אינסולין) - הזמן שנותר מוצג מתחת לסמל
   * עיגול כתום = סופר בולוס בפעולה - הזמן שנותר מוצג מתחת לסמל
   * עיגול כחול מְקֻוְוקָּו = לולאה פתוחה

* לחיצה קצרה או לחיצה ארוכה על הסמל תפתח את תיבת הדו-שיח 'לולאה' כדי להחליף מצב לולאה (סגור, השהיית עקב סוכר נמוך, פתיחה או השבתה), השהה / הפעל מחדש את הלולאה או נתק / חבר מחדש משאבה.
   
   * אם הלחיצה על סמל לולאה היתה קצרה, תידרשו לאשר את בחירתכם בתיבת דו-שיח לאחר בחירתכם
   
   ![Loop status menu](../images/Home2020_Loop_Dialog.png)

#### סימן אזהרה לצד רמת הסוכר

Beginning with Android 3.0, you might get a warning signal beneath your BG number on the main screen.

*הערה*: עד 30 השעות האחרונות נלקחות בחשבון בחישובים של AAPS. אז גם לאחר שפתרתם את בעיית המקור, עשויות לחלוף כ-30 שעות עד שהמשולש הצהוב ייעלם לאחר שהתרחש המרווח האחרון בנתונים.

כדי להסיר אותו באופן מיידי, יש למחוק ידנית כמה ערכים מלשונית xDrip או BYODA.

אולם, כשיש הרבה כפילויות, אולי יהיה קל יותר:

* [backup your settings](../Maintenance/ExportImportSettings.md),
* לאתחל את מסד הנתונים שלכם בתפריט התחזוקה
* [import your settings](../Maintenance/ExportImportSettings.md) again

##### סימן אזהרה אדום: כפילות בנתוני סוכר

סימן האזהרה האדום מסמל שנדרשת פעולה מיידית מצידכם: מקבלים נתוני סוכר כפולים, דבר שמפריע ללופ לתפקד. משום כך, הלופ עוצר את פעולתו עד שהמצב ייפתר.

![Red BG warning](../images/bg_warn_red.png)

עליכם לברר מדוע יש כפילות:

* גשר Dexcom מופעל בהגדרת אתר נייטסקאוט? בטלו את את הגשר ע"י כניסה לאתר Heroku שלכם, שנו בהגדרות את המשתנה Enable ובו מחקו את "bridge". (ניתן למצוא [פרטים לגבי Heroku כאן](https://nightscout.github.io/troubleshoot/troublehoot/#heroku-settings))
* האם יש יותר ממקור אחד להעלאות לנייטסקאוט? אם אתם משתמשים ב-BYODA, אפשרו את ההעלאה לנייטסקאוט ב-AAPS ואל תאפשרו את ההעלאה מ-xDrip אם הוא בשימוש.
* יש לכם עוקב שמקבל את נתוני הסוכר וגם מעלים נתוני סוכר לנייטסקאוט?
* מוצא אחרון: ב-AAPS, גשו להגדרות NSClient, בחרו בהגדרת הסינכרון וכבו את "קבלת נתוני סנסור מנייטסקאוט".

##### סימן אזהרה צהוב

* סימן האזהרה הצהוב מציין שהסוכר הגיע במרווחי זמן לא קבועים או שחלק מנתוני הסוכר חסרים.
   
   ![Yellow BG warning](../images/bg_warn_yellow.png)

* בדרך כלל אין צורך בנקיטת פעולה כלשהי. הלופ ימשיך לתפקד!

* מכיוון שהחלפת חיישן מפריעה לזרימה המתמדת של נתוני הסוכר, סימן אזהרה צהוב לאחר החלפת חיישן הוא נורמלי ואין ממה לדאוג.
* הערה מיוחדת למשתמשי Freestyle Libre:
   
   * כל חיישן Libre מזייף בדקה או שתיים כל כמה שעות, כלומר לעולם אינך מקבל זרימה מושלמת עם מרווחים קבועים לחלוטין.
   * גם קריאות קופצניות קוטעות את הזרימה הרציפה.
   * לכן סימן האזהרה הצהוב יהיה מופעל תמיד אצל משתמשי Libre.

### חלק D - אינסולין פעיל, פחמימות פעילות, מינונים בזאליים ורגישות

![Section D](../images/Home2020_TBR.png)

* מזרק: אינסולין פעיל (IOB) - כמות אינסולין הפעיל כרגע
   
   * נתון האינסולין הפעיל יהיה אפס אם רק הבזאלי הסטנדרטי מהפרופיל פועל ולא נשאר אינסולין מבולוסים קודמים. 
   * האינסולין הפעיל עשוי להיות שלילי אם היו לאחרונה תקופות של ירידה במינון הבזאלי.
   * לחצו על הסמל כדי לראות את הפיצול של הבולוס והאינסולין הבזאלי

* Grain: [carbs on board (COB)](CobCalculation) - yet unabsorbed carbs you have eaten before -> icon pulses if carbs are required

* קו סגול: מינון בזאלי - שינויים בסמל המשקפים שינויים זמניים במינון הבזאלי (שטוח ב-100%) 
   * לחצו על הסמל כדי לראות את המינון הבזאלי ופרטים של בזאלי זמני אם מופעל (כולל משך הזמן הנותר)
* Arrows up & down: indicating actual [autosens](KeyAapsFeatures#autosens) status (enabled or disabled) and value is shown below icon

#### דרושות פחמימות

![דרושות פחמימות](../images/Home2020_CarbsRequired.png)

* בקשות לפחמימות ניתנות כאשר המערכת מזהה שנדרשות פחמימות.
* זה קורה כאשר האלגוריתם מחשב שהוא לא יכול להציל אותכם מהיפוגליקמיה ע"י הפסקת המינון הבזאלי לבדו ולכן יש לאכול.
* הבקשות לפחמימות מתוחכמות בהרבה מאלה שמופיעות במחשבון הבולוס. ייתכן שתראו בקשות לפחמימות בעוד שמחשבון בולוס אינו מראה שחסרות פחמימות.
* הודעות של דרישה לפחמימות יכולות להישלח ל-Nightscout אם תרצו, ובמקרה זה תוצג ותשודר הודעה.

### חלק E - חיווי מצב

![Section E](../images/Home2020_StatusLights.png)

* נורות הסטטוס נותנות חיווי ויזואלי עבור 
   * גיל הצינורית
   * גיל אינסולין (משך השימוש במכל האינסולין הנוכחי)
   * רמת המכל (יחידות)
   * גיל חיישן
   * גיל ורמת הסוללה (%)
* אם חורגים מסף האזהרה, הערכים יוצגו בצהוב.
* אם חורגים מסף האזהרה הקריטי, הערכים יוצגו באדום.
* Settings can be made in [preferences](../SettingUpAaps/Preferences.md#status-lights).

### חלק F - גרף ראשי

![Section F](../images/Home2020_MainGraph.png)

* הגרף מציג את רמת הסוכר בדם (BG) כפי שנקרא מהחיישן. 
* הערות שהוזנו בלשונית פעולות, כגון כיולים מבדיקות עם גלוקומטר וערכים של פחמימות וכן החלפות פרופיל מוצגות כאן. 
* לחצו לחיצה ארוכה על הגרף כדי לשנות את קנה המידה של ציר הזמן. אפשר לבחור 6, 12, 18 או 24 שעות.
* האזור הירוק משקף את טווח המטרה. It can be configured in [preferences](../SettingUpAaps/Preferences.md#range-for-visualization).
* Blue triangles show [SMB](KeyAapsFeatures#super-micro-bolus-smb) - if enabled in [preferences](../SettingUpAaps/Preferences.md#openaps-smb-settings).
* מידע אופציונלי:
   
   * חיזוי
   * בזאלי
   * פעילות - עקומת פעילות אינסולין

#### הפעלת מידע אופציונלי

* לחצו על המשולש בצד שמאל של הגרף הראשי כדי לבחור איזה מידע יוצג בגרף הראשי.
* עבור הגרף הראשי זמינות רק שלוש האפשרויות שמעל ל-"\---\---- גרף 1 \---\----".
   
   ![Main graph setting](../images/Home2020_MainGraphSetting.png)

(Screenshots-prediction-lines)=

#### עקומי החיזוי

* **Orange** line: [COB](CobCalculation) (colour is used generally to represent COB and carbs)
   
   עקום החיזוי מראה לאן הסוכר (ולא לאן הפחמימות הפעילות עצמן!) ילך בהתבסס על הגדרות המשאבה הנוכחיות ובהנחה שהסטיות עקב ספיגת פחמימות נשארות קבועות. עקום זה מופיע רק אם יש פחמימות פעילות ידועות.

* עקום **כחול כהה**: אינסולין פעיל (כחול משמש בדרך כלל לייצוג אינסולין פעיל או כללי)
   
   עקום החיזוי מראה מה יקרה בהשפעת אינסולין לבדו. למשל אם הזרקתם קצת אינסולין ואז לא אכלתם פחמימות.

* עקום **כחול בהיר**: בזאלי אפס זמני (סוכר חזוי אם יוגדר קצב בזאלי זמני של 0%)
   
   עקום החיזוי מראה כיצד ישתנה עקום הסוכר בדם אם המשאבה תפסיק כל מתן אינסולין (בזאלי זמני 0%).
   
   *This line appears only when the [SMB](../SettingUpAaps/Preferences.md#advanced-meal-assist-ama-or-super-micro-bolus-smb) algorithm is used.*

* **Dark yellow** line: [UAM](../DailyLifeWithAaps/SensitivityDetectionAndCob.md#sensitivity-oref1) (un-announced meals)
   
   ארוחות לא מוכרזות מראש - זיהוי של עלייה משמעותית ברמות הסוכר עקב ארוחות, אדרנלין או השפעות אחרות. עקום החיזוי דומה לעקום הפחמימות הכתום אך הוא מניח שהסטיות יצטמצמו בקצב קבוע (על ידי הארכת קצב הדעיכה הנוכחי).
   
   *This line appears only when the [SMB](../SettingUpAaps/Preferences.md#advanced-meal-assist-ama-or-super-micro-bolus-smb) algorithm is used.*

* **עקום כתום כהה**: ספיגת פחמימות מואצת
   
   דומה לפחמימות פעילות אז מניח שספיגת הפחמימות קבועה ב-10 מ"ג\ד"ל\5דק'. מיושן ובעל תועלת מוגבלת.
   
   *This line appears only when the older [AMA](../SettingUpAaps/Preferences.md#advanced-meal-assist-ama-or-super-micro-bolus-smb) algorithm is used.*

בדרך כלל עקומת הסוכר האמיתית נמצאת באמצע בין העקומים הללו, או קרובה לזו שמניחה הנחות שהכי דומות למצבכם הנוכחי.

#### בזאלי

* עקום **כחול מלא** מציג את הבזאלי הבסיסי מהמשאבה ומשקף את הבזאלי בפועל לאורך זמן.
* הקו ה**כחול המקווקו** הוא המינון הבזאלי אם לא היה בזאלי זמני (TBR).
* בזמנים בהם המינון הבזאלי הוא הסטנדרטי (100% מזה המוגדר בפרופיל), השטח מתחת לעקומה מוצג בכחול כהה.
* כאשר מופעל מינון בזאלי זמנית (מוגבר או מופחת) השטח מתחת לעקומה מוצג בכחול בהיר.

#### פעילות

* העקום ה**צהוב הדק** מציג את פעילות האינסולין. 
* הוא מבוסס על הירידה הצפויה בסוכר בגלל אינסולין פעיל אם לא קיימים גורמים אחרים (כמו פחמימות).

### חלק G - גרפים נוספים

* ניתן להפעיל עד ארבעה גרפים נוספים מתחת לגרף הראשי.
* To open settings for additional graphs click the triangle on the right side of the [main graph](#section-f---main-graph) and scroll down.

![Additional graph settings](../images/Home2020_AdditionalGraphSetting.png)

* כדי להוסיף גרף נוסף יש לסמן את התיבה בצד שמאל של שמו (לדוגמה: \---\---- גרף 1 \---\---- וכו').

#### אינסולין מוחלט

* אינסולין פעיל כולל בולוסים **ואינסולין בזאלי**.

#### אינסולין פעיל

* מראה את האינסולין הפעיל. הוא כולל אינסולין מבולוס ובזאלי זמני (**אך אינו כולל מינונים בזאליים שנקבעו בפרופיל**).
* If there were no [SMBs](KeyAapsFeatures#super-micro-bolus-smb), no boluses and no TBR during DIA time this would be zero.
* אינסולין פעיל יכול להיות שלילי אם אין בולוס או בזאלי זמני אפס/נמוך למשך זמן רב יותר.
* Decaying depends on your [DIA and insulin profile settings](../SettingUpAaps/ConfigBuilder.md#local-profile). 

#### פחמימות פעילות

* מראה את הפחמימות הפעילות, שעדיין לא דעכו. 
* דעיכה תלויה בסטיות שהאלגוריתם מזהה. 
* אם הוא מזהה ספיגת פחמימות גבוהה מהצפוי, ינתן אינסולין וזה יגדיל את IOB (פחות או יותר, תלוי בהגדרות הבטיחות שלכם). 

#### סטיות

* עמודות **אפורות** מראות סטייה עקב פחמימות. 
* עמודות **ירוקות** מראות שרמת הסוכר גבוהה ממה שהאלגוריתם ציפה. Green bars are used to increase resistance in [Autosens](KeyAapsFeatures#autosens).
* עמודות **אדומות** מראות שרמת הסוכר נמוכה ממה שהאלגוריתם ציפה. Red bars are used to increase sensitivity in [Autosens](KeyAapsFeatures#autosens).
* עמודות **צהובות** מראות סטייה עקב ארוחות לא מוכרזות.
* עמודות **שחורות** מציגות סטיות קטנות שלא נלקחו בחשבון בחישוב הרגישות

#### רגישות

* Shows the sensitivity that [Autosens](KeyAapsFeatures#autosens) has detected. 
* חישוב רגישות לאינסולין כתוצאה מפעילות גופנית, תגובות הורמונליות וכו'.

#### פעילות

* מציג את פעילות האינסולין, מחושב לפי פרופיל האינסולין (אינה נגזרת של IOB). 
* הערך גבוה יותר עבור אינסולין כשמתקרבים לזמן השיא.
* ערך זה יהיה שלילי כאשר IOB יורד. 

#### שיפוע הסטייה

* ערך פנימי בשימוש באלגוריתם.

### סעיף H - כפתורים

![Homescreen buttons](../images/Home2020_Buttons.png)

* כפתורי אינסולין, פחמימות ומחשבון 'פועלים תמיד'.
   
   * אם החיבור למשאבה אובד, כפתור האינסולין מוסתר.

* Other Buttons have to be setup in [preferences](../SettingUpAaps/Preferences.md#buttons).

#### אינסולין

![Insulin button](../images/Home2020_ButtonInsulin.png)

* To give a certain amount of insulin without using [bolus calculator](#bolus-wizard).
* By checking the box you can automatically start your [eating soon temp target](../SettingUpAaps/Preferences.md#default-temp-targets).
* אם אינכם רוצים להכניס בולוס דרך המשאבה אלא לרשום את כמות האינסולין (כלומר אינסולין שניתן באמצעות מזרק) סמנו את התיבה המתאימה.

#### פחמימות

![Carbs button](../images/Home2020_ButtonCarbs.png)

* נועד לרישום פחמימות ללא בולוס.
* Certain [pre-set temporary targets](../SettingUpAaps/Preferences.md#default-temp-targets) can be set directly by checking the box.
* היסט זמן: מתי תאכלו פחמימות (בדקות) יחסית לעכשיו.
* Duration: To be used for ["extended carbs"](ExtendedCarbs)
* ניתן להשתמש בכפתורי התוספת כדי לרשום את מספר הפחמימות ביתר קלות.
* Notes will be uploaded to Nightscout - depending on your settings for [NS client](../SettingUpAaps/Preferences.md#nsclient).

#### מחשבון

* See Bolus Wizard [section below](#bolus-wizard)

#### כיולים

* שולח כיול ל- xDrip או פותח את חלון הכיול של אפליקציית Dexcom.
* Must be activated in [preferences](../SettingUpAaps/Preferences.md#buttons).

#### סנסור

* פותח את xDrip+.
* כפתור החזרה מחזיר ל-AAPS.
* Must be activated in [preferences](../SettingUpAaps/Preferences.md#buttons).

#### אשף מהיר

* הזנה בקלות של כמות הפחמימות והגדרת נתוני החישוב.
* Details are setup in [preferences](../SettingUpAaps/Preferences.md#quick-wizard).

## אשף הבולוס

![Bolus wizard](../images/Home2020_BolusWizard_v2.png)

כאן מתכננים במרבית המקרים את בולוסי הארוחה.

### חלק I

* שדה רמת הסוכר בדרך כלל כבר מאוכלס בקריאה האחרונה מהחיישן. אם אין לכם חיישן פעיל הוא יהיה ריק. 
* בשדה פחמימות אתם מוסיפים את ההערכה שלכם לכמות הפחמימות בארוחה שעבורה אתם רוצים לקבל בולוס. 
* שדה התיקון נועד לשינוי המינון הסופי באופן ידני.
* השדה זמן פחמימות מיועד לבולוס מקדים, כך שתוכלו לומר למערכת שיהיה עיכוב של הזמן שרשמתם לפני שהפחמימות צפויות. בכתיבת מספר שלילי בשדה זה אתם נותנים בולוס עבור פחמימות שנאכלו בעבר בעבר.

(Screenshots-eating-reminder)=

#### תזכורת אכילה

* עבור פחמימות עתידיות ניתן לסמן את תיבת סימון התזכורת (היא נבחרת כברירת מחדל כאשר מוזנת ארוחה עתידית) כך שתוכלו לקבל תזכורת לאכול את הפחמימות שהזנתם ל-AndroidAPS בהתאם לזמן שהזנתם ב-"זמן פחמימות"
   
   ![BolusWizard with Eating Reminder](../images/Home2021_BolusWizard_EatingReminder.png)

### חלק J

* סופר בולוס גורם להזרקת האינסולין הבזאלי של השעתיים הקרובות יחד עם בולוס הארוחה ובתמורה, מפעיל בזאלי זמני אפס במשך השעתיים הקרובות. The option only shows when "Enable [superbolus](../SettingUpAaps/Preferences.md#superbolus) in wizard" is set in the [preferences overview](../SettingUpAaps/Preferences.md#overview).
* הרעיון הוא לספק את האינסולין מוקדם יותר ובתקווה להפחית עליות חדות ברמות הסוכר.
* לפרטים עיינו ב-[diabetesnet.com](https://www.diabetesnet.com/diabetes-technology/blue-skying/super-bolus/).

### חלק K

* מציג את הבולוס המחושב. 
* אם כמות האינסולין הפעיל עולה על הבולוס המחושב, תוצג רק כמות הפחמימות הנדרשת.
* Notes will be uploaded to Nightscout - depending on your settings for [NS client](../SettingUpAaps/Preferences.md#nsclient).

### חלק L

* פרטים על חישוב הבולוס של המחשבון.
* אפשר לבטל את הבחירה של כל סעיף אותו לא תרצו לכלול בחישוב אבל בנסיבות רגילות, לא תרצו לבטלם.
* מטעמי בטיחות **יש לסמן את התיבה TT באופן ידני** אם ברצונכם שאשף הבולוס יחשב על פי ערך המטרה הזמני הנוכחי.

#### שילובים של COB ו-IOB ומשמעותם

* מטעמי בטיחות לא ניתן לבטל את סימון התיבה של IOB כאשר תיבת COB מסומנת מכיוון שאתם עלולים להסתכן בכמות גדולה מדי של אינסולין מכיוון ש-AAPS אינו מתייחס למה שכבר ניתן.
* אם תסמנו COB ו-IOB, פחמימות שעוד לא נספגו שלא כוסו כבר באינסולין + כל האינסולין שניתן כבזאלי זמני או כ-SMB יילקח בחשבון.
* אם תסמן IOB ללא COB, הלופ ייקח בחשבון את האינסולין שכבר ניתן, אך לא יכסה פחמימות שעוד לא נספגו. מצב זה מוביל להודעת "פחמימות חסרות".
* אם מזריקים בולוס עבור **מזון נוסף** זמן קצר לאחר בולוס ארוחה (לדוגמה קינוח), ייתכן שכדאי יהיה **לבטל את הסימון בכל התיבות**. כך רק הפחמימות החדשות מתווספות מכיוון שהארוחה העיקרית לא בהכרח תיספג ולכן IOB לא יתאים ל-COB במדויק זמן קצר לאחר בולוס הארוחה.

(Screenshots-wrong-cob-detection)=

#### זיהוי שגוי של פחמימות פעילות

![Slow carb absorption](../images/Calculator_SlowCarbAbsorption.png)

* אם האזהרה למעלה מופיעה לאחר שימוש באשף הבולוס, AndroidAPS זיהה שייתכן שערך הפחמימות הפעילות המחושב שגוי.
* לכן, אם תרצו להזריק בולוס לאחר ארוחה קודמת עם פחמימות פעילות, עליכם להיות מודעים למינון ביתר! 
* For details see the hints on [COB calculation page](CobCalculation#detection-of-wrong-cob-values).

(Screenshots-action-tab)=

## לשונית פעולות

![Actions tab](../images/Home2021_Action.png)

### פעולות - חלק M

* Button [profile switch](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md#profile-switch--profile-percentage) as an alternative to pressing the [current profile](#section-b---profile--target) on homescreen.
* Button [temporary target](../DailyLifeWithAaps/TempTargets.md) as an alternative to pressing the [current target](#section-b---profile--target) on homescreen.
* לחצן להפעלה או ביטול של מינון בזאלי זמני. שימו לב שהלחצן משתנה מ-"בזאלי זמני" ל-"ביטול %x" כאשר מוגדר מינון בזאלי זמני.
* Even though [extended boluses](ExtendedCarbs#extended-bolus-and-why-they-wont-work-in-closed-loop-environment) do not really work in a closed loop environment some people were asking for an option to use extended bolus anyway.
   
   * אפשרות זו קיימת רק במשאבות Dana RS ו-Accu chek Insight. 
   * לולאה סגורה תיעצר אוטומטית ותעבור למצב לולאה פתוחה למשך זמן פעילות הבולוס הממושך.
   * Make sure to read the [details](ExtendedCarbs) before using this option.

(Screenshots-careportal-section-n)=

### פורטל הטיפולים - חלק N

* מידע אודות תצוגת
   
   * גיל חיישן ואחוזי סוללה
   * גיל וכמות אינסולין (יחידות)
   * גיל הצינורית
   * גיל ודרגת טעינת סוללת המשאבה

* Less information will be shown if [low resolution skin](../SettingUpAaps/Preferences.md#skin) is used.

(Screenshots-sensor-level-battery)=

#### רמת טעינת סוללת החיישן

* דרוש xDrip nightly מדצמבר 10, 2020 או חדש יותר.
* עובד עם חיישנים ומשדרים כדוגמת MiaoMiao 2. (טכנית, החיישן צריך לשלוח את המידע של רמת הסוללה לxDrip+.)
* Thresholds can be set in [preferences](../SettingUpAaps/Preferences.md#status-lights).
* אם רמת החיישן זהה לרמת הסוללה של הטלפון, כנראה שגרסת ה-xDrip+ ישנה מדי וצריכה עדכון.
   
   ![Sensor levels equals phone battery level](../images/Home2021_ActionSensorBat.png)

### פורטל הטיפולים - חלק O

* BG check, prime/fill, sensor insert and pump battery change are the base for the data displayed in [section N](#careportal---section-n).
* תיחול\מילוי מאפשר לתעד את החלפת מיקום חיבור צינורית המשאבה ואת החלפת מכל האינסולין.
* חלק O משקף את פורטל הטיפולים שבנייטסקאוט. לכן התעמלות, הכרזות ושאלות הן סוגים מיוחדים של הערות.

### כלים - חלק P

#### דפדפן היסטוריה

* מאפשר לדפדף בהיסטוריית השימוש ב-AAPS.

#### TDD - סה"כ מינון אינסולין יומי

* תצרוכת האינסולין הכללית (TDD=סיכום יומי של הבולוסים יחד עם המינונים הבזאליים)
* רופאים לפעמים רושמים, במיוחד למשתמשי משאבה חדשים, יחס מינונים בזאליים-מינוני בולוסים של 50:50. 
* לכן היחס מחושב כ-TDD/2 X TBB ( TBB מינון בזאלי כולל= סכום המינונים הבזאליים ביממה). 
* אחרים מעדיפים יחס של 32-37% מה-TDD ל-TBB. 
* לרוב כללי האצבע האלה תוקף מוגבל בפרקטיקה. הערה: הסוכרת שלכם עשויה להיות שונה!

![Histroy browser + TDD](../images/Home2021_Action_HB_TDD.png)

(Screenshots-insulin-profile))=

## פרופיל האינסולין

![פרופיל האינסולין](../images/Screenshot_insulin_profile.png)

* This shows the activity profile of the insulin you have chosen in [config builder](../SettingUpAaps/ConfigBuilder.md#insulin). 
* העקום הסגול מראה כמה אינסולין נשאר לאחר הזרקתו כשהוא דועך לאורך הזמן והעקום הכחול מראה כמה הוא פעיל.
* חשוב לשים לב לכך שלדעיכה יש זנב ארוך. 
* אם השתמשתם בעבר במשאבה, כנראה שהנחתם שדעיכת האינסולין לוקחת כ-3.5 שעות. 
* עם זאת, בשימוש בלופ, הזנב הארוך חשוב כיוון שהחישובים הרבה יותר מדויקים והכמויות הקטנות הללו בזנבות מסתכמות למספרים משמעותיים בחישובים הרקורסיבים של אלגוריתמים של AndroidAPS.

לדיון מפורט יותר על סוגי האינסולין השונים, פרופילי הפעילות שלהם ומדוע כל זה חשוב, אפשר לקרוא מאמר כאן על [הבנת עקומות החדשות של האינסולין הפעיל על סמך עקומות פעילות אקספוננציאליות](https://openaps.readthedocs.io/en/latest/docs/While%20You%20Wait%20For%20Gear/understanding-insulin-on-board-calculations.html#understanding-the-new-iob-curves-based-on-exponential-activity-curves)

ניתן גם לקרוא מאמר מצוין בבלוג על זה כאן: [מדוע אנחנו טועים באופן קבוע במשך פעולת האינסולין (DIA) ולמה זה חשוב…](https://www.diabettech.com/insulin/why-we-are-regularly-wrong-in-the-duration-of-insulin-action-dia-times-we-use-and-why-it-matters/)

ועוד כאן: [עקומות אינסולין אקספוננציאליות + Fiasp](https://seemycgm.com/2017/10/21/exponential-insulin-curves-fiasp/)

## סטטוס המשאבה

![סטטוס המשאבה](../images/Screenshot_PumpStatus.png)

* מידעים שונים על מצב המשאבה. המידע המוצג תלוי בדגם המשאבה.
* See [pumps page](../Getting-Started/CompatiblePumps.md) for details.

## פורטל הטיפולים

פורטל הטיפולים שיכפל את הפונקציות שנמצאות במסך נייטסקאוט תחת הסמל "+" המאפשר להוסיף הערות לרשומותיכם.

### סקירה של חישוב הפחמימות

![Review carb calculation on t tab](../images/Screenshots_TreatCalc.png)

* If you have used the [Bolus Wizard](#bolus-wizard) to calculate insulin dosage you can review this calculation later on ts tab.
* פשוט לחץ על קישור "חישוב" הירוק. (בהתאם למשאבה שבשימוש, אינסולין ופחמימות ניתנים להצגה בשורה אחת בטיפולים.)

(Screenshots-carb-correction)=

### תיקון פחמימות

![Treatment in 1 or 2 lines](../images/Treatment_1or2_lines.png)

ניתן להשתמש בלשונית הטיפולים כדי לתקן הזנת פחמימות שגויה (כלומר, הערכת יתר או חסר).

1. בדקו וזכרו את האינסולין והפחמימות הפעילים בפועל במסך הבית.
2. בהתאם למשאבה בלשונית הטיפולים פחמימות עשויות להיות מוצגות יחד עם אינסולין בשורה אחת או כערכים נפרדים (כלומר עם משאבת Dana RS).
3. Remove the entry with the faulty carb amount. (Latest versions have trashcan icon in treatments screen. Press the trashcan icon, select the lines to remove, and then press the trashcan icon again to finalize.)
4. ודאו שהפחמימות הוסרו בהצלחה על ידי בדיקה מחדש של הפחמימות הפעילות במסך הבית.
5. עשו את אותו הדבר עבור אינסולין פעיל אם יש רק שורה אחת בלשונית הטיפול כוללת פחמימות ואינסולין.
   
   -> אם פחמימות לא מוסרות כמתוכנן ואתם מוסיפים פחמימות נוספות כפי שהוסבר כאן (6.), הפחמימות הפעילות יהיו גבוהות מדי וזה עלול להוביל למתן אינסולין גבוה מדי.

6. הזינו את כמות הפחמימות הנכונה דרך כפתור הפחמימות במסך הבית והקפידו להגדיר את מועד האירוע הנכון.

7. אם יש רק שורה אחת בלשונית הטיפולים הכוללת פחמימות ואינסולין, יש להוסיף גם את כמות האינסולין. הקפידו להגדיר את מועד האירוע הנכון ולבדוק את האינסולין הפעיל במסך הבית לאחר אישור הרשומה החדשה.

## לולאה, AMA / SMB

* לשוניות אלה מציגות פרטים על חישובי האלגוריתם ומדוע AAPS פועל כפי שהוא פועל.
* החישובים מחושבים בכל פעם שהמערכת מקבלת קריאה חדשה מהחיישן.
* For more details see [APS section on config builder page](../SettingUpAaps/ConfigBuilder.md#aps).

## Profile

![Profile](../images/Screenshots_Profile.png)

* הפרופיל מכיל מידע על הגדרות הסוכרת האישיות שלכם:
   
   * DIA (משך פעילות האינסולין)
   * IC או I:C: יחס אינסולין לפחמימות
   * ISF: פקטור הרגישות לאינסולין (יחס התיקון)
   * מינון בזאלי
   * ערך מטרה: רמת הגלוקוז בדם שאליה AAPS שואף

(Screenshots-treatment)=

## טיפול

היסטוריה של הטיפולים הבאים:

* Bolus & carbs -> option to [remove entries](#carb-correction) to correct history
* [בולוס ממושך](ExtendedCarbs#extended-bolus-and-switch-to-open-loop---dana-and-insight-pump-only)
* מינון בזאלי זמני
* [ערך מטרה זמני](../DailyLifeWithAaps/TempTargets.md)
* [החלפת פרופיל](../DailyLifeWithAaps/ProfileSwitch-ProfilePercentage.md)
* Careportal - notes entered through action tab and notes in dialogues

## מקורות נתוני סוכר - xDrip+, BYODA...

![BG Source tab - here xDrip](../images/Screenshots_BGSource.png)

* שמה של לשונית זו הוא בהתאם למקור נתוני הסוכר שהוגדר.
* מציג היסטוריה של קריאות של החיישן ומציע אפשרות להסיר קריאה במקרה של כשל (לדוגמה קריאת סוכר נמוך בגלל לחיצה על החיישן).

## NSClient

![NSClient](../images/Screenshots_NSClient.png)

* מציג את מצב החיבור עם אתר הנייטסקאוט שלכם.
* Settings are made in [preferences](../SettingUpAaps/Preferences.md#nsclient). אפשר לפתוח את החלק המתאים על ידי לחיצה על גלגל השיניים בצד השמאלי העליון של המסך.
* For troubleshooting see this [page](../GettingHelp/TroubleshootingNsClient.md).