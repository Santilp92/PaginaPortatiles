<!-- src/views/Portatil.vue -->
<template>
  <div>
    <h1>Detalles del Portátil</h1>
    <div v-if="selectedPc">
      <img :src="selectedPc.img" alt="Imagen pc" />
      <h2>{{ selectedPc.marca }} - {{ selectedPc.modelo }}</h2>
      <p>Procesador: {{ selectedPc.procesador }}</p>
      <p>Memoria RAM: {{ selectedPc.ram }} GB</p>
      <p>Disco Duro: SSD {{ selectedPc.rom }} GB</p>
      <p>Precio: ${{ selectedPc.precio }}</p>
      <!-- Agrega más detalles según sea necesario -->
    </div>
    <div v-else>
      <p>No se ha seleccionado ningún portátil.</p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    selectedPc() {
      return this.$store.state.selectedPc; // Obtener el PC seleccionado del store
    },
  },
};
</script>

// export default {
//   data() {
//     return {
//       pc: null,
//     };
//   },
//   created() {
//     // Acceder al objeto pc de los parámetros de la ruta
//     this.pc = this.$route.params.pc;
//   },
