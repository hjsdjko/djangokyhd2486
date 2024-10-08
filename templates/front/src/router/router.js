import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import qiyeList from '../pages/qiye/list'
import qiyeDetail from '../pages/qiye/detail'
import qiyeAdd from '../pages/qiye/add'
import gerenjianliList from '../pages/gerenjianli/list'
import gerenjianliDetail from '../pages/gerenjianli/detail'
import gerenjianliAdd from '../pages/gerenjianli/add'
import zhiweileixingList from '../pages/zhiweileixing/list'
import zhiweileixingDetail from '../pages/zhiweileixing/detail'
import zhiweileixingAdd from '../pages/zhiweileixing/add'
import zhiweizhaopinList from '../pages/zhiweizhaopin/list'
import zhiweizhaopinDetail from '../pages/zhiweizhaopin/detail'
import zhiweizhaopinAdd from '../pages/zhiweizhaopin/add'
import mianshiyaoqingList from '../pages/mianshiyaoqing/list'
import mianshiyaoqingDetail from '../pages/mianshiyaoqing/detail'
import mianshiyaoqingAdd from '../pages/mianshiyaoqing/add'
import yingpinxinxiList from '../pages/yingpinxinxi/list'
import yingpinxinxiDetail from '../pages/yingpinxinxi/detail'
import yingpinxinxiAdd from '../pages/yingpinxinxi/add'
import mianshixinxiList from '../pages/mianshixinxi/list'
import mianshixinxiDetail from '../pages/mianshixinxi/detail'
import mianshixinxiAdd from '../pages/mianshixinxi/add'
import luyongjieguoList from '../pages/luyongjieguo/list'
import luyongjieguoDetail from '../pages/luyongjieguo/detail'
import luyongjieguoAdd from '../pages/luyongjieguo/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'qiye',
					component: qiyeList
				},
				{
					path: 'qiyeDetail',
					component: qiyeDetail
				},
				{
					path: 'qiyeAdd',
					component: qiyeAdd
				},
				{
					path: 'gerenjianli',
					component: gerenjianliList
				},
				{
					path: 'gerenjianliDetail',
					component: gerenjianliDetail
				},
				{
					path: 'gerenjianliAdd',
					component: gerenjianliAdd
				},
				{
					path: 'zhiweileixing',
					component: zhiweileixingList
				},
				{
					path: 'zhiweileixingDetail',
					component: zhiweileixingDetail
				},
				{
					path: 'zhiweileixingAdd',
					component: zhiweileixingAdd
				},
				{
					path: 'zhiweizhaopin',
					component: zhiweizhaopinList
				},
				{
					path: 'zhiweizhaopinDetail',
					component: zhiweizhaopinDetail
				},
				{
					path: 'zhiweizhaopinAdd',
					component: zhiweizhaopinAdd
				},
				{
					path: 'mianshiyaoqing',
					component: mianshiyaoqingList
				},
				{
					path: 'mianshiyaoqingDetail',
					component: mianshiyaoqingDetail
				},
				{
					path: 'mianshiyaoqingAdd',
					component: mianshiyaoqingAdd
				},
				{
					path: 'yingpinxinxi',
					component: yingpinxinxiList
				},
				{
					path: 'yingpinxinxiDetail',
					component: yingpinxinxiDetail
				},
				{
					path: 'yingpinxinxiAdd',
					component: yingpinxinxiAdd
				},
				{
					path: 'mianshixinxi',
					component: mianshixinxiList
				},
				{
					path: 'mianshixinxiDetail',
					component: mianshixinxiDetail
				},
				{
					path: 'mianshixinxiAdd',
					component: mianshixinxiAdd
				},
				{
					path: 'luyongjieguo',
					component: luyongjieguoList
				},
				{
					path: 'luyongjieguoDetail',
					component: luyongjieguoDetail
				},
				{
					path: 'luyongjieguoAdd',
					component: luyongjieguoAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
