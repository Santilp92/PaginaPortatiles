<template>
  <div class="card my-3 mx-3 container-fluid" v-if="selectedPc">
    <div class="row g-0" id="contenedor-card">
      <div class="col-md-4">
        <div class="container" id="contenedor-img">
          <img
            :src="getMediaUrl(selectedPc.imagen)"
            alt="Imagen pc"
            class="img-fluid"
          />
        </div>
      </div>
      <div class="col-md-8" id="contenedor-info">
        <div class="card-body">
          <div class="row">
            <h5 class="card-title" id="nombre-pc">
              Computador Portátil {{ selectedPc.marca }} -
              {{ selectedPc.pantalla }}" {{ selectedPc.modelo }} -
              {{ selectedPc.procesador }} - {{ selectedPc.ram }}GB - Disco SSD{{
                selectedPc.rom
              }}GB - {{ selectedPc.color }}.
            </h5>
          </div>
          <div class="row" id="marca">
            <p>
              <button type="button" class="btn btn-outline-secondary" disabled>
                {{ selectedPc.marca }}
              </button>
            </p>
          </div>
          <div class="row" id="datos-pc">
            <div class="col-4" id="procesador">
              <h6>Procesador</h6>
              <p>{{ selectedPc.procesador }}</p>
            </div>
            <div class="col-4" id="ram">
              <h6>Memoria RAM</h6>
              <p>{{ selectedPc.ram }} GB</p>
            </div>
            <div class="col-4" id="rom">
              <h6>Disco Duro</h6>
              <p>Disco SSD {{ selectedPc.rom }}GB</p>
            </div>
            <div class="row">
              <div class="col-6" id="precio">
                <h6>Precio</h6>
                <p>$ {{ selectedPc.precio }}</p>
              </div>
              <div
                class="col align-self-center offset-md-2 text-end"
                id="opciones"
              >
                <div class="container">
                  <button
                    v-if="isAuthorized === true"
                    @click.prevent="updatePc(selectedPc)"
                    id="updatePc"
                    type="button"
                    class="btn btn-outline-dark me-2"
                  >
                    Modificar
                  </button>
                  <button
                    v-if="isAuthorized === true"
                    @click.prevent="confirmDeletePc(selectedPc)"
                    id="eliminatePc"
                    type="button"
                    class="btn btn-outline-dark me-2"
                  >
                    Eliminar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  
  name: "Portatil",
  computed: {
    selectedPc() {
      return this.$store.state.selectedPc;
    },
    isAuthorized() {
      return this.$store.state.isAuthorized;
    },
  },

  methods: {
    confirmDeletePc(pc) {
      const isConfirmed = window.confirm(
        `¿Estás seguro de eliminar el computador con ID ${pc.id}?`
      );
      if (isConfirmed) {
        this.eliminatePc(pc);
      }
    },

    eliminatePc(pc) {
      axios
        .delete(`http://127.0.0.1:8000/portatil/${pc.id}/`)
        .then((response) => {
          alert("Portatil Eliminado");
          this.$emit("loadHome");
        })
        .catch((error) => {
          console.error("Error al eliminar el portátil:", error);
        });        
      },

    updatePc(pc) {
      this.$store.commit("setSelectedPc", pc);
      this.$emit("loadPortatil", pc);
    },
    getMediaUrl(filename) {
      // Combina la URL base de media con el nombre del archivo
      return `http://127.0.0.1:8000/${filename}`;
    },
  },
};
</script>

<style>
</style>