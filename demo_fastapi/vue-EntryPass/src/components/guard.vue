<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { ref } from 'vue';

const categories = ref([
  {
    id: 1,
    name: "Alice",
    date: "12/13/23",
    time:"12:13PM",
    office:"Cashier",

  },
  {
    id: 2,
    name: "Paul",
    date: "12/13/23",
    time:"12:13PM",
    office:"Cashier",
  }
]);

const editingCategory = ref(null);
const newCategory = ref({ name: '', date: '', time: '', office: ''}); // New category object

const editCategory = (category) => {
  editingCategory.value = { ...category.data }; // Set editingCategory to the selected category's data
};

const saveEditedCategory = () => {
  if (editingCategory.value) {
    // Update the category data with the edited values
    const index = categories.value.findIndex((c) => c.id === editingCategory.value.id);
    categories.value[index].name = editingCategory.value.name;
    categories.value[index].date = editingCategory.value.date;
    categories.value[index].time = editingCategory.value.time;
    categories.value[index].office = editingCategory.value.office;
    editingCategory.value = null;
  }
};

const cancelEdit = () => {
  editingCategory.value = null;
};

const deleteCategory = (category) => {
  // Find the index of the category
  const index = categories.value.findIndex((c) => c.id === category.id);
  // Remove the category from the categories array
  categories.value.splice(index, 1);
};

const addCategory = () => {
  if (newCategory.value.name && newCategory.value.description) {
    // Generate a new unique ID (replace with your actual ID generation logic)
    const newId = Math.max(...categories.value.map((c) => c.id)) + 1;
    newCategory.value.id = newId;
    categories.value.push({ ...newCategory.value });
    // Clear the form for the next addition
    newCategory.value.name = '';
    newCategory.value.date = '';
    newCategory.value.time = '';
    newCategory.value.office = '';
  }
};
</script>

<template>
  <body>
    
    <div class="Whitebackground"><form class="logos">
  <img src="/src/assets/uic1.png" class="uiclogo">
  <img src="/src/assets/myuic.png" class="myuic">
</form>
    
    <div class="Graybackground"></div>
    
    <div class="Curvebox">
      <h2 class="Admin">Admin</h2>
    </div>
    <div class="Curvebox1">
      <h2 class="OIC">Office in Charge</h2>
    </div>
    <div class="Curvebox2">
      <h2 class="Guard">Guard</h2>
    </div>
    <div class="Curvebox3">
      <h2 class="Booking">Booking</h2>
    </div>
    <div class="Pinkbackground">
      <h1>Visitor Information</h1>
      
    <div class="Whitebackground1">
      

  
  <div>
    
    
    <DataTable :value="categories" tableStyle="min-width: 50rem">
      <Column field="id" header="ID"></Column>
      <Column field="name" header="Name"></Column>
      <Column field="date" header="Date"></Column>
      <Column field="time" header="Time"></Column>
      <Column field="office" header="Office"></Column>
      <Column header="Actions">
        <template #body="rowData">
          <Button label="Edit" icon="pi pi-pencil" class="p-button-info" @click="editCategory(rowData)" />
          <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="deleteCategory(rowData)" />
          <Button label="Confirm" icon="pi pi-pencil" class="p-button-info" @click="editCategory(rowData)" />
          <Button label="Decline" icon="pi pi-pencil" class="p-button-info" @click="editCategory(rowData)" />
        </template>
      </Column>
    </DataTable>

    <div v-if="editingCategory">
      <h2>Edit Category</h2>
      <form @submit="saveEditedCategory">
        <div>
          <label for="editedName">Name:</label>
          <InputText id="editedName" v-model="editingCategory.name" />
        </div>
        <div>
          <label for="editedDate">Date:</label>
          <InputText id="editedDate" v-model="editingCategory.date" />
        </div>
        <div>
          <label for="editedTime">Time:</label>
          <InputText id="editedTime" v-model="editingCategory.time" />
        </div>
        <div>
          <label for="editedOffice">Office:</label>
          <InputText id="editedOffice" v-model="editingCategory.office" />
        </div>
        <div>
          <Button label="Save" icon="pi pi-check" class="p-button-success" type="submit" />
          <Button label="Cancel" icon="pi pi-times" class="p-button-secondary" @click="cancelEdit" />
        </div>
      </form>
    </div>

    <!-- Add Category Form -->
    <div>
      <h2 class="Addvisitor">Add Visitor</h2>
      <form @submit.prevent="addCategory">
        <div>
          <label class="Name" for="newName">Name:</label>
          <InputText id="newName" v-model="newCategory.name" />
        </div>
        <div>
          <label class="Date" for="newDate">Date:</label>
          <InputText id="newDate" v-model="newCategory.date" />
        </div> 
        <div>
          <label class="Time" for="newTime">Time:</label>
          <InputText id="newTime" v-model="newCategory.time" />
        </div>
        <div>
          <label class="Office" for="newOffice">Office:</label>
          <InputText id="newOffice" v-model="newCategory.office" />
        </div> 
        <div>
          <Button label="Add" icon="pi pi-plus" class="p-button-primary" type="submit" />
        </div>
      </form>
    </div>
  </div>
</div>
</div>
</div>
</body>
</template>

<style scoped>
body {
background-image: url('/src/assets/bg.png');
position: relative;
width: 1920px;
height: 1080px;
left: 0px;
top: 0px;
}
.Whitebackground{
  position: relative;
  border: 1px solid;
  width: 1683px;
  height: 902px;
  top: 12%;
  padding: 2% 0 0;
  margin: auto;
  background-color:rgba(217, 217, 217, 85%);
}

.Whitebackground1{
  position: absolute;
  border: 1px solid;
  width: 1045px;
  height: 496px;
  right: 10%;
  bottom: 8%;
  background-color:rgba(217, 217, 217, 50%);
}
.myuic{
position: absolute;
margin: auto;
width:222px;
height:90px;
top: 9.5%;
right: 39.5%;
display: block;

}
.uiclogo{
position: absolute;
margin:auto;
width:215px;
height:215px;
top: -12.5%;
right: 40%;
display: block;
padding-bottom: 8px;
}

.p-button-primary{
  position: absolute;
  right: 71%;
  bottom: 2%;
  font-family: arial;
}

.Addvisitor{
  position: absolute;
  right: 69%;
  bottom: 40%;
}

.Name{
  position: absolute;
  left: 7%;
  bottom: 37%;
}


#newName{
  position: absolute;
  border-radius: 10px;
  width: 269px;
  height: 35px;
  top: 58%;
  left: 12%;
}

.Date{
  position: absolute;
  left: 7%;
  bottom: 28.5%;
}

#newDate{
  position: absolute;
  border-radius: 10px;
  width: 269px;
  height: 35px;
  top: 66%;
  left: 12%;
}

.Time{
  position: absolute;
  left: 7%;
  bottom: 20.5%;
}

#newTime{
  position: absolute;
  border-radius: 10px;
  width: 269px;
  height: 35px;
  top: 74%;
  left: 12%;
}

.Office{
  position: absolute;
  left: 7%;
  bottom: 12.5%;
}

#newOffice{
  position: absolute;
  border-radius: 10px;
  width: 269px;
  height: 35px;
  top: 82.2%;
  left: 12%;
}


h1{
  position: absolute;
  right: 37.5%;
  top: 1%;
  font-family: arial;
}

.Admin{
  position: absolute;
  right: 32%;
  bottom: -28%;
  font-family: arial;
}

.OIC{
  position: absolute;
  width: 190px;
  right: 4%;
  bottom: -30%;
  font-family: arial;
}

.Guard{
  position: absolute;
  right: 34%;
  bottom: -20%;
  font-family: arial;
}

.Booking{
  position: absolute;
  right: 26%;
  bottom: -28%;
  font-family: arial;
}

.Pinkbackground{
  position: absolute;
  border: 1px solid;
  width: 1319px;
  height: 641px;
  top: 20%;
  right: 2%;
  padding: 2% 0 0;
  margin: auto;
  background-color:rgba(234, 198, 235, 100%);
}
.Graybackground{
  position: absolute;
  border-radius: 20px;
  top: 25%;
  left: 2%;
  width: 271px;
  height: 576px;
  background-color:rgba(184, 184, 184, 100%);
}

.Curvebox{
  position: absolute;
  border-radius: 15px;
  width: 210px;
  height: 43px;
  top: 28%;
  left: 3.8%;
  background-color:rgba(255, 255, 255, 100%);
}

.Curvebox1{
  position: absolute;
  border-radius: 15px;
  width: 210px;
  height: 43px;
  top: 35%;
  left: 3.8%;
  background-color:rgba(255, 255, 255, 100%);
}

.Curvebox2{
  position: absolute;
  border-radius: 15px;
  width: 234px;
  height: 51px;
  top: 42%;
  left: 3%;
  background-color:rgba(238, 139, 204, 100%);
}

.Curvebox3{
  position: absolute;
  border-radius: 15px;
  width: 210px;
  height: 43px;
  top: 50%;
  left: 3.8%;
  background-color:rgba(255, 255, 255, 100%);
}
</style>
