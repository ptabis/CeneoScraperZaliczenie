import '../css/main.css';
import $ from 'jquery';
import 'datatables.net';
import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css';

let mod = document.body.dataset['mod']
switch(mod) {
    case 'home':
        break;
    case 'extract':
        document.querySelector('#extraction_start').onclick = function(e) {
            e.preventDefault()
            window.location = '/extract/'+document.querySelector('#product_id').value
        };
        break;
    case "product":
        $('#opinions-table').DataTable();
        $('div.dataTables_filter input').addClass('form-control');
        $('div.dataTables_filter select').addClass('form-control');
        break;
}
