<template>
  <div>
    <!-- <div>
      <base-header></base-header>
    </div> -->
    <div class="header">
      <base-header></base-header>
    </div>
    <div class="center">
      <Index></Index>
    </div>
    <div class="footer">
      <base-footer></base-footer>
    </div>

  </div>
</template>
<script>
import BaseHeader1 from '@/components/BaseHeader1'
import BaseHeader from '@/components/BaseHeader'
import BaseFooter from '@/components/BaseFooter'
import Index from '@/pages/Index'
export default {
  name: 'Home',
  components: {
    BaseHeader,
    BaseFooter,
    Index,
    BaseHeader1
  }
}
</script>
<style lang="stylus" scoped>
  .header
    float: left
    width: 100%
  .center
    float: left
    width: 100%
  .footer
    float: left
    width: 100%
  // div
  //   display: block
</style>
