<template>
  <div class="header">
    <div class="container">
      <!-- logo -->
      <div class="logo">
        <img src="../assets/img/1.png" alt="logo" width="150" height="50" />
      </div>
      <!-- 头部导航 -->
      <div class="nav">
        <ul>
          <li>首页</li>
          <li>分类</li>
          <li>标签</li>
          <li>归档</li>
          <li>日志</li>
          <li>留言板</li>
        </ul>
      </div>
      <div class="center">
        <div>
          <i class="iconfont">&#xe60e;</i> 写文章
        </div>
      </div>
      <div class="right" >
        <ul>
          <li>登录</li>
          <li>注册</li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'BaseHeader'
}
</script>
<style lang="stylus" scoped>
// button
//   color:$color
//   background-color: $bgColor
div
  box-sizing: border-box
.header
  background-color: #fff
.container
  width: 100%
  background-color: $headerColor
.logo
  float: left  //logo图片在一行
  // margin-left: 20px
  // margin-top: 10px
  margin: 10px 50px
  // width: 0 auto
.nav li
  background-color: $headerColor
  color: $color
  float: left
  height: 60px
  line-height: 60px   //height和line-height同时设置60，表示垂直居中
  cursor: pointer
  font-size: 14px
  padding: 20px
  // margin 0px 25px
.center div
  float: left
  background-color: $headerColor
  color: $color
  height: 60px
  line-height: 60px   //height和line-height同时设置60，表示垂直居中
  cursor: pointer
  font-size: 14px
  margin: 0 200px
  padding: 20px
.right
  color: $color
  float: right
  height: 60px
  line-height: 60px
  cursor: pointer
  font-size: 20px
.right li
  background-color: $headerColor
  cursor: pointer
  float: right
  color: $clickColor
  padding: 20px
  font-size: 14px
  height: 60px
  line-height: 60px
li:hover
  color: $hover
</style>
