document
  .getElementById("formData")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch("/submit", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("message").innerText = data.message;
      })
      .catch((error) => console.error("Error:", error));
  });
