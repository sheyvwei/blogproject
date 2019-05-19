<template>
  <div>
    <div class="content">
      <div class="container">
        <h1>博客登陆</h1>
        <form>
          <input type="text" placeholder="用户名" />
          <input type="password" placeholder="密码" />
          <div class="login">
            <button  type="submit">登录</button>
            <!-- <button type="submit">注册</button> -->
          </div>
        </form>
        <div class="footer">
          about me
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Login'
}
</script>
<style lang="stylus" scoped>
.content
  min-width: 100%
  min-height: 100%
.container
  background-color: white
  position: absolute
  width: 300px
  height: 260px
  left: 50%
  margin-top: 150px
  margin-left: -180px
  border-radius: 10px
  padding: 30px
.container h1
  text-align: center
  font-size: 24px
  margin-bottom : 20px
  // vertical-align: center
.container input
  border-radius: 4px
  border: 1px solid #dcdfe6
  height: 40px
  line-height: 1px
  padding: 0 15px
  width: 200px
  width: 100% //每个input占一行 332  (padding 15 border 1 )
  font-size: inherit //规定应该从父元素继承字体尺寸
  box-sizing: border-box  //子元素超出了父元素的宽度 为元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制
  margin-bottom: 20px
.container button
  width: 100%
  cursor: pointer
  border: 1px solid #dcdfe6;
  text-align: center
  border-radius: 3px
  padding: 10px 20px
  color: white
  background-color: #5FB878

button:hover
  background-color: rgb(127, 198, 147) //red
.footer
  padding: 10px 20px
  // font-size: 12px
</style>
