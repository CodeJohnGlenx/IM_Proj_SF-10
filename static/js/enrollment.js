const inputStudentID = document.querySelector('#input-student-id');
const inputDivision = document.querySelector('#input-division');
const inputRegion = document.querySelector('#input-region');
const inputDistrict = document.querySelector('#input-district');
const inputEntranceDate = document.querySelector('#input-entrance-date');
const inputSchoolYear = document.querySelector('#input-school-year');
const inputLevelSection = document.querySelector('#input-level-section');
const inputActionTaken = document.querySelector('#input-action-taken');
const option = document.querySelector('.option').textContent;

// set max of entrance date to today
let todayStr = new Date();
let year = todayStr.getFullYear();
let month = `${todayStr.getMonth() + 1}`.padStart(2, "0");
let day = `${todayStr.getDate()}`.padStart(2, "0")
inputEntranceDate.setAttribute('max', [year, month, day].join('-'));


// initialize division value or set it based on session 
if (inputDivision.getAttribute('_value')) {
    inputDivision.value = inputDivision.getAttribute('_value');
}

// initialize level and section value or set it based on session 
if (inputLevelSection.getAttribute('_value')) {
    inputLevelSection.value = inputLevelSection.getAttribute('_value');
}

if (option === 'EDIT') {
    inputStudentID.readOnly = true;
    window.addEventListener('load', (event) => {
        schoolYear = Number(inputEntranceDate.value.split('-')[0]);
        inputSchoolYear.value = schoolYear + '-' + (schoolYear + 1);

        inputEntranceDate.setAttribute('min', `${schoolYear}-01-01`);
        inputEntranceDate.setAttribute('max', [year, month, day].join('-'));
    });
}


// initialize level and section value or set it based on session 
if (inputActionTaken.getAttribute('_value')) {
    inputActionTaken.value = inputActionTaken.getAttribute('_value');
}



// set value of region and district based on division 
if (inputDivision.value === "Malabon City") {
    inputDistrict.value = 3;
} else if (inputDivision.value === "Quezon City") {
    inputDistrict.value = 1;
}
inputRegion.value = "NCR"



// division change value
inputDivision.addEventListener('change', () => {
    if (inputDivision.value === "Malabon City") {
        inputDistrict.value = 3;
    } else if (inputDivision.value === "Quezon City") {
        inputDistrict.value = 1;
    }
    inputRegion.value = "NCR"
});


// entrance date change value 
inputEntranceDate.addEventListener('change', () => {
    schoolYear = Number(inputEntranceDate.value.split('-')[0]);
    inputSchoolYear.value = schoolYear + '-' + (schoolYear + 1);
});



