<template>
  <div class="tag-wrapper">
    <div class="tag-content">
      <h1>标签</h1>
      <ul>
        <li><i class="iconfont">&#xe789; <span>HTML</span></i></li>
        <li><i class="iconfont">&#xe789; <span>JAVA</span></i></li>
        <li><i class="iconfont">&#xe789; <span>VUE</span></i></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Tag'
}
</script>
<style lang="stylus" scoped>
  .tag-wrapper
    margin: 10px
    padding: 20px
    text-align: left
    background-color: $bgColor
</style>
