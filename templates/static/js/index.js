import '../css/main.css';
import oExtract from './extractHandler';
import oProduct from './productHandler';

let mod = document.body.dataset['mod']
switch(mod) {
    case 'home':
        break;
    case 'extract':
        oExtract.init();
        break;
    case "product":
        oProduct.init();
        break;
    case "products":
        oProduct.init();
        break;
}
