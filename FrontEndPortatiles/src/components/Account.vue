<template>
  <div v-if="loaded" class="information">
    <h1>Información de su cuenta</h1>
    <h2>
      Nombre: <span>{{ name }}</span>
    </h2>
    <h2>
      Correo electrónico: <span>{{ email }}</span>
    </h2>
  </div>
</template>
<script>
// import jwt_decode from "jwt-decode";
import * as jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Account",
  data: function () {
    return {
      name: "",
      email: "",
      loaded: false,
    };
  },

  methods: {
    getData: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      await this.verifyToken();
      let token = localStorage.getItem("token_access");
      let decodeToken = JSON.parse(atob(token.split(".")[1]));
      let userId = decodeToken.user_id;
      console.log(userId)

      axios
        .get(`http://127.0.0.1:8000/user/${userId}/`, {
          headers: { Authorization: `Bearer ${token}`},
        })
        .then((response) => {
          this.name = response.data.name;
          this.email = response.data.email;
          this.loaded = true;
        })
        .catch(() => {
          console.log()
          this.$emit("logOut");
        });
    },
    verifyToken: function () {
      return axios
        .post(
          "http://127.0.0.1:8000/refresh/",
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
  },
  created: async function () {
    this.getData();
  },
};
</script>

<style>
.information {
  margin: 0;
  padding: 0%;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.information h1 {
  font-size: 60px;
  color: #0f1316;
}
.information h2 {
  font-size: 40px;
  color: #283747;
}
.information span {
  color: crimson;
  font-weight: bold;
}
</style>
