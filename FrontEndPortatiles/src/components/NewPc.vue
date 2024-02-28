<template>
  <div class="container mt-5 contenedor-general">
    <div class="card">
      <div class="card-header">
        <h2>Crear Portátil</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="crearPortatil">
          <div class="form-group">
            <label for="id">ID:</label>
            <input
              type="number"
              class="form-control"
              v-model="portatil.id"
              required
            />
          </div>
          <div class="form-group">
            <label for="modelo">Modelo:</label>
            <input
              type="text"
              class="form-control"
              v-model="portatil.modelo"
              required
            />
          </div>
          <div class="form-group">
            <label for="marca">Marca:</label>
            <input
              type="text"
              class="form-control"
              v-model="portatil.marca"
              required
            />
          </div>
          <div class="form-group">
            <label for="fechaLanzamiento">Fecha de Lanzamiento:</label>
            <input
              type="date"
              class="form-control"
              v-model="portatil.fechaLanzamiento"
              required
            />
          </div>
          <div class="form-group">
            <label for="tamaño">Tamaño:</label>
            <input
              type="number"
              step="any"
              class="form-control"
              v-model="portatil.tamaño"
              required
            />
          </div>
          <div class="form-group">
            <label for="precio">Precio:</label>
            <input
              type="number"
              class="form-control"
              v-model="portatil.precio"
              required
            />
          </div>
          <div class="form-group">
            <label for="procesador">Procesador:</label>
            <input
              type="text"
              class="form-control"
              v-model="portatil.procesador"
              required
            />
          </div>
          <div class="form-group">
            <label for="ram">RAM:</label>
            <input
              type="number"
              class="form-control"
              v-model="portatil.ram"
              required
            />
          </div>
          <div class="form-group">
            <label for="rom">ROM:</label>
            <input
              type="number"
              class="form-control"
              v-model="portatil.rom"
              required
            />
          </div>
          <div class="form-group">
            <label for="color">Color:</label>
            <input
              type="text"
              class="form-control"
              v-model="portatil.color"
              required
            />
          </div>
          <div class="form-group">
            <!-- <label for="imagen">Imagen (URL) o Cargar desde Archivo:</label> -->
            <input
              type="text"
              class="form-control"
              style="display: none"
              v-model="portatil.imagen"
              placeholder="URL de la imagen o elige un archivo"
              required
            />
            <input
              type="file"
              ref="fileInput"
              style="display: none"
              @change="handleFileChange"
            />
            <button
              type="button"
              class="btn btn-secondary my-3"
              @click="triggerFileInput"
            >
              Cargar Archivo
            </button>
          </div>
          <div v-if="portatil.imagen">
            <strong>Archivo seleccionado:</strong> {{ portatil.imagen.name }}
          </div>
          <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NewPc",

  data() {
    
    return {
      portatil: {
        id: null,
        modelo: "",
        marca: "",
        fechaLanzamiento: "",
        tamaño: null,
        precio: null,
        procesador: "",
        ram: null,
        rom: null,
        color: "",
        imagen: "",
      },
    }; 
  },
  methods: {
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        // Almacena el archivo seleccionado en el modelo
        this.portatil.imagen = file;
      }
    },

    triggerFileInput() {
      // Simula hacer clic en el input de archivo
      this.$refs.fileInput.click();
    },

    async crearPortatil() {
      try {
        // Crea un objeto FormData para enviar los datos del formulario
        const formData = new FormData();
        for (const key in this.portatil) {
          formData.append(key, this.portatil[key]);
        }

        // Realiza la solicitud POST con Axios
        const response = await axios.post(
          "http://127.0.0.1:8000/nuevoPortatil/",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );

        // Verifica si la respuesta fue exitosa
        if (response.status === 201) {
          alert("Portátil creado exitosamente, yes");
          // Limpiar los campos del formulario
          this.portatil = {
            id: null,
            modelo: "",
            marca: "",
            fechaLanzamiento: null,
            tamaño: 0,
            precio: 0,
            procesador: "",
            ram: 0,
            rom: 0,
            color: "",
            imagen: null,
            fileInput: null,
          };
        } else {
          alert("Error al crear el portátil");
        }
      } catch (error) {
        // Manejar errores de la solicitud
        alert(`Error: ${error.message}`);
      }
    },
  },
};
</script>

// async crearPortatil() { // try { // // Realizar la solicitud POST con Axios
// const response = await axios.post( // "http://127.0.0.1:8000/nuevoPortatil/",
// this.portatil // ); // // Verificar si la respuesta fue exitosa // if
(response.status === 201) { // alert("Portátil creado exitosamente"); // //
Limpiar los campos del formulario // this.portatil = { // id: null, // modelo:
"", // marca: "", // fechaLanzamiento: null, // tamaño: 0, // precio: 0, //
procesador: "", // ram: 0, // rom: 0, // color: "", // imagen: "", // }; // }
else { // alert("Error al crear el portátil"); // } // } catch (error) { // //
Manejar errores de la solicitud // alert(`Error: ${error.message}`); // } // },

<style>
.contenedor-general {
  overflow: auto;
}
/* Puedes agregar estilos personalizados aquí si es necesario */
</style>
