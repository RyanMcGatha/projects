"use strict";
const categoryListFormEl = document.querySelector("#categoryListForm");

document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM IS READY");

  const apiurl = "https://api.chucknorris.io/jokes/random?category=dev";
  generateQuote(apiurl);

  const categoriesUrl = "https://api.chucknorris.io/jokes/categories";
  get(categoriesUrl).then(function (response) {
    console.log("CATEGORY RESPONSE:", response);
    generateCategoryList(response);
  });

  categoryListFormEl.addEventListener("submit", function (event) {
    const newCategory = this.querySelector("select").value;
    const apiUrl = `https://api.chucknorris.io/jokes/random?category=${newCategory}`;
    generateQuote(apiUrl, chuckPng);
  });

  function generateQuote() {
    get("https://api.chucknorris.io/jokes/random?category=dev").then(function (
      response
    ) {
      chuckQuote.innerText = response.value;
    });
  }

  function generateCategoryList(categoryArray) {
    const selectEl = document.createElement("select");
    // Filter out the explicit category
    const filteredCategories = categoryArray.filter(function (category) {
      if (category !== "explicit") {
        return category;
      }
    });
    filteredCategories.map(function (category) {
      // create an option element
      const option = document.createElement("option");
      // define option attributes
      option.value = category;
      option.text = category;
      // append the option to the <select>
      selectEl.appendChild(option);
    });
    // append the <select> to the <form>
    categoryListFormEl.append(selectEl);
  }
});
