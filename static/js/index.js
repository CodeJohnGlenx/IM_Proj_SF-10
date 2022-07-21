let inputSearch = document.querySelector('.input-search');
let inputSearchBy = document.querySelector('.input-search-by');
let btnSubmit = document.querySelector('.btn-submit');
const btnEditStudentRecord = document.querySelector('.btn-edit-student-record');
const inputEditStudentRecordId = document.querySelector('.edit-student-record-id');

btnSubmit.addEventListener('click', function(event) {
    if (inputSearch.value.trim().length == 0 && inputSearchBy.value !== 'lrn') {
        alert("please enter search value");
        event.preventDefault();
    }
});

btnEditStudentRecord.addEventListener('click', function(event) {
    let studentID = prompt("Enter Student ID: ");
    // check if studentID input is valid 
    if (!Number(studentID)) {
        alert(`Student ID: ${studentID} is not a valid input.`);
        event.preventDefault();        

    // set value of input edit-student-record-id 
    } else {
        inputEditStudentRecordId.value = studentID;
    }
});



