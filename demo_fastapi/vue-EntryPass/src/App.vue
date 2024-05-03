<script setup>
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'
const router = useRouter();

onBeforeMount(() =>
{router.push('/')}
);
const fetch =async () =>{
  try{
    const response = await axios.get('');
    console.log(response.data)
  }
  catch (error){
    console.error('Error Message:', error);
  }
  finally{

  }
};
fetch()
</script>


<template>
  <div>
  <!--<Menubar :model="items" />-->
  <router-view></router-view>
</div>

</template>

<style scoped></style>