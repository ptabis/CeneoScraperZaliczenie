const webpack = require('webpack');
const resolve = require('path').resolve;

const config = {
      devtool: 'source-map',
      entry: __dirname + '/templates/static/js/index.js',
      output: {
            path: resolve('templates/public'),
            filename: 'bundle.js',
            publicPath: resolve('templates/public')
      },
      resolve: {
            extensions: ['.js']
      },
      module: {
            rules: [
                  {
                        test: /\.css$/i,
                        use: ['style-loader', 'css-loader']
                  }
            ]
      }
};
module.exports = config;
