// frontend/src/components/ProductTracker.js
import React, { useState } from 'react';
import axios from 'axios';


function ProductTracker() {
    const [url, setUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const fetchData = async () => {
        setLoading(true);
        try {
            let destUrl = `http://localhost:5000/scrape?url=${encodeURIComponent(url)}`
            console.log(destUrl)
            const response = await axios.get(destUrl);
            setData(response.data);
            setError(null);
        } catch (error) {
            setError(error.message);
        }
        setLoading(false);
    };

    return (
        <div>
            <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} />
            <button onClick={fetchData} disabled={loading}>Fetch Data</button>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error}</p>}
            {data && (
                <div>
                    <h2>{data.description}</h2>
                    <p>Price: {data.price}</p>
                    <p>Customer Ratings: {data.customer_ratings}</p>
                    <p>Number of Reviews: {data.number_of_reviews}</p>
                    <p>Specifications:</p>
                    <ul>
                        {Object.entries(data.specifications).map(([key, value]) => (
                            <li key={key}>{key}: {value}</li>
                        ))}
                    </ul>
                    <div>
                        {data.image_urls.map((imageUrl, index) => (
                            <img key={index} src={imageUrl} alt={`Product ${index + 1}`} />
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}

export default ProductTracker;
