let btnsDel = document.querySelectorAll('.btn-delete');

for (const btn of btnsDel) {
    btn.addEventListener('click', function(event){
        deleteConfirmation = confirm(`Are you sure you want to delete Student ID: ${btn.getAttribute('student_id')} and its enrollment record?`);
        if (!deleteConfirmation) {
            event.preventDefault();
        }
        if (deleteConfirmation) {
            alert(`Student ID: ${btn.getAttribute('student_id')} deleted.`);
        }
    })
}