$(document).ready( function () {
    $('.pandas').DataTable({
        scrollY: 500,
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        fixedColumns: true,
    });
 
    $('.pandas td').each( function() {
        $(this).replaceWith($('<td contenteditable="true">' + this.innerHTML + '</td>'));

    });
} );
