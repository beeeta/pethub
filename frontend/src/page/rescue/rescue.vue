
<template>
  <div>

  </div>
</template>

<script>
export default {
    data(){
      return{
        helps:[
          { kind:'狗',city:'深圳',postTime:'2017-07-21',link:'vx:559'},
          { kind:'猫',city:'成都',postTime:'2016-08-21',link:'qq:55339'},
        ]
      }
    },
    methods:{
      deleteRow(index,data){
        alert(data);
      }
    }

}
</script>

<style>


</style>
