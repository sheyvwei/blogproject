<template>
  <div class="Index">
    <div class="wrapper-Index">
        <div class="content-Index">
          <Article></Article>
        </div>
    </div>
    <div class="right-Index">
      <about-me></about-me>
      <new-article></new-article>
      <archive></archive>
      <category></category>
      <tag></tag>
    </div>
  </div>
</template>
<script>
import Article from '@/components/blog/Article'
import AboutMe from '@/components/blog/AboutMe'
import NewArticle from '@/components/blog/NewArticle'
import Archive from '@/components/blog/Archive'
import Category from '@/components/blog/Category'
import Tag from '@/components/blog/Tag'
export default {
  name: 'Index',
  components: {
    Article,
    AboutMe,
    NewArticle,
    Archive,
    Category,
    Tag
  }
}
</script>
<style lang="stylus" scoped>
  .Index
    width: 960px
    margin: 0 200px
    // border-bottom: 2px solid red
  .wrapper-Index
    float: left
    margin-left: -30%
    width: 100%
    // float:left
    // widht: 60%
  .content-Index
    // border: 1px solid red
    margin-left: 30%
    // width: 100%
  .right-Index
    float: right
    width: 30%
</style>
