# Data Schemas

Specifications for all references to regions, sectors and age groups
can be found in `enums.py`

## `company_size_and_turnover.csv`

* Sector: UK sector
* min_size: (0 to inf) lower bound of number of employees
* num_companies: (0 to inf) total number of companies in this sector with employee counts in the min_size bucket
* num_employees: (0 to inf) total number of employees in this sector for companies with employee counts in the min_size bucket
* per_turnover: (0 to 100) proportion of turnover share within the sector in percentage terms


## `credit_score.csv`

* Region: UK region
* mean: (-inf to inf) mean personal credit score per region
* stdev: (0 to inf) standard deviation of credit score per region

## `demand.csv`

* columns: UK sector
* rows: UK sector
* values: (0 to 1) demand contribution from row sector
  to column sector. All rows sum to 1.
 
## `earnings.csv`
 
* Region: UK region
* earnings: (0 to inf) median personal earnings per region

## `expenses.csv`

* Region: UK region
* expenses: (0 to inf): minimum personal expenses per region

## `expenses_full.csv`

* Region: UK region
* Sector: UK sector
* Decile: (one to nine): decile of personal income
* expenses: (0 to inf): personal expenses per region per sector per decile in normal times

## `gdp.csv`

* Region: UK Region
* Sector: UK Sector
* Age: Age banding
* gdp: (0 to inf) GDP per region, sector, age group


## `growth_rates.csv`

* Sector: UK Sector
* growth_rates: (0 to inf) historic peacetime growth rates per sector

## `input_output.csv`

* Sector: UK Sector
* employee_compensation: (0 to inf): mean employee compensation per sector
* taxes_minus_subsidies: (0 to inf): mean taxes minus subsidies per sector
* capital_consumption: (0 to inf): mean capital consumption per sector
* net_operating_surplus: (0 to inf): mean net operating surplus per sector

## `input_output_final.csv`

* Sector: UK Sector
* C: consumption
* K: capital formation
* E: exports

## `input_output_intermediate.csv`

* Columns: UK Sector
* Rows: UK Sector
* Values: (0 to inf): consumption of products of row sector by column sector

## `input_output_primary.csv`

* Sector: UK Sector
* IMPORTS: (-inf to inf)
* TAXES_PRODUCTS: (-inf to inf)
* COMPENSATION: (-inf to inf)
* TAXES_PRODUCTION: (-inf to inf)
* FIXED_CAPITAL_CONSUMPTION: (-inf to inf)
* IMPORTS: (-inf to inf)

## `keyworker.csv`

* Sector: UK Sector
* keyworker: (0 to 1): fraction workers per sector who still go to work and are unaffected by lockdown

## `largecap_count.csv`

* Sector: UK Sector
* largecap_count (0 to inf): number of large-cap companies per sector

## `largecap_pct_turnover.csv`

* Sector: UK Sector
* largecap_pct_turnover (0 to 1): fraction of turnover generated by large-cap corporations per sector

## `min_expenses_full.csv`

* Region: UK region
* Sector: UK sector
* Decile: (one to nine): decile of personal income
* expenses: (0 to inf): minimum personal expenses per region per sector per decile

## `populations.csv`

* region: UK Region
* columns: A0, A10, ..., A80 (10 year age bands)
* values: (0 to inf): population of each region by age group

## `smallcap_cash.csv`

* Sector: UK Sector
* smallcap_cash: (0 to inf): number of days of surplus cashflow of cash reserves per sector for small-cap corporations

## `sme_count.csv`

* Sector: UK Sector
* sme_count: (0 to inf): number of small and medium enterprises per sector

## `sme_rate_payer_vulnerability.csv`

* Sector: UK Sector
* vulnerability: (0 to 100): vulnerability factor (higher = more vulnerable) for sectors which pay rates, and hence will have a higher proportion of companies eligible for new spending government stimulus

## `supply.csv'`

* columns: UK sector
* rows: UK sector
* values: (0 to 1) supply contribution from row sector
  to column sector. All rows sum to 1.

## `vulnerability.csv`

* Sector: UK Sector
* vulnerability: (0 to 1): index representing maximum productivity of each sector under a lockdown situation

## `wages.csv`

* Sector: UK Sector
* Age: Lower bound of age band (see `src/adapter_covid19/enums.py` for definition)
* wages: (0 to inf): yearly income pre-tax per sector per age band

## `wfh.csv`

* Sector: UK Sector
* wfh: (0 to 1): productivity of each sector when working from home

## `workers.csv`

* Region: UK Region
* Sector: UK Sector
* Age: Age banding
* workers: (0 to inf) Number of workers per region, sector, age group