const ageInput = document.querySelector("#age")
const message = document.querySelector("#msg")

function validateAge(value) {
    const number = Number(value)
    if (Number.isNaN(number)) {
        return false
    }

    if (number < 5) {
        return false
    }
    if (number > 130) {
        return false
    }
    return true
}

function handleInput() {
    const value = ageInput.value
    if (validateAge(value)) {
        message.textContent = "Age accepted"
    } else {
        message.textContent = "Invalid age"
    }
}

ageInput.addEventListener("input", handleInput)
