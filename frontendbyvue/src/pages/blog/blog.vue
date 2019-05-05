<template>
  <div>
    <blog-header></blog-header>
  </div>
</template>
<script>
import BlogHeader from './components/header'
export default {
  name: 'blog',
  components: {
    BlogHeader
  }
}
</script>
<style lang="stylus" scoped>
  .head
    background: blue
</style>
