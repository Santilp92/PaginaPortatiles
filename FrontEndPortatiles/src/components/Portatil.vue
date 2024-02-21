<template>
  <div>
    <h1>hola</h1>
    
  </div>
</template>

<script>
export default{
  name:"Portatil",
  data(){
    return{
      
    }
  }
}
// export default {
//   name: "Portatil",
//   data() {
//     return {
//       pcId: null,
//       pcDetails: {}, // Almacena los detalles de la computadora portátil
//       // Otras propiedades para detalles de la computadora portátil
//     };
//   },
//   mounted() {
//     // Recupera el id de la ruta actual
//     this.pcId = this.$route.params.id;

//     // Ahora, puedes cargar los detalles de la computadora portátil utilizando this.pcId
//     // Ejemplo: Llama a una función que carga detalles desde tu servicio
//     this.loadPcDetails();
//   },
//   methods: {
//     loadPcDetails() {
//       // Aquí deberías llamar a un servicio para obtener los detalles de la computadora portátil
//       // Simularemos un servicio con una llamada asíncrona
//       setTimeout(() => {
//         // Supongamos que los detalles se cargan con éxito desde el servicio
//         this.pcDetails = {
//           name: "Nombre de la computadora portátil",
//           processor: "Intel Core i5",
//           ram: "8GB",
//           // Agrega más propiedades según tus necesidades
//         };
//       }, 1000); // Simulamos un tiempo de carga de 1 segundo
//     },
//   },
// };
</script>


<style></style>
