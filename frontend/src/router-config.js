
import adoption from './page/adoption/adoption.vue'
import send from './page/send/send.vue'
import rescue from './page/rescue/rescue.vue'
import send_add from './page/send/send-add.vue'

export default [
  {
    path:'/',component:adoption,
  },
  {
    path:'/send',component:send,children:
    [{
      path:'/send/add',component:send_add,
    }]
  },
  {
    path:'/rescue',component:rescue,
  }
]
