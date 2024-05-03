<script setup>

</script>

<template>
  <body>
 <div class="frame">
  <div class="sidepanel">
  <aside>
    <div class="wrapper">
    <div class="image_logo">
          <img class="logo" src="/src/assets/logo.enp.png">
        </div>
     <div class="header_title">
      <p>Automated Entry Pass</p>
     </div>  
    </div>
    <nav class="nav flex-column">
      <p class="welcomMess">Hi Visitors!</p>
  <a class="nav-link-book" href="/booking">Book Appointment</a>
  <a class="nav-link-view" href="/viewapps">View Appointment</a>
  <a class="nav-link-settings" href="#">Settings</a>
  <a class="nav-link-logout" href="/">Logout</a>
</nav>
  </aside>
</div>
 <div id="mainframe">
   
      <table>
    <thead>
        <tr>
            <th colspan="3" id="title_header">Recent Appointments</th>
        </tr>
        <tr id="tlabels">
            <th>Date</th>
            <th>Time</th>
            <th>Purpose of Visit</th>
        </tr>
    </thead>
    <tbody>
       
    </tbody>
</table>


  </div>
 </div>

</body>
</template>

<style scoped>
.frame{
  width: 1528px;
  height: 755px;
  position:relative;
  background-image: url('/src/assets/bg.png');
  background-size:cover;
  background-repeat: no-repeat;
  display:flex;
}
p{
  color: rgb(255, 255, 255);
}
#mainframe{
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: rgba(238, 139, 204, 0.24); 
  }

  #frame1{
    width: 1054.81px;
    height: 639px;
    background-color: rgb(217, 217, 217,0.38);
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
aside{
float: left;
background-color: #F27B8A;
width: 288.84px;
height: 755px;
}
.logo{
  width: 39.79px;
  height: 35.01px;
  position:static;
  border-radius: 20px;
  margin-top: 37px;
  margin-left: 23px;
}
.nav-link-book{
  color: rgb(255, 255, 255);
  text-decoration: none;
  margin-left: 23px;
  margin-bottom:24px;
  margin-top: 70px;
}
.nav-link-view{
  color: rgb(0, 0, 0);
  text-decoration: none;
  margin-left: 23px;
  margin-bottom: 319px;
}
.nav-link-settings{
  color: rgb(255, 255, 255);
  text-decoration: none;
  margin-left: 23px;
  margin-bottom: 18px;
}
.nav-link-logout{
  color: rgb(255, 255, 255);
  text-decoration: none;
  margin-left: 23px;
}
.image_logo{
  flex:1;
  margin-right: 10px;
}
.wrapper{
  display: flex;
  align-items: center;
  justify-content: center;
}
.header_title{
  flex: 2;
  text-align: left;
  margin-top: 55px;
  padding-right: 45px;
  
}
.image-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; 
        margin-bottom: 20px;
        margin-left: 47px;
    }

.image-container div {
        width: 45%; 
        margin-bottom: 10px;
        margin-top: 47px;

    }
    .image-container img {
        max-width: 50%;
        height: auto;
    }
    table{
      background-color: rgb(217, 217, 2217, 38%);
      width:1054.81px ;
      height: 279.67px;
    }
    #title_header{
    color: rgb(255, 255, 255);
    margin-top: 21px;
    margin-left: 27px;
    margin-bottom: 21px;
    font-size:15px;
    background-color: #F27B8A;
    height: 49.86px;
    }
    .header_table{
    background-color: rgb(215, 122, 135);
    height:60.07px ;
    width:1054.81px ;
    }
    #tlabels{
      color: #F27B8A;
      background-color: #D9D9D9;
      text-align: center;
    }
  

    .welcomMess{
      margin-left: 23px;
      margin-top: 44px;
    }
</style>