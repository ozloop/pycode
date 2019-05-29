

#         ##next page
#         response.css('a.next::attr(href)').extract_first()
#         '/c101010100/?page=2'
# https://www.zhipin.com/c101010100/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&page=2&ka=page-next



#         #查询也
#         https://www.zhipin.com/c101010100/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&ka=sel-city-101010100

#         查询页拿到详情页
#         response.css('div.info-primary a[data-itemid]::attr(href)').extract()
#         '/job_detail/0a2e33499cffffe01XR83Nq0ElI~.html',

response.css('div.job-detail h2.name::text').extract()[0]
#         #详情页
#         https://www.zhipin.com/job_detail/8c979ebb0d57c7fb1XB-3N6-F1c~.html

姓名
response.css('div.job-detail h2.name::text').extract()[0]
薪资
response.css('span.salary::text').extract()[0]
职位描述
response.css('div.job-sec div.text').extract()[0]
公司介绍
response.css('div.job-sec.company-info div.text::text').extract()[0]
