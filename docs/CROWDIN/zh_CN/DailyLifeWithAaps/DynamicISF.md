(Open-APS-features-DynamicISF)=
# 动态胰岛素敏感系数（DynamicISF）
**Dynamic ISF** was added in **AAPS** version 3.2 and requires **[Objective 11](#objectives-objective11)** to be started before **Dynamic ISF** can be activated. Check **Enable dynamic sensitivity** in [Preferences > OpenAPS SMB](#Preferences-openaps-smb-settings) to activate. 该功能仅推荐给那些已经熟练掌握**AAPS**控制和监测的高级用户。

为了有效使用**动态ISF**，**AAPS'**数据库需要至少五（5）天的用户**AAPS**数据。

**动态ISF**根据用户的以下情况动态调整用户的胰岛素敏感系数（**ISF**）：

- 每日胰岛素总剂量（TDD）；
- 当前和预测的血糖值。

**动态ISF**使用Chris Wilson的模型来确定**ISF**，而不是用户静态**配置文件**中设置的**ISF**值。

The **Dynamic ISF** equation implemented is: `ISF = 1800 / (TDD * Ln (( glucose / insulin divisor) +1 ))`

SMB/AMA——示例显示了用户**配置文件**中由用户设置的静态**ISF**，并由SMB和AMA使用。

![静态ISF](../images/DynISF1.png)

动态ISF - 用户**ISF**根据**动态ISF**的判定而发生变化的一个示例。

![动态ISF](../images/DynISF2.png)

The section circled in red shows: <br/> Alg:`DynamicISF value (based on TDD)`<br/> `profile ISF` -> `ISF as calculated by DynISF (used in SMB algorithm)` (`ISF used for COB calculations and bolus wizard`)

实施中使用了上述公式来计算当前**ISF**，并在oref1预测中用于**IOB**（活性胰岛素）、**ZT**（零临时胰岛素）和**UAM**（未宣布餐时）的计算。 It is also used for **COB** and in the bolus wizard. Further discussion can be found here: [Chris Wilson on Insulin Sensitivity (Correction Factor) with Loop and Learn, 2/6/2022](https://www.youtube.com/watch?v=oL49FhOts3c).

## 总日剂量（TDD）
TDD将使用以下值的组合：
1.  7天平均**TDD**；
2.  前一天的**TDD**；
3.  过去八小时胰岛素使用量的加权平均值，并推算出24小时的值。

上述公式中使用的**TDD**是上述三个值各占三分之一的加权值。

## 胰岛素除数
胰岛素除数取决于所使用的胰岛素的峰值，并且与峰值时间成反比。 对于Lyumjev，此值为75；对于Fiasp，为65；对于常规速效胰岛素，为55。

## 未来ISF

未来**ISF**用于oref1做出的剂量决策中。  未来**ISF**使用与上面生成的相同的**TDD**值，并考虑调整因子（如上所述）。 然后，它根据不同的血糖值使用：

* 如果血糖水平平稳，在±3毫克/分升以内，且预测的**BG**高于目标值，则使用预测的最低**BG**的50%和当前**BG**的50%的组合。

* 如果最终**BG**高于目标值且血糖水平正在上升，或者最终**BG**高于当前**BG**，则使用当前**BG**。

否则，使用预测的最低**BG**。

## Preferences

Check **Enable dynamic sensitivity** in [Preferences > OpenAPS SMB](#Preferences-openaps-smb-settings) to activate. New settings become available once checked.

![Dynamic ISF settings](../images/Pref2020_DynISF.png)

### 动态ISF调整因子
调整因子允许用户指定1%至300%之间的值。 这作为**TDD**值的乘数，并且当值增加到100%以上时，**ISF**值会变小（即需要更多胰岛素才能使血糖水平小幅移动）；当值降低到100%以下时，<0>ISF</0>值会变大（即需要更少胰岛素才能使血糖水平小幅移动）。

### BG level below which low glucose suspend occurs

BG value below which insulin is suspended. Default value uses standard target model. User can set value between 60mg/dl (3.3mmol/l) and 100mg/dl(5.5mmol/l). Values below 65/3.6 result in use of default model.

### 启用基于TDD的敏感性比率以调整基础率和血糖目标

此设置替换了Autosens，并使用过去24小时**TDD**与7天**TDD**的比率作为基础来增加或减少基础率，这与标准Autosens的方式相同。 如果启用了根据敏感性调整目标的选项，则此计算值也用于调整目标。 与Autosens不同，此选项不会调整**ISF**值。

## 警告 - 自动化或档案百分比增加
使用自动化工具时应始终谨慎。 在使用**动态ISF**时尤其如此。

如果**动态ISF**正在运行，用户应重新考虑是否启用任何作为自动化规则的临时**配置文件**增加，或类似地激活可能使**动态ISF**在校正注射时过于激进并可能导致低血糖的**配置文件百分比**。
