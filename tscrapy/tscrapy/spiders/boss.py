import scrapy
import time
import re

class bossSpider(scrapy.Spider):
    name = 'boss'

    jobDetailTag = 'job_detail'
    domain = 'https://www.zhipin.com'

    #机器学习
    # start_urls = ['https://www.zhipin.com/c101010100/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&ka=sel-city-101010100']

    #深度学习
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&ka=sel-city-101010100']

    def parse(self, response):
        time.sleep(0.4)
        '''
        1. 如果是查询页，则
            添加下一页地址
            抽取所有的详情页地址，添加
        2. 如果是详情页
            抽取信息
        '''
        if self.jobDetailTag in response.url:
            company = response.css('div.company-info a[ka="job-detail-company"]::attr(title)').extract()[0].strip()
            title=response.css('div.info-primary div.name h1::text').extract()[0]
            salary = response.css('span.salary::text').extract()[0]
            desc = ';'.join(response.css('div.job-sec div.text::text').extract())
            company_info = response.css('div.job-sec.company-info div.text::text').extract()[0]

            url = response.url.split('/')[-1]
            filename = company + '-' + title + '-' + salary + '-' + url
            filename = re.sub('[\/:*?"<>|]','-',filename)

            with open(filename, "a+") as f:  # 追加写入文件
                f.write(company + '@\n')
                f.write(salary + '@\n')
                f.write(desc + '@\n')
                f.write(company_info + '@\n')
                self.log('writing is>>>> %s' % filename)
                f.close()  # 关闭文件操作
        else:
            #找详情页
            detail_list=response.css('div.info-primary a[data-itemid]::attr(href)').extract()
            if detail_list is not None:
                for detail in detail_list:
                    self.log('找到详情页 %s' % detail)
                    yield scrapy.Request(self.domain + detail, callback=self.parse) 

            #找下一页
            page = response.css('a.next::attr(href)').extract_first()
            if page is not None:
                num = page.split('=')[-1]
                next_page = self.start_urls[0] + '&page=' + num
                self.log('found next %s' % next_page)
                yield scrapy.Request(next_page, callback=self.parse) 