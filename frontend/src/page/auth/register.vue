
<template>
  <div style="width:30%">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="电子邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="登录密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item label="昵称">
        <el-input v-model="form.username"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">创建</el-button>
        <el-button @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
    data(){
      return {
        form: {
          email: '',
          password: '',
          username: '',
        }
      }
    },
    methods:{
      onSubmit() {
        var vue = this
        $.ajax({
          url: "/auth/register",
          type:'POST',
          data:{user:vue.form},
          dataType:'json',
          success:function(data){
            // 获取分页数据，异步刷新
            alert(data)
          },
          error:function(){
            alert('server error')
          },
        })
      },
      cancel(){
        this.$router.push('/')
      }
    }
}
</script>


<style>


</style>
