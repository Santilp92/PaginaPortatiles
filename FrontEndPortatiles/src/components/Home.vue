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

  <div
    class="container-fluid contenedor-general"
    id="card-auto"
    style="width: 100%"
  >
    <div id="app">
      <div v-for="pc in listaPc" :key="pc.id" class="card-container">
        <div class="card my-3 mx-3">
          <div class="row g-0" id="contenedor-card">
            <div class="col-md-4">
              <div class="container" id="contenedor-img">
                <img
                  :src="getMediaUrl(pc.imagen)"
                  class="img-fluid"
                  alt="Imagen pc"
                />
              </div>
            </div>
            <div class="col-md-8" id="contenedor-info">
              <div class="card-body">
                <div class="row" id="nombre-pc">
                  <h5 class="card-title">
                    Computador Portátil {{ pc.marca }} - {{ pc.pantalla }}"
                    {{ pc.modelo }} - {{ pc.procesador }} - {{ pc.ram }}GB -
                    Disco SSD{{ pc.rom }}GB - {{ pc.color }}.
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
                    <div class="col" id="precio">
                      <h6>Precio</h6>
                      <p>$ {{ pc.precio }}</p>
                    </div>
                    <div
                      class="col align-self-center offset-md-2 text-end"
                      id="detalle"
                    >
                      <p class="invisible" id="idPc">{{ pc.id }}</p>
                      <h6 id="verDetalles">
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
</template>

<script>
import axios from "axios";

export default {

  name: "Home",

  emits: [
    "completedSignUp",
    "completedLogIn",
    "logOut",
    "loadPortatil",
    "loadNewPc",
    "loadHome"
  ],

  data() {
    return {
      listaPc: [],
    };
  },

  mounted() {
    axios
      .get("https://santilp92.pythonanywhere.com/lista/")
      .then((response) => {
        this.listaPc = response.data;
      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {});
  },

  methods: {
    processPortatil(pc) {
      this.$store.commit("setSelectedPc", pc);
      this.$emit("loadPortatil", pc);
    },

    getMediaUrl(filename) {
      return `http://127.0.0.1:8000/${filename}`;
    },
  },
};
</script>

<style>
.contenedor-general {
  overflow: auto;
}

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
