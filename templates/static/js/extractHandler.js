var oExtract = {
    sel: {
        productId: '#product-id',
        extractionStart: '#extraction-start',
        extractionLoader: '#extraction-loader'
    },
    init: function() {
        document.querySelector(oExtract.sel.productId).onkeypress = function(e) {
            let key = event.which || event.keyCode
            if(key == 13){ //enter
                oExtract.extractFromId();
            }
        }
        document.querySelector(oExtract.sel.extractionStart).onclick = function(e) {
            e.preventDefault();
            oExtract.extractFromId();
        };
    },
    extractFromId: function() {
        document.querySelector(oExtract.sel.extractionLoader).classList.toggle("d-none");
        window.location = '/extract/'+document.querySelector(oExtract.sel.productId).value;
    }
}

export default oExtract;