



## eqname and area
response.css('#sf tbody tr')[1].css('td a::text').extract()

Out[45]: ['A black arm protector inlaid with rubies', 'Tunnels of the Undying']

## eq href, area href
In [46]: response.css('#sf tbody tr')[1].css('td a::attr(href)').extract()
Out[46]:
['http://taikajuoma.ovh/wiki/A_black_arm_protector_inlaid_with_rubies',
 'http://batshoppe.dy.fi/areainfo.php?areainfoid=236']


## 原始信息
 response.css('#sf tbody tr')[1].css('td::text').extract()
Out[50]:
[' [Parry version]', ## 这个要与eq name拼接
 '5% ruby, 10% fur, 85% leather',
 '49100',
 '0.570',
 'kote',
 '\n+3% parry']