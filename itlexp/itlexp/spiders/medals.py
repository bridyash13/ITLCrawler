import scrapy 
from ..items import ItlexpItem

class QuoteSpider(scrapy.Spider):
    name = "medals"
    start_urls = [
        'https://olympics.com/en/olympic-games/tokyo-2020/medals'
    ]

    def parse(self,response):

        items = ItlexpItem()

        table = {}
    
        countries = response.css("span.styles__CountryName-sc-fehzzg-6::text").extract()
        gold = []
        silver = []
        bronze = []
        total = []

        l = int(len(countries))

        for i in range(1,l+1):
            gold.append(response.xpath('//div[@data-medal-id="gold-medals-row-'+ str(i) +'"]/span/text()').get())
            silver.append(response.xpath('//div[@data-medal-id="silver-medals-row-'+ str(i) +'"]/span/text()').get())
            bronze.append(response.xpath('//div[@data-medal-id="bronze-medals-row-'+ str(i) +'"]/span/text()').get())
            total.append(response.xpath('//div[@data-medal-id="total-medals-row-'+ str(i) +'"]/span/text()').get())
        
        l = []
        for i in range(len(countries)):
            l = []
            l.append(gold[i])
            l.append(silver[i])
            l.append(bronze[i])
            l.append(total[i])
            table[str(countries[i])] = l
        
        for i in sorted(table.keys()):
            items['Country'] = str(i)
            items['Gold'] = table[i][0]
            items['Silver'] = table[i][1]
            items['Bronze'] = table[i][2]
            items['Total'] = table[i][3]
            yield items