# Web Scraping

- Scrape a Wikipedia page and record which passages need citations.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.

## Functions

- get_citations_needed_count(URL):
  - Input: URL
  - Output: Integer
  - Description: Counts the number of places a citation is needed
- get_citations_needed_report(URL):
  - Input: URL
  - Output: String
  - Description: Returns content requiring citation in string form