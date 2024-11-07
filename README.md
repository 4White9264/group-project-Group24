# Developer：Qilong Yun 23067693G

Section_D_GoogleScholar_spider.py uses the scholarly third-party library scholarly-python-package, which introduces the following bugs that have not yet been fixed. Please use it with caution.
https://github.com/scholarly-python-package/scholarly/blob/main/README.md

In Section_D_GoogleScholar_spider.py, if multiple author information is queried in a loop, a StopIteration error will occur. This issue cannot be fixed at the moment, so only the first author's information can be retrieved.

In Section_D_GoogleScholar_spider.py, since the arxiv_api cannot return the author's university information, if authors have the same name, the information may be retrieved incorrectly. It is necessary to replace arxiv with another academic database. However, APIs from Elsevier, ResearchGate, IEEE, Scrape, Semantic Scholar, etc., require applications that can take up to two weeks for approval, so this cannot be fixed at this time.

Due to the use of the scholarly library in Section_D_GoogleScholar_spider.py, it will scrape data from Google Scholar, which may result in a 403 error when accessing the Google Scholar website from the same IP. Please use it with caution. This limitation can be addressed by modifying the proxy settings, as referenced here: https://scholarly.readthedocs.io/en/stable/quickstart.html#using-proxies
