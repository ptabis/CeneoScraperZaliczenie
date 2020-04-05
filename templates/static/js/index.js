import '../css/main.css';
import oExtract from './extractHandler';
import oProduct from './productHandler';
import oChart from './chartHandler';

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
    case "charts":
        oChart.init();
        break;
}
