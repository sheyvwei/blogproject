import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TestHeader from '@/common/TestHeader'
import login from '@/pages/login'
import Home from '@/pages/Home'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: '/testheader',
      name: 'testheader',
      component: TestHeader
    }, {
      path: '/login',
      name: 'login',
      component: login
    }, {
      path: '',
      name: 'Home',
      component: Home
    }
  ]
})
