let apiUrl: string = '';
let staticUrl: string = '';

if (process.env.ENVIRONMENT === 'production') {
  apiUrl = 'https://mi8l1qiq2g.execute-api.us-east-1.amazonaws.com/prod';
} else {
  apiUrl = 'http://localhost:8001/api';
}

export { apiUrl, staticUrl };