<template>
  <el-container>
    <el-aside width="200px">    
      <el-menu 
      router
      :default-active="this.$route.path" 
      class="el-menu-demo" 
      @select="handleSelect"
      style="min-height: 100vh;position: fixed;width: 200px;">
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/corrector">文书纠错</el-menu-item>
        <el-menu-item index="/test">相似案例识别</el-menu-item>   
      </el-menu>
    </el-aside>

  
<el-main>
  <div style="display:flex">
    <div class="split">
      <div style="display: flex;float: right;position: sticky;z-index: 202;">
        <el-button type="primary" plain v-on:click="getMessage()">纠错</el-button>
      </div>
      <div id="edit">
        <!--标题-->
        <input id="title" type="text" class="title" placeholder="在此键入标题..." maxlength="200" spellcheck="false">
        <!--正文-->
        <div id="content" class="editorComponent is-show-placeholder" spellcheck="false" contenteditable="true" data-placeholder="在此键入正文..." v-html="msg" @blur="msg=$event.target.innerText">
        </div>  
      </div>
    </div>

    <div id="result" class="split" style="background-color:#f7f9fc;">
      <el-card class="box-card" v-for="j in change.length" style="margin: 10px;" :id='"card"+(j-1)' :key="j">
              <span>{{change[j-1][0]}}</span>
              →
              <span>{{change[j-1][1]}}</span>
              <el-button class="button accept" text :id='"accept"+(j-1)' v-on:click="accept(j-1)">接受</el-button>
              <el-button class="button reject" text :id='"reject"+(j-1)' type="danger" plain v-on:click="reject(j-1)">拒绝</el-button>
      </el-card>
    </div>
  </div>


</el-main>
</el-container>
</template>

<script>
export default {
  name: 'corrector',
  data() {
    return{
      msg:'经本院审理查明：2014年4月20日，被告以生意资金周转为由向原告借款9万园',//初始设为''
      result:'',
      change:'',
    };
  },
  methods:{
    getMessage(){
      var param = {
          "sentence": this.msg.replace(/<.*?>/g,"")
                }
      this.axios
      .post("/", param)
      .then(
        res => {
            this.msg=this.msg.replace(/<.*?>/g,"")
            this.result = res.data.context
            this.change=res.data.change
            console.log(res.data.context)
            if(this.change.length>0){
              var nowx=0;
              var nowy=0;
              var add=0;
              var now=[];
              for (var i=0;i<this.change.length;i++){
                now=this.change[i]
                nowx=now[2];
                nowy=now[3];
                this.msg=this.insertStr(this.msg,nowx+add,"<span class='error' id=error"+i+">");
                add+=29+i.toString().length;
                this.msg=this.insertStr(this.msg,nowy+add,"</span>");
                add+=7
              }
              console.log(this.msg)
              console.log(this.msg.replace(/<.*?>/g,""))
            }
        }
      )
      .catch(res => {
        console.log(res)
        console.log("shiwo")
      });
    },

    insertStr(soure, start, newStr){   
      return soure.slice(0, start) + newStr + soure.slice(start);
    },
    accept(i){
      var text=document.getElementById('error'+i)//文章内文字
      var card=document.getElementById('card'+i)//右侧卡片
      text.className='accept'
      text.innerText=this.change[i][1]
      card.parentNode.removeChild(card);
      card
    },
    reject(i){
      var text=document.getElementById('error'+i)//文章内文字
      var card=document.getElementById('card'+i)//右侧卡片
      text.className='reject'
      card.parentNode.removeChild(card);
    }
  },

}
</script>
 
 
<style scoped>
 
</style>
<style>
  .el-main{
    padding: 0px;
    margin: 0px;
  }
  .split{
    width:50%;
    padding: 20px;
    margin: 0px;
  }
  .editorComponent:empty:before {
    content: attr(data-placeholder);
  }
  .editorComponent{
    padding-bottom: 15.625rem;
    margin: 0 auto;
    min-height: 100%;
    width: 100%;
    color: #2a2b2e;
    background: transparent;
    outline: none;
    white-space: pre-wrap;
    white-space: break-spaces;
    word-wrap: break-word;
    word-break: break-word;
    position: relative;
    caret-color: blue;
    text-align: left;
  }
  
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
  #title{
  overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-family: "Noto Serif SC",-apple-system,BlinkMacSystemFont,"Segoe UI","Roboto","Oxygen","Ubuntu","Cantarell","Fira Sans","Droid Sans","Helvetica Neue",sans-serif;
    width: 100%;
    font-size: 1.75rem;
    font-weight: 600;
    color: #2a2b2e;
    outline: none;
    background: none;
    border: 0;
    position: relative;
    margin: 0 0 1rem 0;
    vertical-align: middle;
  }
  .error{
    background: #fff2d9;
    border-bottom-color: #ffbe40;
    border-bottom-style: solid;
    cursor: pointer;
  }


</style>