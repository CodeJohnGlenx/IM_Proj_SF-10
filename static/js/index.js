let inputSearch = document.querySelector('.input-search');
let inputSearchBy = document.querySelector('.input-search-by');
let btnSubmit = document.querySelector('.btn-submit');
const btnEditStudentRecord = document.querySelector('.btn-edit-student-record');
const inputEditStudentRecordId = document.querySelector('.edit-student-record-id');
const btnEditEnrollmentRecord = document.querySelector('.btn-edit-enrollment-record');
const inputEditEnrollmentID = document.querySelector('.edit-enrollment-id');
const inputEditSchoolYear = document.querySelector('.edit-enrollment-school-year');
const btnDeleteEnrollmentRecord = document.querySelector('.btn-delete-enrollment-record');
const deleteEnrollmentId = document.querySelector('.delete-enrollment-id');
const deleteEnrollmentSchoolYear = document.querySelector('.delete-enrollment-school-year');
const btnDeleteStudentRecord = document.querySelector('.btn-delete-student-record');
const inputDeleteStudentRecordId = document.querySelector('.delete-student-record-id');


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

btnEditEnrollmentRecord.addEventListener('click', function(event) {
    let studentID = prompt("Enter Student ID: ");

    // check if studentID input is valid 
    if (!Number(studentID)) {
        alert(`Student ID: ${studentID} is not a valid input.`);
        event.preventDefault();        
        return ;
    }

    let schoolYear = prompt("Enter School Year (e.g. 2016): ");

    // check if school year input is valid 
    if (!Number(schoolYear)) {
        alert(`School Year: ${schoolYear} is not a valid input.`);
        event.preventDefault(); 
        return ;
    }

    inputEditEnrollmentID.value = studentID;
    inputEditSchoolYear.value = schoolYear;
})




btnDeleteEnrollmentRecord.addEventListener('click', function(event) {
    let studentID = prompt("Enter Student ID: ");

    // check if studentID input is valid 
    if (!Number(studentID)) {
        alert(`Student ID: ${studentID} is not a valid input.`);
        event.preventDefault();        
        return ;
    }

    let schoolYear = prompt("Enter School Year (e.g. 2016): ");

    // check if school year input is valid 
    if (!Number(schoolYear)) {
        alert(`School Year: ${schoolYear} is not a valid input.`);
        event.preventDefault(); 
        return ;
    }

    let confirmDelete = confirm(`Delete Student ID: ${studentID} School Year: ${schoolYear}?`);

    if (!confirmDelete) {
        event.preventDefault(); 
        return ;
    }

    deleteEnrollmentId.value = studentID;
    deleteEnrollmentSchoolYear.value = schoolYear;
});

btnDeleteStudentRecord.addEventListener('click', function(event) {
    let studentID = prompt("Enter Student ID: ");
    // check if studentID input is valid 
    if (!Number(studentID)) {
        alert(`Student ID: ${studentID} is not a valid input.`);
        event.preventDefault();    
        return ;    
    // set value of input edit-student-record-id 
    } 

    let confirmDelete = confirm(`Delete Student ID: ${studentID}? and its enrollment record?`);

    if (!confirmDelete) {
        event.preventDefault();
        return ;
    }

    inputDeleteStudentRecordId.value = studentID;
    
});



