Spotreba energie podľa regiónov – Power BI Dashboard

Tento projekt prezentuje Power BI dashboard zameraný výhradne na regionálnu analýzu spotreby energie. Všetky vizualizácie porovnávajú spotrebu medzi regiónmi alebo zobrazujú vývoj spotreby v čase rozdelený podľa regiónov.

Projekt je vhodný ako portfóliová ukážka Power BI zručností vrátane práce s measures, vizualizáciami a analytickým myslením.

🎯 Ciele projektu

Porovnať celkovú spotrebu energie podľa regiónov

Identifikovať regióny s najvyšším počtom dní s vysokou spotrebou (High Usage Days)

Analyzovať časový trend spotreby energie pre jednotlivé regióny

Poskytnúť prehľadné a zrozumiteľné vizualizácie pre regionálne rozhodovanie

📊 Vizualizácie
1️⃣ Clustered Bar Chart – Total Consumption by Region

Graf porovnáva celkovú spotrebu energie medzi jednotlivými regiónmi a umožňuje rýchlo identifikovať regióny s najvyššou energetickou záťažou.

Y-axis: Region

X-axis: Total Consumption (measure)

Vizualizácia: Clustered Bar Chart

Analytický účel: Regionálne porovnanie spotreby

📌 Obrázok:
images/total_consumption_by_region.png

2️⃣ Clustered Bar Chart – High Usage Days by Region

Graf zobrazuje počet dní s vysokou spotrebou energie pre jednotlivé regióny, čím identifikuje regióny s častými špičkami spotreby.

Y-axis: Region

X-axis: High Usage Days (measure)

Vizualizácia: Clustered Bar Chart

Analytický účel: Identifikácia regionálnych rizík

📌 Obrázok:
images/high_usage_days_by_region.png

3️⃣ Line Chart – Energy Consumption Trend by Region

Line chart analyzuje vývoj spotreby energie v čase rozdelený podľa regiónov. Umožňuje porovnať trendy, sezónnosť a dlhodobý vývoj medzi regiónmi.

X-axis: Date

Y-axis: Total Consumption (measure)

Legend: Region

Vizualizácia: Line Chart

Analytický účel: Regionálna časová analýza

📌 Obrázok:
images/consumption_trend_by_region.png

⚙️ Použité nástroje a dáta

Power BI Desktop – tvorba dashboardu a dátového modelu

Dataset obsahuje:

region – región

date – dátum

consumption – spotreba energie (kWh)

Measures (DAX):

Total Consumption

High Usage Days

🔍 Hlavné výstupy dashboardu

Jasné porovnanie spotreby medzi regiónmi

Identifikácia regiónov s vysokou energetickou záťažou

Prehľadný pohľad na časový vývoj spotreby podľa regiónov

Podpora rozhodovania na regionálnej úrovni

📂 Štruktúra projektu
PowerBI-Dashboard/
│
├─ data/
│   └─ energy_consumption.csv
│
├─ images/
│   ├─ total_consumption_by_region.png
│   ├─ high_usage_days_by_region.png
│   └─ consumption_trend_by_region.png
│
├─ reports/
│   └─ Energy_Consumption.pbix
│
├─ reports_pdf/
│   └─ Energy_Consumption_Report.pdf
│
└─ README.md

🎤 Vysvetlenie projektu:

„Projekt je zameraný na regionálnu analýzu spotreby energie. Použil som clustered bar charty na porovnanie celkovej spotreby a počtu high usage dní podľa regiónov a line chart na sledovanie vývoja spotreby v čase pre jednotlivé regióny.“

🚀 Autor:

Tibor Pukluš,M.Sc.