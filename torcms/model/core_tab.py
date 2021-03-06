# -*- coding:utf-8 -*-

import peewee
from playhouse.postgres_ext import BinaryJSONField
from torcms.core.base_model import BaseModel


class g_Tag(BaseModel):
    uid = peewee.CharField(null=False, max_length=4, index=True, unique=True, primary_key=True, help_text='', )
    slug = peewee.CharField(null=False, index=True, unique=True, max_length=36, help_text='', )
    name = peewee.CharField(null=False, max_length=255, help_text='', )
    order = peewee.IntegerField()
    count = peewee.IntegerField(default=0)
    kind = peewee.CharField(null=False, max_length=2, default='11',
                            help_text='tag type: 0 for category, 1 for label', )
    role_mask = peewee.CharField(null=False, default='00100', help_text='Member Privilege')


class g_Link(BaseModel):
    uid = peewee.CharField(null=False, index=False, unique=True, primary_key=True, default='0000',
                           max_length=4, help_text='', )
    link = peewee.CharField(null=False, max_length=36, help_text='', )
    name = peewee.CharField(null=False, max_length=255, help_text='', )
    logo = peewee.CharField(null=False, max_length=255, help_text='', )
    order = peewee.IntegerField()


class g_Post(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, default='00000',
                           max_length=5, help_text='', )
    title = peewee.CharField(null=False, help_text='Title')
    keywords = peewee.CharField(null=False, default='', help_text='Keywords')
    date = peewee.DateTimeField(null=False, help_text='')
    time_create = peewee.IntegerField()
    user_name = peewee.CharField(null=False, default='', max_length=36, help_text='UserName', )
    time_update = peewee.IntegerField()
    view_count = peewee.IntegerField()
    logo = peewee.CharField(default='')
    valid = peewee.IntegerField(null=False, default=1, help_text='Whether the infor would show.')
    cnt_md = peewee.TextField()
    cnt_html = peewee.TextField()
    kind = peewee.CharField(null=False, max_length=1, default='1', help_text='Post type: 1 for doc, 2 for inor', )
    extinfo = BinaryJSONField(default={})


class g_Wiki(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    title = peewee.CharField(null=False, unique=True, index=True, help_text='Title')
    date = peewee.DateTimeField()
    time_create = peewee.IntegerField()
    user_name = peewee.CharField(null=False, max_length=36, help_text='UserName', )
    time_update = peewee.IntegerField()
    view_count = peewee.IntegerField()
    cnt_md = peewee.TextField()
    cnt_html = peewee.TextField()
    kind = peewee.CharField(null=False, max_length=1, default='1', help_text='1 for wiki, 2 for page.', )


class g_PostHist(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, help_text='', primary_key=True, max_length=36)
    title = peewee.CharField(null=False, max_length=255, help_text='', )
    post_id = peewee.CharField(null=False, max_length=5, help_text='', )
    user_name = peewee.CharField()
    cnt_md = peewee.TextField()
    time_update = peewee.IntegerField()
    logo = peewee.CharField()


class g_WikiHist(BaseModel):
    uid = peewee.CharField(null=False,
                           index=True,
                           unique=True,
                           help_text='',
                           primary_key=True,
                           max_length=36)
    title = peewee.CharField(null=False,
                             max_length=255,
                             help_text='', )
    wiki_id = peewee.CharField(null=False,
                               max_length=8,
                               help_text='', )
    user_name = peewee.CharField()
    cnt_md = peewee.TextField()
    time_update = peewee.IntegerField()


class g_Member(BaseModel):
    '''
    privilege:
    11111
    read,add,edit,delete,manage
    [0]: read
    [1]: for post, page, wiki,
    [2]: for infor.
    [3]: keep
    [4]: keep
    And, could be extended.
    '''
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    user_name = peewee.CharField(null=False, index=True, unique=True, max_length=16, help_text='User Name', )
    user_email = peewee.CharField(null=False, unique=True, max_length=255, help_text='User Email', )
    user_pass = peewee.CharField(null=False, max_length=255, help_text='User Password')
    role = peewee.CharField(null=False, default='10000', help_text='Member Privilege', )
    time_reset_passwd = peewee.IntegerField(null=False, default=0)
    time_login = peewee.IntegerField(null=False, default=0)
    time_create = peewee.IntegerField(null=False, default=0)
    time_update = peewee.IntegerField(null=False, default=0)
    time_email = peewee.IntegerField(null=False, default=0, help_text='Time auto send email.')


class g_Entity(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, )
    path = peewee.CharField(null=False, unique=True, max_length=255, help_text='', )
    time_create = peewee.IntegerField()
    kind = peewee.CharField(null=False,
                            max_length=1,
                            default='1',
                            help_text='1 for image', )


class g_Post2Tag(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    tag = peewee.ForeignKeyField(g_Tag, related_name='tag_id')
    post = peewee.ForeignKeyField(g_Post, related_name='post_id')
    order = peewee.IntegerField()


class g_Reply(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    create_user_id = peewee.ForeignKeyField(g_Member, related_name='reply_member_id')
    user_name = peewee.TextField()
    timestamp = peewee.IntegerField()
    date = peewee.DateTimeField()
    cnt_md = peewee.TextField()
    cnt_html = peewee.TextField()
    vote = peewee.IntegerField()


class g_Post2Reply(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    post = peewee.ForeignKeyField(g_Post, related_name='post_reply_id')
    reply = peewee.ForeignKeyField(g_Reply, related_name='reply_post_id')
    timestamp = peewee.IntegerField()


class g_Voter2Reply(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True, primary_key=True, max_length=36, help_text='', )
    reply = peewee.ForeignKeyField(g_Reply, related_name='reply_voter_id')
    voter = peewee.ForeignKeyField(g_Member, related_name='voter_reply_id')
    timestamp = peewee.IntegerField()


class g_Collect(BaseModel):
    '''
    用户收藏
    '''
    uid = peewee.CharField(max_length=36, null=False, unique=True, help_text='', primary_key=True)
    post = peewee.ForeignKeyField(g_Post, related_name='collect_info_rel')
    user = peewee.ForeignKeyField(g_Member, related_name='collect_user_rel')
    timestamp = peewee.IntegerField()


class g_Evaluation(BaseModel):
    '''
    用户评价
    '''
    uid = peewee.CharField(max_length=36, null=False, unique=True, help_text='', primary_key=True)
    post = peewee.ForeignKeyField(g_Post, related_name='evaluation_info_rel')
    user = peewee.ForeignKeyField(g_Member, related_name='evaluation_user_rel')
    value = peewee.IntegerField()  # 用户评价， 1 或 0, 作为计数


class g_Rating(BaseModel):
    '''
    Rating for App of each user.
    '''
    uid = peewee.CharField(max_length=36, null=False, unique=True, help_text='', primary_key=True)
    user = peewee.ForeignKeyField(g_Member, related_name='rating_user_rel')
    post = peewee.ForeignKeyField(g_Post, related_name='rating_info_rel')
    value = peewee.IntegerField(null=False)  # 用户评价， 1 或 0, 作为计数
    timestamp = peewee.IntegerField(null=False)


class g_Usage(BaseModel):
    uid = peewee.CharField(max_length=36, null=False, unique=True, help_text='', primary_key=True)
    post = peewee.ForeignKeyField(g_Post, related_name='info_id')
    user = peewee.ForeignKeyField(g_Member, related_name='user_id')
    count = peewee.IntegerField()
    tag = peewee.CharField(null=True)
    timestamp = peewee.IntegerField()


class g_Rel(BaseModel):
    '''
    相关应用
    我们认为，相关性，并非是对称操作
    '''
    uid = peewee.CharField(max_length=36, null=False, unique=True, help_text='', primary_key=True)
    post_f = peewee.ForeignKeyField(g_Post, related_name='rel_post_f')
    post_t = peewee.ForeignKeyField(g_Post, related_name='rel_post_t')
    count = peewee.IntegerField()
