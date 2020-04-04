import $ from 'jquery';
import 'datatables.net';
import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css';

let oProduct = {
    sel: {

    },
    data: {
        mod: document.body.dataset['mod']
    },
    init: function() {
        switch(oProduct.data.mod) {
            case 'products':
                oProduct.productTable();
                break;

            case 'product':
                oProduct.opinionTable();
                break;
        }
    },
    productTable: function() {
        console.log("xD")
        $('#products-table').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/Polish.json"
            },
            "dom": '<"top"ilf>rt<"bottom"p><"clear">',
            "scrollX": true,
            "scrollY": true
        });
    },
    opinionTable: function() {
        $('#opinions-table').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/Polish.json"
            },
            "dom": '<"top"ilf>rt<"bottom"p><"clear">',
            "scrollX": true,
            "scrollY": true
        });
        $('div.dataTables_filter input').addClass('form-control');
        $('div.dataTables_filter select').addClass('form-control');
    }
}

export default oProduct;