<template>
  <div class="flex-shrink-0 p-3 side-bar" style="width: 250px; height: 100%">
    <a
      href="/"
      class="d-flex align-items-center pb-3 mb-3 link-body-emphasis text-decoration-none border-bottom"
    >
      <span class="fs-5 fw-bold">Filtrar por:</span>
    </a>
    <ul class="list-unstyled ps-0">
      <li class="mb-1" id="marca">
        <button
          class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed"
          data-bs-toggle="collapse"
          data-bs-target="#home-collapse"
          aria-expanded="true"
        >
          Marca
        </button>
        <div class="collapse show" id="home-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >HP</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >LENOVO</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >ASUS</a
              >
            </li>
          </ul>
        </div>
      </li>
      <li class="mb-1">
        <button
          class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed"
          data-bs-toggle="collapse"
          data-bs-target="#dashboard-collapse"
          aria-expanded="false"
        >
          Procesador
        </button>
        <div class="collapse" id="dashboard-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >Intel Core i7</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >Intel Core i5</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >AMD Raizen 5</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >AMD Raizen 3</a
              >
            </li>
          </ul>
        </div>
      </li>
      <li class="mb-1">
        <button
          class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed"
          data-bs-toggle="collapse"
          data-bs-target="#orders-collapse"
          aria-expanded="false"
        >
          Memoria RAM
        </button>
        <div class="collapse" id="orders-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >32 GB</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >16 GB</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >12 GB</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >8 GB</a
              >
            </li>
          </ul>
        </div>
      </li>
      <li class="border-top my-3"></li>
      <li class="mb-1">
        <button
          class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed"
          data-bs-toggle="collapse"
          data-bs-target="#account-collapse"
          aria-expanded="false"
        >
          Tamaño Pantalla
        </button>
        <div class="collapse" id="account-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >21"</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >18"</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >17"</a
              >
            </li>
            <li>
              <a
                href="#"
                class="link-body-emphasis d-inline-flex text-decoration-none rounded"
                >15"</a
              >
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </div>

  <div class="container-fluid contenedor-general"
    id="card-auto"
    style="width: 100%">
    <div id="app">
    <div v-for="pc in pc_portatiles" :key="pc.id" class="card-container">
      <div class="card my-3 mx-3">
        <div class="row g-0" id="contenedor-card">
          <div class="col-md-4">
            <div class="container" id="contenedor-img">
              <img :src="pc.img" class="img-fluid" alt="Imagen pc" />
            </div>
          </div>
          <div class="col-md-8" id="contenedor-info">
            <div class="card-body">
              <div class="row">
                <h5 class="card-title" id="nombre-pc">
                  Computador Portátil {{ pc.marca }} - {{ pc.pantalla }}"
                  {{ pc.modelo }} - {{ pc.procesador }} - {{ pc.ram }}GB - Disco
                  SSD{{ pc.rom }}GB - {{ pc.color }}.
                </h5>
              </div>
              <div class="row" id="marca">
                <p>
                  <button
                    type="button"
                    class="btn btn-outline-secondary"
                    disabled
                  >
                    {{ pc.marca }}
                  </button>
                </p>
              </div>
              <div class="row" id="datos-pc">
                <div class="col-4" id="procesador">
                  <h6>Procesador</h6>
                  <p>{{ pc.procesador }}</p>
                </div>
                <div class="col-4" id="ram">
                  <h6>Memoria RAM</h6>
                  <p>{{ pc.ram }} GB</p>
                </div>
                <div class="col-4" id="rom">
                  <h6>Disco Duro</h6>
                  <p>Disco SSD {{ pc.rom }}GB</p>
                </div>
                <div class="row">
                  <div class="col-6" id="precio">
                    <h6>Precio</h6>
                    <p>$ {{ pc.precio }}</p>
                  </div>
                  <div
                    class="col align-self-center offset-md-2 text-end"
                    id="detalle"
                  >
                    <p class="invisible" id="idPc">{{ pc.id }}</p>
                    <h6>
                      <a
                        @click.prevent="processPortatil(pc)"
                        class="verDetalles"
                        href="#"
                      >
                        ver más detalles
                      </a>
                    </h6>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  </div>
  

  <!-- <div
    class="container-fluid contenedor-general"
    id="card-auto"
    style="width: 100%"
  ></div> -->

  <!-- <div class="container-fluid contenedor-general" style="width: 100%">    
    <div class="card my-3 mx-3">
      <div class="row g-0" id="contenedor-card">
        <div class="col-md-4">
          <div class="container" id="contenedor-img">
            <img
              src="https://www.ktronix.com/medias/750Wx750H-master-hotfolder-transfer-incoming-deposit-hybris-interfaces-IN-media-product-197532261341-001.jpg?context=bWFzdGVyfGltYWdlc3wxNTYwNTd8aW1hZ2UvanBlZ3xhRFV3TDJnd1pDOHhOREF3Tmprek56Z3hNekF5TWk4M05UQlhlRGMxTUVoZmJXRnpkR1Z5TDJodmRHWnZiR1JsY2k5MGNtRnVjMlpsY2k5cGJtTnZiV2x1Wnk5a1pYQnZjMmwwTDJoNVluSnBjeTFwYm5SbGNtWmhZMlZ6TDBsT0wyMWxaR2xoTDNCeWIyUjFZM1F2TVRrM05UTXlNall4TXpReFh6QXdNUzVxY0djfDNiNDY5MTViNzExNDFiMTg5YzFiMzYyMTgzNzcwMGFjMzhkYmJmZmU4YzJhODg4YmFkNDc0NjlkY2JjMzQ3OTI"
              class="img-fluid"
              alt="Imagen pc"
            />
          </div>
        </div>
        <div class="col-md-8" id="contenedor-info">
          <div class="card-body">
            <div class="row">
              <h5 class="card-title" id="nombre-pc">
                Computador Portátil LENOVO 15,6" Pulgadas IdeaPad Slim 3 Táctil
                - Intel Core i5 - RAM 8GB - Disco SSD 512GB - Gris
              </h5>
            </div>
            <div class="row" id="marca">
              <p>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  disabled
                >
                  LENOVO
                </button>
              </p>
            </div>
            <div class="row" id="datos-pc">
              <div class="col-4" id="procesador">
                <h6>Procesador</h6>
                <p>Intel Core i5</p>
              </div>
              <div class="col-4" id="ram">
                <h6>Memoria RAM</h6>
                <p>8 GB</p>
              </div>
              <div class="col-4" id="rom">
                <h6>Disco Duro</h6>
                <p>Disco SSD 512GB</p>
              </div>
              <div class="row">
                <div class="col-6" id="precio">
                  <h6>Precio</h6>
                  <p>$2,099,000</p>
                </div>
                <div
                  class="col align-self-center offset-md-2 text-end"
                  id="detalle"
                >
                  <h6><a v-on:click.prevent="processPortatil" href="">ver más detalles</a></h6>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
  <!-- <div class="card my-3 mx-3">
      <div class="row g-0">
        <div class="col-md-4">
          <div class="container">
            <img
              src="https://www.ktronix.com/medias/4711387355954-001-750Wx750H?context=bWFzdGVyfGltYWdlc3wxMzUzNzR8aW1hZ2Uvd2VicHxhR015TDJnd1pTOHhOREV6TVRBME5qRTROekF6T0M4ME56RXhNemczTXpVMU9UVTBYekF3TVY4M05UQlhlRGMxTUVnfGQ0ODM3ZmQwNWYyMWNjMmIwZDAxMmVlOWVlOTcyMDAzMjdjZDk3NGUyZWE4ZDkyYzE2ZWMxYjRjMzgzODcxYTc"
              class="img-fluid"
              alt="Imagen pc"
            />
          </div>
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <div class="row">
              <h5 class="card-title">
                Computador Portátil ASUS Vivobook Go OLED 15.6" Pulgadas E1504FA
                - AMD Ryzen 5 - RAM 16GB - Disco SSD 512 GB - Negro
              </h5>
            </div>
            <div class="row">
              <p>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  disabled
                >
                  AUSUS
                </button>
              </p>
            </div>
            <div class="row">
              <div class="col-4">
                <h6>Procesador</h6>
                <p>AMD Ryzen 5</p>
              </div>
              <div class="col-4">
                <h6>Memoria RAM</h6>
                <p>16 GB</p>
              </div>
              <div class="col-4">
                <h6>Disco Duro</h6>
                <p>Disco SSD 512GB</p>
              </div>
              <div class="row">
                <div class="col-6">
                  <h6>Precio</h6>
                  <p>$2,349,000</p>
                </div>
                <div class="col align-self-center offset-md-2 text-end">
                  <h6><a href="">ver más detalles</a></h6>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="card my-3 mx-3">
      <div class="row g-0">
        <div class="col-md-4">
          <div class="container">
            <img
              src="https://www.ktronix.com/medias/197498374697-001-750Wx750H?context=bWFzdGVyfGltYWdlc3wxNTQ3NjR8aW1hZ2Uvd2VicHxhREl3TDJnMllTOHhOREEzT1RVM01qUTBNekUyTmk4eE9UYzBPVGd6TnpRMk9UZGZNREF4WHpjMU1GZDROelV3U0F8NDFkY2VkN2UxY2UyMmE0M2YzNzRjMzBkZWE1MDAzN2YzZWQ0Y2E5OWMzM2M2YTE5NWFjNmQyMTVmM2M5MzA4MA"
              class="img-fluid"
              alt="Imagen pc"
            />
          </div>
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <div class="row">
              <h5 class="card-title">
                Computador Portátil HP 14" Pulgadas Dq5005la INTEL Core i5 - RAM
                12GB - Disco SSD 512GB - Plata
              </h5>
            </div>
            <div class="row">
              <p>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  disabled
                >
                  HP
                </button>
              </p>
            </div>
            <div class="row">
              <div class="col-4">
                <h6>Procesador</h6>
                <p>Intel Core i5</p>
              </div>
              <div class="col-4">
                <h6>Memoria RAM</h6>
                <p>12 GB</p>
              </div>
              <div class="col-4">
                <h6>Disco Duro</h6>
                <p>Disco SSD 512GB</p>
              </div>
              <div class="row">
                <div class="col-6">
                  <h6>Precio</h6>
                  <p>$2,099,000</p>
                </div>
                <div class="col align-self-center offset-md-2 text-end">
                  <h6><a href="">ver más detalles</a></h6>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
  <!-- </div> -->
</template>

<script>
import axios from "axios";

export default {
  emits: ["completedSignUp", "completedLogIn", "logOut", "loadPortatil", "loadNewPc"],
  name: "Home",
  data() {
    return {
      pc_portatiles : [
  {
    id: 1,
    marca: "LENOVO",
    modelo: "IdeaPad Slim 3 Tactil",
    pantalla: 15.6,
    procesador: "Intel Core i7",
    img: "https://www.ktronix.com/medias/750Wx750H-master-hotfolder-transfer-incoming-deposit-hybris-interfaces-IN-media-product-197532261341-001.jpg?context=bWFzdGVyfGltYWdlc3wxNTYwNTd8aW1hZ2UvanBlZ3xhRFV3TDJnd1pDOHhOREF3Tmprek56Z3hNekF5TWk4M05UQlhlRGMxTUVoZmJXRnpkR1Z5TDJodmRHWnZiR1JsY2k5MGNtRnVjMlpsY2k5cGJtTnZiV2x1Wnk5a1pYQnZjMmwwTDJoNVluSnBjeTFwYm5SbGNtWmhZMlZ6TDBsT0wyMWxaR2xoTDNCeWIyUjFZM1F2TVRrM05UTXlNall4TXpReFh6QXdNUzVxY0djfDNiNDY5MTViNzExNDFiMTg5YzFiMzYyMTgzNzcwMGFjMzhkYmJmZmU4YzJhODg4YmFkNDc0NjlkY2JjMzQ3OTI",
    precio: 2099000,
    ram: 8,
    rom: 512,
    color: "Gris",
    resumen: "",
  },
  {
    id: 2,
    marca: "HP",
    modelo: "IdeaPad Slim 3 Tactil",
    pantalla: 15.6,
    procesador: "Intel Core i7",
    img: "https://www.ktronix.com/medias/750Wx750H-master-hotfolder-transfer-incoming-deposit-hybris-interfaces-IN-media-product-197532261341-001.jpg?context=bWFzdGVyfGltYWdlc3wxNTYwNTd8aW1hZ2UvanBlZ3xhRFV3TDJnd1pDOHhOREF3Tmprek56Z3hNekF5TWk4M05UQlhlRGMxTUVoZmJXRnpkR1Z5TDJodmRHWnZiR1JsY2k5MGNtRnVjMlpsY2k5cGJtTnZiV2x1Wnk5a1pYQnZjMmwwTDJoNVluSnBjeTFwYm5SbGNtWmhZMlZ6TDBsT0wyMWxaR2xoTDNCeWIyUjFZM1F2TVRrM05UTXlNall4TXpReFh6QXdNUzVxY0djfDNiNDY5MTViNzExNDFiMTg5YzFiMzYyMTgzNzcwMGFjMzhkYmJmZmU4YzJhODg4YmFkNDc0NjlkY2JjMzQ3OTI",
    precio: 2099000,
    ram: 8,
    rom: 512,
    color: "Gris",
    resumen: "",
  },
  {
    id: 3,
    marca: "ASUS",
    modelo: "IdeaPad Slim 3 Tactil",
    pantalla: 15.6,
    procesador: "Intel Core i7",
    img: "https://www.ktronix.com/medias/750Wx750H-master-hotfolder-transfer-incoming-deposit-hybris-interfaces-IN-media-product-197532261341-001.jpg?context=bWFzdGVyfGltYWdlc3wxNTYwNTd8aW1hZ2UvanBlZ3xhRFV3TDJnd1pDOHhOREF3Tmprek56Z3hNekF5TWk4M05UQlhlRGMxTUVoZmJXRnpkR1Z5TDJodmRHWnZiR1JsY2k5MGNtRnVjMlpsY2k5cGJtTnZiV2x1Wnk5a1pYQnZjMmwwTDJoNVluSnBjeTFwYm5SbGNtWmhZMlZ6TDBsT0wyMWxaR2xoTDNCeWIyUjFZM1F2TVRrM05UTXlNall4TXpReFh6QXdNUzVxY0djfDNiNDY5MTViNzExNDFiMTg5YzFiMzYyMTgzNzcwMGFjMzhkYmJmZmU4YzJhODg4YmFkNDc0NjlkY2JjMzQ3OTI",
    precio: 2099000,
    ram: 8,
    rom: 512,
    color: "Gris",
    resumen: "",
  },
],
      // fields: [
      //   "referencia",
      //   "nombre",
      //   "marca",
      //   "tamaño",
      //   "procesador",
      //   "ram",
      //   "rom",
      //   "precio",
      // ],
      // username: localStorage.getItem("username") || "none",
      // referencia: "",
      // nombre: "",
      // marca: "",
      // tamaño: "",
      // procesador: "",
      // ram: "",
      // rom: "",
      // precio: "",
      // listarDatos: [],
    };
  },

  mounted() {
    // this.loadPopularPc();

    // axios
    //   .get("http://127.0.0.1:8000/lista/")
    //   .then((response) => {
    //     this.listarDatos = response.data;
    //     console.log(this.listarDatos);
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   })
    //   .finally(function () {
    //     //se ejecuta sin problemas
    //   });
  },

  methods: {
    createPcElement(pc) {
      const pcElement = document.createElement("div");
      pcElement.classList.add("card-container");
      pcElement.innerHTML = `
    <div class= "card my-3 mx-3">
    <div class="row g-0" id="contenedor-card">
        <div class="col-md-4">
          <div class="container" id="contenedor-img">
            <img
              src="${pc.img}"
              class="img-fluid"
              alt="Imagen pc"
            />
          </div>
        </div>
        <div class="col-md-8" id="contenedor-info">
          <div class="card-body">
            <div class="row">
              <h5 class="card-title" id="nombre-pc">
                Computador Portátil ${pc.marca} - ${pc.pantalla}" ${pc.modelo} - ${pc.procesador} - ${pc.ram}GB - Disco SSD${pc.rom}GB - ${pc.color}.
              </h5>
            </div>
            <div class="row" id="marca">
              <p>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  disabled
                >
                  ${pc.marca}
                </button>
              </p>
            </div>
            <div class="row" id="datos-pc">
              <div class="col-4" id="procesador">
                <h6>Procesadr</h6>
                <p>${pc.procesador}</p>
              </div>
              <div class="col-4" id="ram">
                <h6>Memoria RAM</h6>
                <p>${pc.ram} GB</p>
              </div>
              <div class="col-4" id="rom">
                <h6>Disco Duro</h6>
                <p>Disco SSD ${pc.rom}GB</p>
              </div>
              <div class="row">
                <div class="col-6" id="precio">
                  <h6>Precio</h6>
                  <p>$ ${pc.precio}</p>
                </div>
                <div
                  class="col align-self-center offset-md-2 text-end"
                  id="detalle"
                >
                  <p class="invisible" id="idPc">${pc.id}</p>
                  <h6><a v-on:click.prevent="processPortatil" class="verDetalles" href="#">ver más detalles</a>                </h6>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    `;
      return pcElement;
    },

    loadPopularPc() {
      try {
        const lista = pc_portatiles;
        const pcContainer = document.querySelector("#card-auto");
        pcContainer.innerHTML = ""; // Limpiar el contenedor para nuevas tarjetas
        lista.forEach((pc) => {
          const pcElement = this.createPcElement(pc);
          pcContainer.appendChild(pcElement);
        });
      } catch (error) {
        console.error("Error al mostrar las películas:", error);
      }
    },

    processPortatil(pc) {
      this.$store.commit('setSelectedPc', pc);
      this.$emit("loadPortatil",pc);
    },
  },

  //Metodo para solicitar la información de un solo pc
  // methods: {
  //   getData: async function () {
  //     let idPc = 345;
  //     axios
  //       .get(`http://127.0.0.1:8000/portatil/${idPc}/`)
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

  created: async function () {},
};
</script>

<style>
.contenedor-general {
  overflow: auto;
}

/* .side-bar {
  position: fixed;
} */

/* bootstrap */

.bi {
  vertical-align: -0.125em;
  fill: currentColor;
}

.bd-mode-toggle {
  z-index: 1500;
}

.bd-mode-toggle .dropdown-menu .active .bi {
  display: block !important;
}

.dropdown-toggle {
  outline: 0;
}

.btn-toggle {
  padding: 0.25rem 0.5rem;
  font-weight: 600;
  color: var(--bs-emphasis-color);
  background-color: transparent;
}
.btn-toggle:hover,
.btn-toggle:focus {
  color: rgba(var(--bs-emphasis-color-rgb), 0.85);
  background-color: var(--bs-tertiary-bg);
}

.btn-toggle::before {
  width: 1.25em;
  line-height: 0;
  content: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='rgba%280,0,0,.5%29' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M5 14l6-6-6-6'/%3e%3c/svg%3e");
  transition: transform 0.35s ease;
  transform-origin: 0.5em 50%;
}

.btn-toggle[aria-expanded="true"] {
  color: rgba(var(--bs-emphasis-color-rgb), 0.85);
}
.btn-toggle[aria-expanded="true"]::before {
  transform: rotate(90deg);
}

.btn-toggle-nav a {
  padding: 0.1875rem 0.5rem;
  margin-top: 0.125rem;
  margin-left: 1.25rem;
}
.btn-toggle-nav a:hover,
.btn-toggle-nav a:focus {
  background-color: var(--bs-tertiary-bg);
}
</style>
