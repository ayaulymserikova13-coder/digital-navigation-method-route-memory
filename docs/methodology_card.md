# Methodology Passport Card

## 1 Project Information

| Field | Information |
|---|---|
| Research title | The effect of digital navigation method on route memory in young people: a comparison of turn-by-turn directions and prior study of a digital map |
| Authors | Ayaulym Serikova; Gulnar Khabibullayeva |
| GitHub repository | https://github.com/khabibullayeva-gulnar/digital-navigation-method-route-memory |
                    | https://github.com/ayaulymserikova13-coder/digital-navigation-method-route-memory |

## 2 Research Type

Quantitative research. A preliminary randomized between-group experiment measures direction recall and landmark recognition after one traversal of an unfamiliar walking route. A structured questionnaire records the number of unfamiliar-route walking trips involving each navigation method during the past 30 days. Both components produce numerical data; no qualitative analysis is planned.

The planned sample is 20 young adult volunteers, randomly assigned to two groups of 10. This is a feasibility-based preliminary study. Pilot participants will not enter the main sample. No participant data have been collected.

## 3 Hypotheses

| Question | Null hypothesis H0 | Alternative hypothesis H1 |
|---|---|---|
| RQ1 Navigation habits | H01: The mean reported number of unfamiliar-route walking trips using TBT during the past 30 days equals the mean reported number using prior digital map study. | H11: The mean reported numbers of such trips differ between the two methods. |
| RQ2 Direction recall | H02: Mean direction recall accuracy after one traversal is equal between the TBT and Map Study groups. | H12: Mean direction recall accuracy after one traversal differs between the groups. |
| RQ3 Landmark recognition | H03: Mean landmark recognition accuracy after one traversal is equal between the TBT and Map Study groups. | H13: Mean landmark recognition accuracy after one traversal differs between the groups. |

RQ1 compares paired reports from the same participants. RQ2 and RQ3 compare independent groups on the same unfamiliar route. All alternative hypotheses are two-sided. RQ2 is the primary experimental question.

## 4 Variable Classification Matrix

The experimental factor is assigned navigation method. Questionnaire method use is measured rather than assigned. Participant characteristics are recorded, not treated as constants.

| Classification | Variable | Operational definition |
|---|---|---|
| Independent | Assigned navigation method | TBT directions during walking, or prior study of a digital map followed by walking without map access. |
| Dependent Primary | Direction recall accuracy (%) | Correct left/right/straight responses at five photograph-based decision points. |
| Dependent Secondary | Landmark recognition accuracy (%) | Correct classifications of ten photographs: five encountered objects and five new objects. |
| Measured factor RQ1 | Navigation method reported | Each participant reports both TBT and prior digital map study; neither is assigned for the questionnaire. |
| Measured outcome RQ1 | Navigation frequency | Number of unfamiliar-route walking trips involving each method in the past 30 days. |
| Controlled | Route and planned exposure | Same route, start, finish, direction and one planned traversal. Familiar volunteers are excluded before assignment. |
| Controlled | Navigation materials | Fixed route map, map orientation, and TBT wording. TBT does not name scored landmarks. |
| Controlled within condition | Assistance timing | Three minutes of map study in Map Study; standardized digital TBT delivery at predefined points in TBT. |
| Controlled | Testing | Same photographs, display settings, answer key, item order and scoring. Two-minute delay, then direction test followed by landmark test. |
| Controlled | Corrections | Standardized safety and correction protocol; wrong turns, unplanned aid and additional exposure are logged. |
| Controlled | Questionnaire | Same definitions, wording, 30-day period and counting unit. |
| Controlled Analysis | Processing | Same data schema, configuration, scoring code and fixed software versions. |

Age, map-reading experience and navigation habits are measured participant characteristics, not controlled constants. The proposed experimental settings will be checked in a pilot and finalized before main data collection.

## 5 Selected Metrics and Baseline

### Evaluation Metrics

Direction recall is primary because it answers RQ2, the main experimental question in Task 1. Landmark recognition answers RQ3 as a secondary outcome. Navigation frequency addresses RQ1 separately. The participant is the unit of analysis.

| Metric and role | Formula or measurement | Rationale |
|---|---|---|
| Direction recall accuracy (%) — Primary Metric | 100 × correct direction answers / 5 | Measures memory for the required route decisions. |
| Landmark recognition accuracy (%) — Secondary Metric | 100 × (correctly recognized encountered objects + correctly rejected new objects) / 10 | Measures recognition of route objects, including rejection of objects not encountered. |
| Navigation frequency RQ1 | Separate trip counts for both methods over 30 days | Describes habits and permits paired comparison. A trip using both methods counts toward both. |
| Mean accuracy difference — Comparative summary | Mean Map Study accuracy − mean TBT accuracy, in percentage points | Shows effect magnitude and direction separately for both memory outcomes. Positive values favor Map Study. |

Accuracy is calculated for each participant before averaging within groups. Presented but unanswered items score zero; technically incomplete tests are excluded from the corresponding outcome analysis. Missing questionnaire responses are not treated as zero; RQ1 uses participants with both frequency reports available.

### Guardrail Metrics

| Indicator | Threshold | Action |
|---|---|---|
| Eligibility and consent | 100% of enrolled volunteers have consent and report no route familiarity. | Do not enroll volunteers failing either requirement. |
| Unplanned navigation aid | 0 occurrences for a compliant traversal. | Record every occurrence. Keep assigned-group labels; flag deviations for sensitivity analysis. |
| Procedure-log completeness | 100% of completed sessions have required checklist fields, deviation status and response/missing codes. | Resolve gaps against source records; flag unresolved missingness. |
| Input validity | 0 invalid codes, duplicate records or missing answer-key entries before scoring. | Stop affected processing and resolve errors before calculation. |
| Safety and withdrawal | 0 continuations after withdrawal or identification of an unsafe condition. | Stop immediately and record the interruption. |

### Baseline and Comparison

TBT is the active reference condition: 10 participants receive standardized digital movement directions while walking. It provides a practical comparison in which assistance is available during navigation.

Map Study is the comparison condition: 10 participants study the route map for three minutes and then walk without further map access. The designation does not assume that either method performs better.

Participants will be randomly assigned using a documented computer-generated sequence with ten assignments per condition. Both groups complete the same unfamiliar route and memory tests. Corrections and additional route exposure will be recorded under a standardized protocol.

The comparison evaluates two complete navigation conditions, including presentation format and timing of assistance. It does not isolate these components or compare either method with unaided navigation. Findings from the small sample will be interpreted as preliminary.