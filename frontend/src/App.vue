<template>
  <div id="app" class="container">
    <div class="center">
    <!-- 头部导航 -->
      <header class="header">
        <link rel="shortcut icon" href="/assets/favicon.ico">
        <el-row>
          <el-col :span="24">
            <el-menu default-active="5" class="el-menu-demo" mode="horizontal" @select="">
              <el-menu-item index="1"><router-link to="/">收养</router-link></el-menu-item>
              <el-menu-item index="2"><router-link to="/send">送养</router-link></el-menu-item>
              <el-menu-item index="3"><router-link to="/rescue">救助</router-link></el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </header>
      <div style="position: relative;height: 60px;width: 100%;"></div>

      <main>
        <!-- 右侧主内容区 -->
        <div  class="main-right" >
          <h1>Pethub! 宠物收养救助小站</h1>
          <router-view></router-view>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {

  },
  data(){

  }
}

</script>

<style scoped>

</style>

