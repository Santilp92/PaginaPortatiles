<template>
  <div class="card my-3 mx-3 container-fluid" v-if="selectedPc">
    <div class="row g-0" id="contenedor-card">
      <div class="col-md-4 container" id="contenedor-img">
        <div class="card-body">
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
          </div>
          <div class="row" id="datos-pc">
            <div class="col-4" id="precio">
              <h6>Precio</h6>
              <p>$ {{ selectedPc.precio }}</p>
            </div>
            <div class="col-4">
              <h6>Color</h6>
              <p>{{ selectedPc.color }}</p>
            </div>
            <div class="col-4">
              <h6>Fecha de Lanzamiento</h6>
              <p>{{ selectedPc.fechaLanzamiento }}</p>
            </div>
          </div>
          <div class="row">
            <div
              class="col align-self-center offset-md-2 text-end"
              id="opciones"
            >
              <div class="container">
                <!-- Modal de Modificación -->
                <div
                  class="modal fade"
                  aria-hidden="true"
                  tabindex="-1"
                  ref="updateModal"
                  id="updateModal"
                  data-bs-backdrop="static"
                  data-bs-keyboard="false"
                >
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">Modificar Computador</h5>
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="modal"
                          aria-label="Close"
                        ></button>
                      </div>
                      <div class="modal-body text-start">
                        <!-- Contenido del modal -->
                        <div class="mb-3">
                          <label for="modelo" class="form-label">Modelo</label>
                          <input
                            type="text"
                            class="form-control"
                            id="modelo"
                            v-model="selectedPc.modelo"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="marca" class="form-label">Marca</label>
                          <input
                            type="text"
                            class="form-control"
                            id="marca"
                            v-model="selectedPc.marca"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="procesador" class="form-label"
                            >Procesador</label
                          >
                          <input
                            type="text"
                            class="form-control"
                            id="procesador"
                            v-model="selectedPc.procesador"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="fechaLanzamiento" class="form-label"
                            >Fecha de Lanzamiento:</label>
                          <input
                            type="date"
                            class="form-control"
                            id="fechaLanzamiento"
                            v-model="selectedPc.fechaLanzamiento"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="ram" class="form-label">Ram</label>
                          <input
                            type="text"
                            class="form-control"
                            id="ram"
                            v-model="selectedPc.ram"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="rom" class="form-label">rom</label>
                          <input
                            type="text"
                            class="form-control"
                            id="rom"
                            v-model="selectedPc.rom"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="precio" class="form-label">Precio</label>
                          <input
                            type="text"
                            class="form-control"
                            id="precio"
                            v-model="selectedPc.precio"
                          />
                        </div>
                        <div class="mb-3">
                          <label for="color" class="form-label">Color</label>
                          <input
                            type="text"
                            class="form-control"
                            id="color"
                            v-model="selectedPc.color"
                          />
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-primary"
                          data-bs-target="#mensajeExitoso"
                          data-bs-toggle="modal"
                          @click="saveUpdatedPc"
                        >
                          Guardar
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="modal fade"
                  id="mensajeExitoso"
                  aria-hidden="true"
                  aria-labelledby="guardadoExitosamente"
                  tabindex="-1"
                  data-bs-backdrop="static"
                  data-bs-keyboard="false"
                >
                  <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h1 class="modal-title fs-5" id="guardadoExitosamente">
                          Mensaje de Confirmación
                        </h1>
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="modal"
                          aria-label="Close"
                        ></button>
                      </div>
                      <div class="modal-body text-center">
                        El portátil se ha actualizado correctamente.
                      </div>
                      <div class="modal-footer"></div>
                    </div>
                  </div>
                </div>
              </div>
              <button
                v-if="isAuthorized === true"
                id="updatePc"
                type="button"
                class="btn btn-outline-dark me-2"
                data-bs-toggle="modal"
                data-bs-target="#updateModal"
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
</template>

<script>
import axios from "axios";

export default {
  name: "Portatil",

  data() {
    return {};
  },

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
        .delete(`https://santilp92.pythonanywhere.com/portatil/${pc.id}/`)
        .then((response) => {
          alert("Portatil Eliminado");
          this.$emit("loadHome");
        })
        .catch((error) => {
          console.error("Error al eliminar el portátil:", error);
        });
    },

    getMediaUrl(filename) {
      // Combina la URL base de media con el nombre del archivo
      return `https://santilp92.pythonanywhere.com/${filename}`;
    },

    saveUpdatedPc() {
      const updatedPc = {
        modelo: this.selectedPc.modelo,
        marca: this.selectedPc.marca,
        procesador: this.selectedPc.procesador,
        ram: this.selectedPc.ram,
        rom: this.selectedPc.rom,
        precio: this.selectedPc.precio,
        color: this.selectedPc.color,
        fechaLanzamiento : this.selectedPc.fechaLanzamiento,
      };

      axios
        .patch(
          `https://santilp92.pythonanywhere.com/portatil/${this.selectedPc.id}/`,
          updatedPc
        )
        .then((response) => {})
        .catch((error) => {
          console.error("Error al actualizar el portátil:", error);
        });
      // Después de la petición, cierra el modal
    },
  },
};

//Metodo para solicitar la información de un solo pc
// methods: {
//   getData: async function () {
//     let idPc = 345;
//     axios
//       .get(`https://santilp92.pythonanywhere.com/portatil/${idPc}/`)
//       .then((response) => {
//         this.nombre = response.data.nombre;
//         this.marca = response.data.marca;
//         this.tamaño = response.data.tamaño;
//         this.procesador = response.data.procesador;
//         this.ram = response.data.ram;
//         this.rom = response.data.rom;
//         this.precio = response.data.precio;
//         console.log(response);
//       })
//       .catch((error) => {
//         console.log(error);
//         // if (error.response.status.alert )
//         //   alert("ERROR 400: Error.");
//       });
//   },
// },
</script>

<style></style>
