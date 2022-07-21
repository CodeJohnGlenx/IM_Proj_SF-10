
let resultData = document.querySelector('.result-data').getAttribute('_value').toUpperCase();
let option = document.querySelector('.option-data').textContent.toUpperCase();
let btnSubmit = document.querySelector('.btn-submit'); 
let inputTexts = document.querySelectorAll('input[type="text"]');
let inputGender = document.querySelector('#input-gender');

if (resultData.includes("'GENDER': 'M'")) {
    inputGender.value = 'M'
} else if (resultData.includes("'GENDER': 'F'")) {
    inputGender.value = 'F'
}

if (option === 'READ') {
    let inputs = document.querySelectorAll('input');
    for (const input of inputs) {
        input.disabled = true;
        input.placeholder = ""
    }

    let selects = document.querySelectorAll('select');
    for (const select of selects) {
        select.disabled = true;
        select.value = select.getAttribute('_value');
    }
}

for (const inText of inputTexts) {
    inText.addEventListener('blur', function() {
        inText.value = inText.value.trim();
    });
}

