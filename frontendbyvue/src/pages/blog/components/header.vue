<template>
  <div class="header">
    <div class="header-left">
      <h1 class="left-content"><a href="#"><b>Black</b> &amp; White</a></h1>
    </div>

    <div class="header-right">
      <ul class="right-ul">
        <li class="right-content"><a href="#"></a>首页</li>
        <li class="right-content"><a href="#"></a>博客</li>
        <li class="right-content"><a href="#"></a>关于</li>
        <li class="right-content"><a href="#"></a>联系</li>
        <li class="right-content">
          <span class="iconfont search-icon">&#xe615;</span>
          <input type="text" placeholder="搜索关键词"/>
        </li>
      </ul>
  </div>
  </div>
</template>
<script>
export default {
  name: 'BlogHeader'
}
</script>
<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .header-left
    float left
    position relative
    .left-content
      margin-top: 8px
      font-size: 24px
      background: $bgColor
      color: #333333
      text-align:center

  .header-right
    display:inline
    .right-ul
      float:right !important
      margin-right:15px
      .right-content
        list-style-type:none
        float: left
        padding: 10px 0
        color: $color
        text-shadow: none
        text-align :center

        padding: 10px 0;
        text-shadow: none;
</style>
