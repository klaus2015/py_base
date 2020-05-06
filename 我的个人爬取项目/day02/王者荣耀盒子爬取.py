import requests
import os


class WZRYSpider:
    def __init__(self):

        self.url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90001a&app_id=h9044j&game_id=7622&game_name' \
                   '=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.2.1&version_code=13021&cuid=19339AEAB8B9987F7D2F9695D0097A35&ovr=9&device=HUAWEI_MHA-AL00&net_type=1&client_id=uQvF8PFhyQVs%2BASWAOf8kA%3D%3D&info_ms=XunCelHf7H2BIG2N%2BCTKeA%3D%3D&info_ma=kdb1erQb4xgSLk2yHfEuXJWq%2FgbPvj14AgKVW55nXPg%3D&mno=0&info_la=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&info_ci=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&mcc=0&clientversion=13.0.2.1&bssid=uYYbQdYwMdNOLF5zbuVuHBb%2BkWdsrt4x%2Fft0dFALgAg%3D&os_level=28&os_id=8139a7bab2b45fd8&resolution=1080_1808&dpi=480&client_ip=192.168.1.101&pdunid=3HX0216B16004880 HTTP/1.1'
        self.headers = {
            "Accept-Charset": "UTF-8;",
            "Accept-Encoding": "gzip,deflate",
            "Content-type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; MHA-AL00 Build/HUAWEIMHA-AL00)",
            "Host": "gamehelper.gm825.com",
            "Connection": "Keep-Alive",
        }
        self.one_hero_link = 'http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}' \
                             '&channel_id=90001a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.2.1&version_code=13021&cuid=19339AEAB8B9987F7D2F9695D0097A35&ovr=9&device=HUAWEI_MHA-AL00&net_type=1&client_id=uQvF8PFhyQVs%2BASWAOf8kA%3D%3D&info_ms=XunCelHf7H2BIG2N%2BCTKeA%3D%3D&info_ma=kdb1erQb4xgSLk2yHfEuXJWq%2FgbPvj14AgKVW55nXPg%3D&mno=0&info_la=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&info_ci=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&mcc=0&clientversion=13.0.2.1&bssid=uYYbQdYwMdNOLF5zbuVuHBb%2BkWdsrt4x%2Fft0dFALgAg%3D&os_level=28&os_id=8139a7bab2b45fd8&resolution=1080_1808&dpi=480&client_ip=192.168.1.101&pdunid=3HX0216B16004880%20HTTP/1.1'
        self.equipment_link = 'http://gamehelper.gm825.com/wzry/equip/list?channel_id=90001a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.2.1&version_code=13021&cuid=19339AEAB8B9987F7D2F9695D0097A35&ovr=9&device=HUAWEI_MHA-AL00&net_type=1&client_id=uQvF8PFhyQVs%2BASWAOf8kA%3D%3D&info_ms=XunCelHf7H2BIG2N%2BCTKeA%3D%3D&info_ma=kdb1erQb4xgSLk2yHfEuXJWq%2FgbPvj14AgKVW55nXPg%3D&mno=0&info_la=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&info_ci=4XK2Eu6gxi1XlSg6rRvMPQ%3D%3D&mcc=0&clientversion=13.0.2.1&bssid=uYYbQdYwMdNOLF5zbuVuHBb%2BkWdsrt4x%2Fft0dFALgAg%3D&os_level=28&os_id=8139a7bab2b45fd8&resolution=1080_1808&dpi=480&client_ip=192.168.1.101&pdunid=3HX0216B16004880 HTTP/1.1'
        self.hero_id = []
        # [{'纯肉': ['64', '74']},{'纯肉': ['64', '74']}]
        # ['纯肉':{['64', '74']},'纯肉1': {['64', '74']}]
        # name_id:[title:['64', '74'],title:['64', '74']]
        self.hero_equip = []
        # {"64":"大剑","65":"剑"}
        self.equip_list = {}

    def save_image(self):
        """
        保存英雄头像图片
        :return:
        """
        html = self.get_html(self.url)
        hero_list = html['list']
        directory = '/home/tarena/image/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        for hero in hero_list:
            name = hero['name']
            link = hero['cover']
            self.hero_id.append(hero['hero_id'])
            print(hero['hero_id'])
            h = requests.get(url=link).content
            filename = directory + name + link[-4:]
            with open(filename, 'wb') as f:
                f.write(h)

    def get_html(self, url):
        """

        :param url:
        :return:
        """
        html = requests.get(url=url, headers=self.headers).json()
        return html

    def show_one_hero_detial(self):
        for id in self.hero_id:
            url = self.one_hero_link.format(id)
            html = self.get_html(url)
            name = html['info']['name']
            equip_choice = html['info']['equip_choice']
            for type in equip_choice:
                title = type['title']
                equip_id = []
                equip_id_list = type['list']
                for item in equip_id_list:
                    equip_id.append(self.equip_list[item['equip_id']])

                self.hero_equip.append({name + '-' + title: equip_id})

    def get_equip_id(self):
        html = self.get_html(self.equipment_link)
        equip_list = html['list']
        for equip in equip_list:
            equip_name = equip['name']
            equip_id = equip['equip_id']
            # {"64":"大剑"}
            one_equip = {equip_id: equip_name}
            self.equip_list[equip_id] = equip_name

    def show_detial(self):
        self.save_image()
        self.show_one_hero_detial()
        self.get_equip_id()
        for item in self.hero_equip:
            for i in item.values():
                for s in i:
                    a = self.equip_list[s]
                    print(item.key,a)



if __name__ == "__main__":
    w = WZRYSpider()
    w.show_detial()

