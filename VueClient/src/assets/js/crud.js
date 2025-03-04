import axios from 'axios';
import { Response } from './response.js';

// Create a bok and send a Post Request
export async function createBook(playload)
{
    // Initialize the path
    const path = 'http://localhost:5000/';

    // Send a post request to the server
    await axios.post(path, playload).then(() => 
        {
            Response();

        }).catch((error) => {
            console.error(error);
        });
};
// Delete a book and send a delete request
export async function removeBook(ID)
{
    // Initialize the path
    const path = `http://localhost:5000/${ID}`;
    
    // Send a delete request to the server
    await axios.delete(path).then(() => 
        {
            Response();

        }).catch((error) => {
            console.error(error);
        });
};

// Update a book and send Put Request
export async function updateBook(payload)
{
    //  Initialize the path
    const path = `http://localhost:5000/${payload.id}`;

    // Send a post request to the server
    await axios.put(path, payload).then(() => 
        {
            Response();
            console.log('Book updated successfully', payload);
        }).catch((error) => {
        console.error(error);
        });
        
    
};

