<template>
  <div>
    <div class="alert alert-success alert-dismissible" role="alert">
      {{ message }}
      <button
        type="button"
        class="btn-close fade show"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["message"],
};
</script>
