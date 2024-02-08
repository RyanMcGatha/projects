"use strict";

document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM READY");
  const moodForm = document.querySelector("#moodRing");
  const myMood = document.querySelector("#myMood");

  moodForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const moodInput = moodForm.querySelector("input[name=mood]:checked");
    myMood.innerText = moodInput.value;

    switch (moodInput.value) {
      case "very-happy":
        toggleClass(myMood, "very-happy", ["happy", "die"]);
        break;
      case "happy":
        toggleClass(myMood, "happy", ["very-happy", "die"]);
        break;
      case "die":
        toggleClass(myMood, "die", ["very-happy", "happy"]);
        break;
      default:
        break;
    }
  });
});

function toggleClass(element, className, classesToRemove) {
  console.log(element, className, classesToRemove);
  if (element.classList.contains(className)) {
    element.classList.remove(className);
  } else {
    element.classList.add(className);
  }

  if (classesToRemove.length > 0) {
    classesToRemove.forEach(function (className) {
      if (element.classList.contains(className)) {
        element.classList.remove(className);
      }
    });
  }
}
