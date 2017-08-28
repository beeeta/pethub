import send from './page/send/send.vue'
import rescue from './page/rescue/rescue.vue'
import user_info from './page/auth/userinfo.vue'
import user_login from './page/auth/login.vue'
import user_register from './page/auth/register.vue'


export default [
  {
    path:'/',component:send,
  },
  {
    path:'/rescue',component:rescue,
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
