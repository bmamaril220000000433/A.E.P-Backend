<script setup> 

</script> 

<template> 
<body> 
  <div class="Whitebackground"><form class="logos">
  <img src="/src/assets/uic1.png" class="uiclogo">
  <img src="/src/assets/myuic.png" class="myuic">
</form>
<div class="Pinkbackground">
  <div class="whitebackground">
  <div class="confirmation"> 
    <h1 class="Text">ARE YOU SURE THAT THIS IS YOUR </h1> 
    <h1 class="Text2">FINAL BOOK REQUEST?</h1>
    </div>
   
  </div> 
   <router-link class="confirm" to="">Confirm</router-link>
    <router-link class="cancel" to="/booking">Cancel</router-link>
</div>
</div>
    </body> 
    
</template> 

    <style scoped> 
    
    body { background-image: url('/src/assets/bg.png'); 
    position: relative; 
    width: 1920px; 
    height: 1080px; 
    left: 0px; top: 0px; } 
    p{ font-size: small; 
    font-family: 'mulish'; 
    color: black; 
    position: relative; } 

  .Whitebackground{
  position: absolute;
  border: 1px solid;
  width: 1262px;
  height: 786px;
  top: 15%;
  left: 17%;
  padding: 2% 0 0;
  margin: auto;
  background-color:rgba(217, 217, 217, 85%);
}

.uiclogo{
position: absolute;
margin:auto;
width: 215px;
height: 215px;
top: -18%;
right: 40%;
display: block;
padding-bottom: 8px;
}
.myuic{
position: absolute;
margin: auto;
width:222px;
height:90px;
top: 8%;
right: 39.5%;
display: block;
}

.Pinkbackground{
  position: absolute;
  border: 1px solid;
  width: 967px;
  height: 473px;
  top: 20%;
  right: 11.5%;
  padding: 2% 0 0;
  margin: auto;
  background-color:rgba(234, 198, 235, 100%);
}
.confirm{

position: relative;
margin:auto;
background-color: #EE8BCC;
border-radius: 20px;
height: 58px;
width: 172px;
top: 220px;
left: 75%;

}
.cancel{

position: relative;
margin:auto;
background-color: #EE8BCC;
border-radius: 20px;
height: 58px;
width: 221px;
top: 220px;
left: 10%;
}

.Text{
  position: relative;
  width: 70%;
  left: 23%;
}
.Text2{
  position: relative;
  width: 70%;
  top: -15px;
  left: 31.5%;
}
    </style>