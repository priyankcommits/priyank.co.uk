let apiUrl: string = '';
let staticUrl: string = '';

if (process.env.ENVIRONMENT === 'production') {
  apiUrl = 'https://oe5a4xnzh8.execute-api.us-east-1.amazonaws.com/prod/api';
} else {
  apiUrl = 'http://localhost:8001/api';
}

export { apiUrl, staticUrl };