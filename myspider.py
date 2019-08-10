import scrapy
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.amazon.co.uk/s?k=Ailun&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=amazon&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=amazonbasics&i=electronics&ref=nb_sb_noss'
                  'https://www.amazon.co.uk/s?k=amFilm&i=specialty-aps&srs=1624982031&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=Anker&i=computers&ref=nb_sb_noss'
                  'https://www.amazon.co.uk/s?k=apple&i=computers&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=arlo&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=beam+electronics&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=bic&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=Cambridge+Soundworks&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=Energizer&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=Fujifilm&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=Glad&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=Hammermill&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=HP&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=HP+Paper&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=iBUYPOWER&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=iottie&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=JEtech&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=jsaux&i=electronics&crid=IP401KC4BP&sprefix=JSAU%2Celectronics%2C565&ref=nb_sb_ss_i_3_4',
                  'https://www.amazon.co.uk/s?k=matein&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=maxboost&i=electronics&ref=nb_sb_noss_1',
                  'https://www.amazon.co.uk/s?k=mead&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=microsoft&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=mkeke&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=mpow&i=electronics&ref=nb_sb_noss_1',
                  'https://www.amazon.co.uk/s?k=mr.shield&i=electronics&crid=1BW48J1RS8B4K&sprefix=mR.SH%2Celectronics%2C457&ref=nb_sb_ss_fb_1_5',
                  'https://www.amazon.co.uk/s?k=NETGEAR&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=NETGEAR&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=post-it&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=purity&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=roku&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=sabrent&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=samsung&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=sandisk&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=Scotch+brand&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=Sparin&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=Steren&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=takaki&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=tepoinn&ref=nb_sb_noss_1',
                  'https://www.amazon.co.uk/s?k=tozo&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=TP-Link&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=trianium&i=electronics&crid=2X17HI0ILNSCQ&sprefix=trian%2Celectronics%2C566&ref=nb_sb_ss_i_1_5',
                  'https://www.amazon.co.uk/s?k=victsing&i=electronics&ref=nb_sb_noss_2',
                  'https://www.amazon.co.uk/s?k=videosecu&i=electronics&ref=nb_sb_noss_1',
                  'https://www.amazon.co.uk/s?k=wyze+labs&i=electronics&ref=nb_sb_noss_1',
                  'https://www.amazon.co.uk/s?k=XDesign&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=Xiaomi&i=electronics&ref=nb_sb_noss',
                  'https://www.amazon.co.uk/s?k=yootech&i=electronics&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        for title in response.css('span.a-size-medium'):
            yield {'title': title.css('span ::text').extract_first()}

        for next_page in response.css('.a-last a'):
            yield response.follow(next_page, self.parse)