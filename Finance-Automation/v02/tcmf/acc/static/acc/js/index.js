// assiging the button variabel to the button to be clicked
$(document).on('submit', '#add-data-form',function(e){
    // prevent page from getting refresh
    e.preventDefault();

    console.log("Form Submitted"); // sanity check

    add_data();
});

function add_data(){
    console.log("add data is working"); // sanity check
    console.log($('#GST'-{{ data_row.6}}).val());
}