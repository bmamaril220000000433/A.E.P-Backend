<script setup>
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import { RouterLink } from 'vue-router';

const validate = () => {
            const firstname = document.getElementById('fname').value;
            const lastname = document.getElementById('lname').value;
            const password = document.getElementById('pass').value;

            if (firstname === 'test' && password === 'test' && lastname === 'test') {
                alert('Create account successful!');
                window.open('/home','_self');
            }
            else {
                alert('The account is already createds. Please try logging in to your account.');
            }
        };
</script>


<template>

<body>
 <div class="frame">
 <div class="form">
  <form class="logos">
  <img src="/src/assets/uic1.png" class="uic1">
  <img src="/src/assets/myuic.png" class="myuic">
</form>
<form class="loginform">
  <InputText class="fname" id="fname" v-model="value1" type="text" size="small" placeholder="First Name"/>
  <InputText class="lname" id="lname" v-model="value2" type="text" size="small" placeholder="Last Name"/>
  <InputText class="pass" id="pass" v-model="value3" type="text" size="small" placeholder="Password"/>
  <Button @click="validate()">Register</Button>
   <p>
      <router-link to="/">Already have an account?</router-link>
   </p>
  </form> 
  </div>
</div>
</body>

</template>

<style scoped>
.frame{
  width: 1528px;
  height: 755px;
  padding: 1% 0 0;
  position:relative;
  background-image: url('/src/assets/bg.png');
  background-size:cover;
  background-repeat: no-repeat;
}
.form{
  width: 473px;
    height: 524px;
    padding-top: 2px;
    margin: 66px auto;
    background-color: rgba(217, 217, 217, 85%);
    border-radius: 15px;
}

.myuic{
position: relative;
margin: auto;
height:60px;
width:112px;
display: block;

}
.uic1{
position: relative;
margin:auto;
height: 150px;
width:150px;
display: block;
}

.fname{
  display: block;
  position: relative;
  margin-right: auto;
  margin-bottom: 12px;
  margin-left: auto;
  background: #FFFDFD;
border-radius: 20px;
height: 48px;
width: 275px;
}
.lname{
  display: block;
  position: relative;
  margin-right: auto;
  margin-bottom: 12px;
  margin-left: auto;
  background: #FFFDFD;
border-radius: 20px;
height: 48px;
width: 275px;
}
.pass{
  display: block;
  position: relative;
  margin:auto;
  background: #FFFDFD;
  margin-top: auto;
    margin-right: auto;
    margin-bottom: 14px;
    margin-left: auto;
  border-radius: 20px;
height: 48px;
width: 275px;

}

.logos {
  margin-bottom: 17px;
}
button{
display: block;
position: relative;
margin:auto;
background-color: #FA7B9F;
border-radius: 20px;
border-bottom: 12px;
height: 44px;
width: 180px;
}
p{
text-align: center;
}
::placeholder{
  text-align: center;
}
input {
 text-align: center;
}
</style>