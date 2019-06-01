import scrapy
import time
import re
class bossSpider(scrapy.Spider):
    name = 'bateq'
    filename='bateq0601.md'
    joins='@@'
    
    def start_requests(self): # 由此方法通过下面链接爬取页面
        print('>>>>>>>>.')
        baseUrl = 'http://batshoppe.dy.fi/eqinfo2.php'
        eq_classes = [
            # 'Any Slot',
            # 'Any Held',
            'Amulet',
            'Arm',
            'Arms',
            'Belt',
            'Bracelet',
            'Bracelets',
            'Cloak',
            'Feet',
            'Foot',
            'Hand',
            'Hands',
            'Head',
            'Held',
            'Leg',
            'Legs',
            'Neck',
            'Ring',
            'Rig',
            'Tail',
            'Torso',
            'Axe',
            'Bludgeon',
            'Longsword',
            'Shortsword',
            'Polearm',
            'Ranged',
            'Shield',
            'Multislot',
            'Relic'
        ]
        eq_classes_test = [
            'Bracelet'
        ]
        
        form_data = {
            'eqshort':'',
            'eq_classes':'Amulet',
            'res_name':'0',
            'skill_name':'0',
            'spell_name':'0',
            'ability_name':'0',
            'weightsel':'0',
            'sac_value':'0',
            'dam_type':'0',
            'compareclass':'0',
            'eq_type':'0',
            'material':'0',
            'racename':'Human',
            'eq_areas':'0',
            'andoror':'AND',
            'submit':'Submit'
        }
        for eq_class in eq_classes:
            self.log('start -------- %s' % eq_class)
            form_data['eq_classes'] = eq_class
            yield scrapy.FormRequest(url = baseUrl,
                formdata=form_data, callback=self.parse) 

    def parse(self, response):
        time.sleep(1)
        rows = response.css('#sf tr')
        rs=''
        time.sleep(0.7)
        for row in rows:
            # ## usful info
            cols = row.css('td::text').extract()
            ## eqname and area
            names = row.css('td a::text').extract()
            ## eqname and area， href
            hrefs=row.css('td a::attr(href)').extract()
            
            if len(cols) < 5:
                continue
            #处理装备名称，第三个是数字
            if re.match('^\d+$', cols[2], flags=0) :
                if len(names) > 0:
                    cols[0] = names[0] + cols[0]
                    names.pop(0)
            else:#第二个是数字
                if len(names) > 0:
                    cols.insert(0,names[0])
                    names.pop(0)
                else:
                    cols.insert(0,'noname')

            #处理area
            if len(cols) == 6:#差一个
                if len(names) > 0:
                    cols.append(names[0])
                else:
                    cols.append("noarea")
            elif len(cols) == 7:
                if len(names) > 0:
                    cols[6] += names[0]

            for c in cols:
                rs = rs + c + self.joins
            for h in hrefs:
                rs = rs + h + self.joins
            # for name
            rs+='结尾'
        # self.log("###### rs=%s" % rs)
        with open(self.filename, "a+") as f:  # 追加写入文件
            f.write(rs )
            f.close()  # 关闭文件操作
