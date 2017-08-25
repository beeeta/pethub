
import send from './page/send/send.vue'
import rescue from './page/rescue/rescue.vue'
import send_add from './page/send/send-add.vue'
import rescue_addReply from './page/rescue/rescue-addReply.vue'
import user_info from './page/auth/userinfo.vue'
import user_login from './page/auth/login.vue'
import user_register from './page/auth/register.vue'


export default [
  {
    path:'/',component:send,children:
    [{
      path:'/send/add',component:send_add,
    }]
  },
  {
    path:'/rescue',component:rescue,children:
    [{
      path:'/rescue/addReply',component:rescue_addReply,
    }]
  },
  {
    path:'/auth',component:user_info
  },
  {
    path:'/auth/login',component:user_login
  },
  {
    path:'/auth/register',component:user_register
  },
]
