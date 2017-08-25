<template>
  <div id="app" class="container">
    <!-- 头部导航 -->
      <header class="header">
        <link rel="shortcut icon" href="/assets/favicon.ico">
        <div  class="main-right" >
          <h1>Pethub! 宠物收养救助小站</h1>
        </div>
        <el-row>
          <el-col :span="24">
            <el-menu default-active="5" class="el-menu-demo" mode="horizontal" @select="">
              <el-menu-item index="1"><router-link to="/">收养&送养</router-link></el-menu-item>
              <el-menu-item index="2"><router-link to="/rescue">救助</router-link></el-menu-item>
              <el-menu-item index="3" style="float:right" v-show="logined_flag"><router-link to="/auth/userinfo">用户信息</router-link></el-menu-item>
              <el-menu-item index="5" style="float:right" v-show="! logined_flag"><router-link to="/auth/register">注册</router-link></el-menu-item>
              <el-menu-item index="4" style="float:right" v-show="! logined_flag"><router-link to="/auth/login">登录</router-link></el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </header>
      <div style="position: relative;height: 60px;width: 100%;"></div>
      <main>
        <!-- 右侧主内容区 -->
        <router-view></router-view>
      </main>
    </div>
</template>

<script>
export default {
  name: 'app',
  components: {

  },
  data(){
      return{
        logined_flag:false
      }
  },
  created:function () {
    var vue = this
    $.ajax({
      url: "/auth/checkLogin",
      type:'GET',
      dataType:'json',
      success:function(data){
        if(null==data){
          vue.logined_flag = false
        }else{
          vue.logined_flag = true
        }
      },
      error:function(){
        vue.logined_flag = false
        alert('server error')
      },
    })
  }
}

</script>

<style scoped>

</style>

