<template>
  <div class="category-wrapper">
    <div class="category-content">
      <h1>分类</h1>
      <ul>
        <li><i class="iconfont">&#xe6ce; <span>前端</span></i></li>
        <li><i class="iconfont">&#xe6ce; <span>后端</span></i></li>
        <li><i class="iconfont">&#xe6ce; <span>数据库</span></i></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Category'
}
</script>
<style lang="stylus" scoped>
  .category-wrapper
    margin: 10px
    padding: 20px
    text-align: left
    background-color: $bgColor
</style>
