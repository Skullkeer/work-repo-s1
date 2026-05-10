// const countOutput = document.querySelector("#count")
// const incOutput = document.querySelector("#inc")
// const resetOutput = document.querySelector("#reset")
//
// let count = 0
//
// function render() {
//     countOutput.textContent = count
//
// }
//
// function reset() {
//     count = 0
//     render()
// }
//
// function increment() {
//     count = count + 1
//     render()
// }
//
// incButton.addEventListener("click", increment)
// render()
//


const countOutput = document.querySelector("#count")
const incButton = document.querySelector("#inc")
const resetButton = document.querySelector("#reset")

// const counterInput = document.querySelector("#counterInput")

let count = 0

function render() {
    countOutput.textContent = count

     if (count > 20) {
       incButton.disabled = true
     }
}

function increment() {
    count = count + 1
    render()
}

function reset() {
    count = 0
    render()
}


/*
 *
 *
 * function handleEnter(event) {
 *  if (event.key === "Enter") {
 *    increment()
 *    counterInput.value = ""
 *  }
 * }
 *
 * counterInput.addEventListener("keydown", handleEnter)
 *
 *
 */

incButton.addEventListener("click", increment)
resetButton.addEventListener("click", reset)

render()
