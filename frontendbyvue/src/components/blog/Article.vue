<template>
  <div class="article-wrapper">
    <div class="article-header">
      <h1 class="article-title">文章标题</h1>
      <div class="article-info">
        <span><i class="iconfont">&#xe789;</i>标签.</span>
        <span><i class="iconfont">&#xe673;</i>作者.</span>
        <span><i class="iconfont">&#xe61e;</i>时间.</span>
        <span><i class="iconfont">&#xe638;</i>评论.</span>
        <span><i class="iconfont">&#xe65e;</i>评论.</span>
      </div>
    </div>
    <div class="article-content">
      <p>文章摘要阿士大夫撒发送到发我的饭按时发斯蒂芬
      啊发顺丰沙发舒服撒地方阿士大夫撒爱是人生ERASBASRAWR AFASDF DFAT阿三哥阿斯顿发阿发</p>
    </div>
    <div class="article-view">
      继续阅读
    </div>
    <div v-for="item of list" :key="item.pk">
      {{item.fields.title}}
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Article',
  data () {
    return {
      list: []
    }
  },
  methods: {
    getArticles () {
      axios.get('/api/blog/show_post')
        .then(this.getArticlesSucc)
    },
    getArticlesSucc (res) {
      console.log(1)
      let content = res.data
      let eff = content.eff
      console.log(eff)
    }
  },
  mounted () {
    this.getArticles()
  }
}
</script>
<style lang="stylus" scoped>
  .article-wrapper
    margin: 10px
    padding: 16px
    background-color: $bgColor
  .article-title
    margin: 10px 0px
    text-align:center
    font-size: 20px
    color: $content
  .article-info
    // font-size: 13px
    margin-bottom: 20px
  .article-content
    font-size: 16px
    color: $content
  .article-view
    font-size: 18px
    margin: 10px  0px
</style>
