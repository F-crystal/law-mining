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
      <template>
<div>
  <!-- Two-way Data-Binding -->
  <quill-editor
      ref="myQuillEditor"
      v-model="content"
      :options="editorOption"
      @blur="onEditorBlur($event)"
      @focus="onEditorFocus($event)"
      @ready="onEditorReady($event)"
  />

</div>
</template>

</el-main>
</el-container>
</template>
 
<script>
export default {
  name: 'test' 
}

</script>

<script>
// require styles 导入富文本编辑器对应的样式
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import { quillEditor } from 'vue-quill-editor'
export default {
  components: {
    quillEditor
  }
}
</script>
<script>
export default {
  data () {
    return {
      content: '<h2>I am Example</h2>',
      editorOption: {
        // Some Quill options...
      }
    }
  },
  methods: {
    onEditorBlur(quill) {
      console.log('editor blur!', quill)
    },
    onEditorFocus(quill) {
      console.log('editor focus!', quill)
    },
    onEditorReady(quill) {
      console.log('editor ready!', quill)
    },
    onEditorChange({ quill, html, text }) {
      console.log('editor change!', quill, html, text)
      this.content = html
    }
  },
  computed: {
    editor() {
      return this.$refs.myQuillEditor.quill
    }
  },
  mounted() {
    console.log('this is current quill instance object', this.editor)
  }
}
</script>

 
 
<style scoped>


</style>