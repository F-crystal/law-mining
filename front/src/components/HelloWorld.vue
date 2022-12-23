<template>
<el-container>
  <!--
  <el-header>法律文书写作辅助系统</el-header>
   -->
  <el-container>
    <el-aside width="200px">    
      <el-menu 
      router
      :default-active="this.$route.path" 
      class="el-menu-demo" 
      @select="handleSelect"
      style="min-height: 100vh">
      <el-menu-item index="/">首页</el-menu-item>
      <el-menu-item index="/corrector">文书纠错</el-menu-item>
      <el-menu-item index="/test">相似案例识别</el-menu-item>   
    </el-menu>
  </el-aside>
    <el-main>
            首页
    </el-main>
  </el-container>
</el-container>
</template>

<style>
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
    caret-color: #d20a0a;
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


</style>

<script>
  export default {
    data() {
      const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      };
      return {
        tableData: Array(20).fill(item)
      }
    }
  };
</script>