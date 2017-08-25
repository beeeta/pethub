
<template>

  <div>
    <router-view></router-view>
    <el-row>
      <el-col :span="19" v-for="help in helps">
        <el-card :body-style="{ padding: '0px' }">
          <!--<img src="~examples/assets/images/hamburger.png" class="image">-->
          <div style="padding: 14px;">
            <span>{{help.content}}</span>
            <div class="bottom clearfix" :name="help.id">
              <el-button type="text" class="button" @click="showReplys">查看回复</el-button>
              <el-button type="text" class="button" @click="addRescueReplyVisible = true">回复</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog title="添加回复" :visible.sync="addRescueReplyVisible">
      <el-form :model="comment">
        <el-form-item label="" :label-width="formLabelWidth">
          <el-input v-model="comment.context" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitForm">确 定</el-button>
      </div>
    </el-dialog>

  </div>

</template>

<script>
export default {
    data(){
      return{
        helps:[
          { id:'h1',content:'深圳地铁旁边的带收养',replys:[{id:'a1',content:'啊，好可爱',user:{id:'u1'}},{id:'2',content:'我想领养',user:{id:'u11'}}]},
          { id:'h2',content:'宝安地铁一只流浪犬地铁旁边的带收养',replys:[{id:'b1',content:'我就在附近',user:{id:'u2'}},{id:'b2',content:'哈哈哈哈哈哈哈',user:{id:'u22'}}]},
        ],
        addRescueReplyVisible: false,
        comment:{
          context:'',
        }
      }
    },
    methods:{
        showReplys(event){
          var id = $(event.target).parent().parent().attr('name')
          $.ajax({
            url: "/rescue/reply/",
            type:'GET',
            data:{id:id},
            dataType:'json',
            success:function(data){
              alert(data)
            },
            error:function(){
              alert('server error')
            }
          })
        },
      submitForm(){
          var vue = this;
          var content = $('form.el-form').find('input[type="text"]').val()
          $.ajax({
            url: "/rescue/add/",
            type:'POST',
            data:{content:content},
            dataType:'json',
            success:function(data){
              vue.addRescueReplyVisible = false
              // 获取分页数据，异步刷新
              alert(data)
            },
            error:function(){
              alert('server error')
            },
          })
      },
    }
}
</script>


<style>


</style>
