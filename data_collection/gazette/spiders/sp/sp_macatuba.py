from gazette.spiders.base.sigpub import SigpubGazetteSpider


class SpMacatubaSpider(SigpubGazetteSpider):
    name = "sp_macatuba"
    TERRITORY_ID = "3528007"
    CALENDAR_URL = "https://www.diariomunicipal.com.br/macatuba"
