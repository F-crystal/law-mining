<template>

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
  <div style="margin-top: 15px;">
    <el-input placeholder="请输入内容" v-model="words" class="input-with-select">
      <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
    </el-input>
  </div>
  <ul>
     <li v-for="(item) in list">{{item}}</li>
  </ul>
</el-main>
</el-container>
</template>

<script>
// require styles 导入富文本编辑器对应的样式
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

// import { quillEditor } from 'vue-quill-editor'

export default {
  data () {
    return {
      content: '<h2>I am Example</h2>',
      words: '', // 搜索内容
      list: [], // 展示内容
      editorOption: {
        // Some Quill options...
      }
    }
  },
  methods: {
    // 搜索事件
    search () {
       this.axios.post(`/word`,
         {words: this.words}).then((res) => {
         if (res.data.status === 'success') {
           this.list =  res.data.info
          } else {
           this.$message.error('搜索失败')
         }
         console.log(res)
       }).catch((error) => {
         this.$message.error(error)
       })
    }
  },
  computed: {
    editor () {
      return this.$refs.myQuillEditor.quill
    }
  },
  mounted () {
    console.log('this is current quill instance object', this.editor)
  }
}
</script>
<style scoped>
li{
  text-align: left;
}

</style>