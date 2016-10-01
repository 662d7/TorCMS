# -*- coding:utf-8 -*-


import config
from torcms.model.core_tab import g_Tag
from torcms.model.supertable_model import MSuperTable


class MCategory(MSuperTable):
    def __init__(self):
        self.tab = g_Tag
        try:
            g_Tag.create_table()
        except:
            pass

    def get_qian2(self, qian2, type = 2):
        '''
        用于首页。根据前两位，找到所有的大类与小类。
        并为方便使用，使用数组的形式返回。
        :param qian2: 分类id的前两位
        :return: 数组，包含了找到的分类
        '''
        return self.tab.select().where((self.tab.type == type) & (self.tab.uid.startswith(qian2)) ).order_by(self.tab.order)
    def query_pcat(self, type = 2):
        return  self.tab.select().where((self.tab.type == type) & (self.tab.uid.endswith('00'))).order_by(self.tab.order)
    def query_uid_starts_with(self, qian2, type =1 ):
        return self.tab.select().where( (self.tab.type == type) & self.tab.uid.startswith(qian2)).group_by(self.tab.uid).order_by(self.tab.order)

    def query_all(self, by_count=False, by_order=True, type = 1):
        if by_count:
            recs = self.tab.select().where(self.tab.type == type).order_by(self.tab.count.desc())
        elif by_order:
            recs = self.tab.select().where(self.tab.type == type).order_by(self.tab.order)
        else:
            recs = self.tab.select().where(self.tab.type == type).order_by(self.tab.uid)
        return (recs)

    def query_field_count(self, limit_num, type = 1):
        return self.tab.select().where(self.tab.type == type).order_by(self.tab.count.desc()).limit(limit_num)

    def get_by_slug(self, slug):
        uu = self.tab.select().where(self.tab.slug == slug)
        if uu.count() == 1:
            return uu.get()
        elif uu.count() > 1:
            return False
        else:
            return False

    def update_count(self, cat_id, num):
        entry = self.tab.update(
            count=num,
        ).where(self.tab.uid == cat_id)
        entry.execute()

    def initial_db(self, post_data):
        entry = self.tab.create(
            name=post_data['name'],
            id_cat=post_data['id_cat'],
            slug=post_data['slug'],
            order=post_data['order'],
        )
        return (entry)

    def update(self, uid, post_data):
        raw_rec = self.get_by_id(uid)
        entry = self.tab.update(
            name=post_data['name'] if 'name' in post_data else raw_rec.name,
            slug=post_data['slug'] if 'slug' in post_data else raw_rec.slug,
            order=post_data['order'] if 'order' in post_data else raw_rec.order,
            type = post_data['type'] if 'type' in post_data else raw_rec.type,
        ).where(self.tab.uid == uid)
        entry.execute()

    def insert_data(self, id_post, post_data):

        uu = self.get_by_id(id_post)
        if uu:
            self.update(id_post, post_data)
        else:
            entry = self.tab.create(
                name=post_data['name'],
                slug=post_data['slug'],
                order=post_data['order'],
                uid=id_post,
                type = post_data['type'] if 'type' in post_data else 1,
            )
            return (entry.uid)