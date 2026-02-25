# Flight-Deal-Finder

A small Python utility that reads a destinations sheet, enriches it with IATA airport codes, and prepares the data for downstream flight‑deal workflows (e.g., price checks, alerts). It currently demonstrates the IATA code enrichment path using a FlightSearch service and a DataManager abstraction for your data source.

Loads destination rows (city, iataCode, lowestPrice, id).

For now, main.py uses a sample in‑memory payload (sheet_raw_data).

If any row is missing iataCode, it fetches the correct IATA code for that city via FlightSearch.get_iata_code() and populates the data.
Prints the enriched dataset; hooks are in place to persist back via DataManager.update_iata_code() (commented).

├─ main.py                # Entry point (IATA enrichment demo)
├─ data_manager.py        # Abstraction around your data source (e.g., Sheety/Sheets/DB)   
├─ flight_search.py       # IATA lookup & (later) fare search logic                        
├─ flight_data.py         # (later) Normalize API response into domain objects             
├─ notification_manager.py# (later) Email/SMS/Slack notifications                          
└─ .env                   # Environment variables (API keys, endpoints)
