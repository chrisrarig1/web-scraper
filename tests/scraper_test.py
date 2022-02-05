from webscrapper.scraper import  get_citations_needed_count,get_citations_needed_report

def test_cit_count():
    URL = 'https://en.wikipedia.org/wiki/Beer'
    assert get_citations_needed_count(URL) == 1

def test_cit_not_count():
    URL = 'https://en.wikipedia.org/wiki/Beer'
    assert get_citations_needed_count(URL) != 5

def test_cit_string():
    URL = 'https://en.wikipedia.org/wiki/Beer'
    assert 'citation needed' in get_citations_needed_report(URL)

def test_cit_not_string():
    URL = 'https://en.wikipedia.org/wiki/Beer'
    actual = 'citation needed' in get_citations_needed_report(URL)
    expected = 'citation needed' not in get_citations_needed_report(URL)
    assert actual != expected