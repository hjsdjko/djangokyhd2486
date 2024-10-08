#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    touxiang=Text
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class qiye(BaseModel):
    __doc__ = u'''qiye'''
    __tablename__ = 'qiye'

    __loginUser__='qiyezhanghao'


    __authTables__={'qiyezhanghao':'qiye',}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='qiyezhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='企业账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    qiyemingcheng=models.CharField ( max_length=255,null=False,unique=True, verbose_name='企业名称' )
    qiyedizhi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='企业地址' )
    qiyexingye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业行业' )
    farendaibiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='法人代表' )
    qiyeyouxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业邮箱' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    zhuceshijian=models.DateField   (  null=True, unique=False, verbose_name='注册时间' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    qiyezhanghao=VARCHAR
    mima=VARCHAR
    qiyemingcheng=VARCHAR
    qiyedizhi=VARCHAR
    qiyexingye=VARCHAR
    farendaibiao=VARCHAR
    qiyeyouxiang=VARCHAR
    lianxifangshi=VARCHAR
    zhuceshijian=Date
    qiyetupian=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qiye'
        verbose_name = verbose_name_plural = '企业'
class gerenjianli(BaseModel):
    __doc__ = u'''gerenjianli'''
    __tablename__ = 'gerenjianli'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    xueli=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历' )
    chushengriqi=models.DateField   (  null=True, unique=False, verbose_name='出生日期' )
    qiuzhiyixiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='求职意向' )
    yixiangzhiwei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='意向职位' )
    yixiangchengshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='意向城市' )
    xinziyaoqiu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='薪资要求' )
    jiaoyubeijing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教育背景' )
    huojiangzhengshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='获奖证书' )
    gongzuojingyan=models.TextField   (  null=True, unique=False, verbose_name='工作经验' )
    xiangmujingyan=models.TextField   (  null=True, unique=False, verbose_name='项目经验' )
    gerenjineng=models.TextField   (  null=True, unique=False, verbose_name='个人技能' )
    ziwopingjia=models.TextField   (  null=True, unique=False, verbose_name='自我评价' )
    jianliwenjian=models.TextField   (  null=True, unique=False, verbose_name='简历文件' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    touxiang=Text
    zhuanye=VARCHAR
    xueli=VARCHAR
    chushengriqi=Date
    qiuzhiyixiang=VARCHAR
    yixiangzhiwei=VARCHAR
    yixiangchengshi=VARCHAR
    xinziyaoqiu=VARCHAR
    jiaoyubeijing=VARCHAR
    huojiangzhengshu=VARCHAR
    gongzuojingyan=Text
    xiangmujingyan=Text
    gerenjineng=Text
    ziwopingjia=Text
    jianliwenjian=Text
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'gerenjianli'
        verbose_name = verbose_name_plural = '个人简历'
class zhiweileixing(BaseModel):
    __doc__ = u'''zhiweileixing'''
    __tablename__ = 'zhiweileixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweileixing=models.CharField ( max_length=255, null=True,unique=True, verbose_name='职位类型' )
    '''
    zhiweileixing=VARCHAR
    '''
    class Meta:
        db_table = 'zhiweileixing'
        verbose_name = verbose_name_plural = '职位类型'
class zhiweizhaopin(BaseModel):
    __doc__ = u'''zhiweizhaopin'''
    __tablename__ = 'zhiweizhaopin'



    __authTables__={'qiyezhanghao':'qiye',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    qiyedizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业地址' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    zhiweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位类型' )
    zhaopinrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='招聘人数' )
    xinzidaiyu=models.IntegerField  (  null=True, unique=False, verbose_name='薪资待遇' )
    xueliyaoqiu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历要求' )
    jingyanyaoqiu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='经验要求' )
    gongzuoshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作时间' )
    zhiweijieshao=models.TextField   (  null=True, unique=False, verbose_name='职位介绍' )
    fabushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发布时间' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    qiyedizhi=VARCHAR
    qiyetupian=Text
    zhiweileixing=VARCHAR
    zhaopinrenshu=Integer
    xinzidaiyu=Integer
    xueliyaoqiu=VARCHAR
    jingyanyaoqiu=VARCHAR
    gongzuoshijian=VARCHAR
    zhiweijieshao=Text
    fabushijian=DateTime
    clicktime=DateTime
    clicknum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'zhiweizhaopin'
        verbose_name = verbose_name_plural = '职位招聘'
class mianshiyaoqing(BaseModel):
    __doc__ = u'''mianshiyaoqing'''
    __tablename__ = 'mianshiyaoqing'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yaoqingbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='邀请编号' )
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='企业名称' )
    lianxifangshi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='联系方式' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    zhiweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位类型' )
    zhaopinrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='招聘人数' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘人' )
    mianshishijian=models.DateTimeField  ( null=False, unique=False, verbose_name='面试时间' )
    yaoqingbeizhu=models.TextField   ( null=False, unique=False, verbose_name='邀请备注' )
    tijiaoshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='提交时间' )
    '''
    yaoqingbianhao=VARCHAR
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxifangshi=VARCHAR
    qiyetupian=Text
    zhiweileixing=VARCHAR
    zhaopinrenshu=Integer
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    mianshishijian=DateTime
    yaoqingbeizhu=Text
    tijiaoshijian=DateTime
    '''
    class Meta:
        db_table = 'mianshiyaoqing'
        verbose_name = verbose_name_plural = '面试邀请'
class yingpinxinxi(BaseModel):
    __doc__ = u'''yingpinxinxi'''
    __tablename__ = 'yingpinxinxi'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    qiyedizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业地址' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    zhiweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘岗位' )
    yingpinshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='应聘时间' )
    gerenjingli=models.TextField   (  null=True, unique=False, verbose_name='个人经历' )
    gerenjianli=models.TextField   (  null=True, unique=False, verbose_name='个人简历' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘人' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    qiyedizhi=VARCHAR
    qiyetupian=Text
    zhiweileixing=VARCHAR
    yingpinshijian=DateTime
    gerenjingli=Text
    gerenjianli=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shouji=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'yingpinxinxi'
        verbose_name = verbose_name_plural = '应聘信息'
class mianshixinxi(BaseModel):
    __doc__ = u'''mianshixinxi'''
    __tablename__ = 'mianshixinxi'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    qiyedizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业地址' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    zhiweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='招聘岗位' )
    mianshishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='面试时间' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘人' )
    '''
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    qiyedizhi=VARCHAR
    qiyetupian=Text
    zhiweileixing=VARCHAR
    mianshishijian=DateTime
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    '''
    class Meta:
        db_table = 'mianshixinxi'
        verbose_name = verbose_name_plural = '面试信息'
class luyongjieguo(BaseModel):
    __doc__ = u'''luyongjieguo'''
    __tablename__ = 'luyongjieguo'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    qiyetupian=models.TextField   (  null=True, unique=False, verbose_name='企业图片' )
    luyongjieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='录用结果' )
    zhiweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='录用岗位' )
    fabushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发布时间' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='应聘人' )
    '''
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    qiyetupian=Text
    luyongjieguo=VARCHAR
    zhiweileixing=VARCHAR
    fabushijian=DateTime
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    '''
    class Meta:
        db_table = 'luyongjieguo'
        verbose_name = verbose_name_plural = '录用结果'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '公告信息分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class aboutus(BaseModel):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'aboutus'
        verbose_name = verbose_name_plural = '关于我们'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '系统简介'
