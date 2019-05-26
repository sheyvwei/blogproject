<template>
  <div class="new-wrapper">
    <div class="new-content">
      <h1>最新文章</h1>
      <ul>
        <li><i class="iconfont">&#xe6a2; <span>文章一</span></i></li>
        <li><i class="iconfont">&#xe6a2; <span>文章一</span></i></li>
        <li><i class="iconfont">&#xe6a2; <span>文章一</span></i></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'NewArticle'
}
</script>
<style lang="stylus" scoped>
  .new-wrapper
    margin: 10px
    padding: 20px
    text-align: left
    background-color: $bgColor
  .new-content
    // text-algin: left
</style>
